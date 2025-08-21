# S3 Tree Browser Utility

This utility provides a convenient way to browse and explore S3 datasets, particularly useful for climate simulation data stored in cloud storage.

## Overview

The `s3tree.py` utility is designed to help researchers and data scientists navigate large S3 datasets by providing:

- **Variable Listing**: Quickly see what variables (subdirectories) are available under a group prefix
- **Tree Visualization**: Display complete directory structures with file sizes
- **Interactive CLI**: Command-line interface for exploring datasets
- **Efficient S3 Operations**: Uses pagination and optimized listing for large datasets

## Features

- List variables (subdirectories) under a group prefix
- Show complete directory trees with file sizes
- Interactive CLI mode for exploration
- Efficient S3 listing with pagination
- Human-readable file size formatting (B, KB, MB, GB, etc.)
- Support for both API and command-line usage

## Usage Examples

### Python API

```python
from s3tree import (
    list_variables, print_variables,
    show_tree, show_tree_for_variable,
    build_tree_with_sizes, print_tree_with_sizes,
)

# List variables under a group prefix (fast, no size computation)
print_variables(bucket="my-bucket", group="gauss", show_sizes=False)

# List variables with sizes (slower but more informative)
print_variables(bucket="my-bucket", group="gauss", show_sizes=True)

# Show complete tree for a group
show_tree(bucket="my-bucket", group="gauss")

# Show tree for a specific variable only
show_tree_for_variable(bucket="my-bucket", group="gauss", variable="TREFHT")

# Get raw data for custom processing
variables = list_variables(bucket="my-bucket", group="gauss")
variables_with_sizes = list_variables_with_sizes(bucket="my-bucket", group="gauss")
```

### Command Line Interface

```bash
# Basic usage
python s3tree.py <bucket> <group>

# Example
python s3tree.py my-climate-data gauss
```

The CLI will:

1. List all available variables under the specified group
2. Prompt you to choose a specific variable or view all
3. Display the tree structure with file sizes

## Installation

```bash
pip install boto3
```

## How It Works

### S3 Structure Understanding

S3 is actually a flat key-value store, but the utility simulates directory structures using key prefixes separated by `/`. For example:

- `gauss/TREFHT/2020/01/01.nc` appears as a file in a nested directory structure
- The utility groups keys by common prefixes to show the "tree" structure

## Example Output

```
Listing variables under s3://my-bucket/gauss/ ...

 1. TREFHT                   2.1GB
 2. PRECT                    1.8GB

Building tree for s3://my-bucket/gauss/TREFHT/ ...

|_ gauss/TREFHT/  (2.1GB total)
  |_ 2020/  (1.1GB total)
    |_ 01/  (100MB total)
      |_ 01.nc  (3.2MB)
      |_ 02.nc  (3.2MB)
      |_ ...
  |_ 2021/  (1.0GB total)
    |_ 01/  (90MB total)
      |_ 01.nc  (3.0MB)
      |_ ...
```

## Code Reference

The complete implementation is available in [s3tree.py](s3tree.py). The utility is well-documented with type hints and includes comprehensive error handling for S3 operations.
