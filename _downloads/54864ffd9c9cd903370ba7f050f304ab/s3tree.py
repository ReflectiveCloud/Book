"""
s3tree.py — Tiny S3 tree browser for simulation datasets

Usage (API):
    from s3tree import (
        list_variables, print_variables,
        show_tree, show_tree_for_variable,
        build_tree_with_sizes, print_tree_with_sizes,
    )

    # List variables (subdirectories) under a group prefix:
    print_variables(bucket="my-bucket", group="gauss")

    # Print the whole tree for a group:
    show_tree(bucket="my-bucket", group="gauss")

    # Print only one variable's subtree:
    show_tree_for_variable(bucket="my-bucket", group="gauss", variable="TREFHT")

CLI:
    python s3tree.py <bucket> <group>
    -> Lists variables and prompts to show a specific variable or ALL.

Requirements:
    - boto3
    - Valid AWS credentials (env vars, ~/.aws/credentials, IAM role, etc.)

Notes:
    - S3 is flat; "directories" are simulated using key prefixes separated by '/'
    - Directory sizes shown are sums of contained file sizes (keys ending with '/' are ignored)
"""
from __future__ import annotations

import sys
import boto3
from collections import defaultdict
from typing import Dict, Iterable, Iterator, List, Optional, Tuple

# ----------------------------- utilities -----------------------------

def sizeof_fmt(num: float, suffix: str = "B") -> str:
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Y{suffix}"

def _norm_prefix(*parts: str) -> str:
    # join path parts with '/', ensure trailing slash for S3 prefix listing
    joined = "/".join(p.strip("/") for p in parts if p is not None and p != "")
    return f"{joined}/" if joined else ""

def _is_dir_marker(key: str) -> bool:
    # Some tools upload zero-byte "directory marker" objects ending in '/'
    return key.endswith("/")

# --------------------------- S3 listing core --------------------------

def iter_objects(bucket: str, prefix: str, s3=None) -> Iterator[Tuple[str, int]]:
    """
    Yield (key, size) for all objects under s3://bucket/prefix
    """
    if s3 is None:
        s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=prefix):
        for obj in page.get("Contents", []):
            yield obj["Key"], obj["Size"]

def list_variables(bucket: str, group: str, s3=None) -> List[str]:
    """
    Return sorted immediate subdirectory names under s3://bucket/group/ using Delimiter='/'.
    Fast and does not compute sizes.
    """
    if s3 is None:
        s3 = boto3.client("s3")
    base = _norm_prefix(group)
    names = set()
    paginator = s3.get_paginator("list_objects_v2")
    for page in paginator.paginate(Bucket=bucket, Prefix=base, Delimiter="/"):
        for cp in page.get("CommonPrefixes", []):
            child = cp["Prefix"][len(base):-1]  # strip base and trailing slash
            names.add(child)
    return sorted(names)

def compute_prefix_size(bucket: str, prefix: str, s3=None) -> int:
    """
    Sum sizes of all objects under s3://bucket/prefix
    """
    total = 0
    for _, size in iter_objects(bucket, prefix, s3=s3):
        total += size
    return total

def list_variables_with_sizes(bucket: str, group: str, s3=None) -> List[Tuple[str, int]]:
    """
    Return a sorted list of (name, total_size_bytes) for immediate subdirectories
    under s3://bucket/group/. Computes each variable's total by scanning its subtree.
    """
    if s3 is None:
        s3 = boto3.client("s3")
    vars_only = list_variables(bucket, group, s3=s3)
    result: List[Tuple[str, int]] = []
    for name in vars_only:
        prefix = _norm_prefix(group, name)
        size = compute_prefix_size(bucket, prefix, s3=s3)
        result.append((name, size))
    return sorted(result, key=lambda x: x[0])

# ----------------------------- tree model ----------------------------

def _make_node() -> Dict:
    # Each node contains nested children, cumulative size, and file/dir flag
    return {"children": defaultdict(_make_node), "size": 0, "is_file": False}

def build_tree_with_sizes(items: Iterable[Tuple[str, int]]) -> Dict:
    """
    items: iterable of (key, size) pairs; directory markers are skipped.
    Builds a nested tree; directory node size equals sum of contained file sizes.
    """
    root = _make_node()
    for key, size in items:
        if _is_dir_marker(key):
            continue
        parts = [p for p in key.strip("/").split("/") if p]
        cur = root
        cur["size"] += size  # root cumulative
        for i, part in enumerate(parts):
            cur = cur["children"][part]
            cur["size"] += size
            if i == len(parts) - 1:
                cur["is_file"] = True
    return root

def _sorted_items(node: Dict):
    # directories first (False), then files (True), both alphabetical
    return sorted(node["children"].items(), key=lambda kv: (kv[1]["is_file"], kv[0]))

def print_tree_with_sizes(node: Dict, indent: int = 0) -> None:
    for name, child in _sorted_items(node):
        human = sizeof_fmt(child["size"])
        if child["is_file"]:
            print(" " * indent + f"|_ {name}  ({human})")
        else:
            print(" " * indent + f"|_ {name}/  ({human} total)")
            print_tree_with_sizes(child, indent + 2)

def _find_subtree(root: Dict, path: str) -> Optional[Dict]:
    parts = [p for p in path.strip("/").split("/") if p]
    node = root
    for part in parts:
        if part in node["children"]:
            node = node["children"][part]
        else:
            return None
    return node

# --------------------------- user-facing API --------------------------

def print_variables(bucket: str, group: str, show_sizes: bool = True, s3=None) -> None:
    """
    Print variables (subdirectories) under s3://bucket/group/.
    If show_sizes=True, also prints total size per variable (slower).
    """
    if show_sizes:
        vars_with_sizes = list_variables_with_sizes(bucket, group, s3=s3)
        if not vars_with_sizes:
            print(f"No subdirectories found under s3://{bucket}/{group}/")
            return
        for i, (name, size) in enumerate(vars_with_sizes, 1):
            print(f"{i:2d}. {name:<20} {sizeof_fmt(size)}")
    else:
        names = list_variables(bucket, group, s3=s3)
        if not names:
            print(f"No subdirectories found under s3://{bucket}/{group}/")
            return
        for i, name in enumerate(names, 1):
            print(f"{i:2d}. {name}")

def show_tree(bucket: str, group: str, s3=None) -> None:
    """
    Build and print the FULL tree under s3://bucket/group/
    (May be slow/expensive for very large prefixes.)
    """
    base = _norm_prefix(group)
    items = list(iter_objects(bucket, base, s3=s3))
    if not items:
        print(f"No objects under s3://{bucket}/{group}/")
        return
    tree = build_tree_with_sizes(items)
    # print subtree rooted at 'group' if present, else print entire loaded tree
    node = _find_subtree(tree, group)
    if node is None:
        node = tree
        label = group
    else:
        label = group
    total = sizeof_fmt(node["size"])
    print(f"|_ {label}/  ({total} total)")
    print_tree_with_sizes(node, indent=2)

def show_tree_for_variable(bucket: str, group: str, variable: str, s3=None) -> None:
    """
    Print the tree just for a given variable (subdirectory) under the group.
    """
    var_prefix = _norm_prefix(group, variable)
    items = list(iter_objects(bucket, var_prefix, s3=s3))
    if not items:
        print(f"No objects under s3://{bucket}/{group}/{variable}/")
        return
    tree = build_tree_with_sizes(items)
    total = sizeof_fmt(tree["size"])
    print(f"|_ {group}/{variable}/  ({total} total)")
    print_tree_with_sizes(tree, indent=2)

# ------------------------------ CLI mode ------------------------------

def _prompt_choice(n: int) -> str:
    return input(f"Choose a variable by number (1-{n}), or 'a' for ALL, or 'q' to quit: ").strip()

def main(argv: List[str]) -> int:
    if len(argv) < 3:
        print("Usage: python s3tree.py <bucket> <group>")
        return 2
    bucket, group = argv[1], argv[2]
    print(f"Listing variables under s3://{bucket}/{group}/ ...\\n")
    names = list_variables(bucket, group)
    if not names:
        print(f"No subdirectories found under s3://{bucket}/{group}/")
        return 0
    # Show sizes (could be slow if many); opt for names only here
    for i, name in enumerate(names, 1):
        print(f"{i:2d}. {name}")
    print()
    while True:
        choice = _prompt_choice(len(names)).lower()
        if choice == "q":
            return 0
        if choice == "a":
            print(f"\\nBuilding full tree for s3://{bucket}/{group}/ ...\\n")
            show_tree(bucket, group)
            print("\\nDone.")
            return 0
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(names):
                var = names[idx-1]
                print(f"\\nBuilding tree for s3://{bucket}/{group}/{var}/ ...\\n")
                show_tree_for_variable(bucket, group, var)
                print("\\nDone.")
                return 0
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))