# issue-creds — Guide for Hub Users

`issue-creds` vends **short-lived, scope-limited AWS S3 credentials** from inside
the Hub. Instead of long-lived keys, you request exactly the access you need
(read or write) for a bounded time.

> **Beta:** this tool is new. Flags and defaults may change, and you may hit rough
> edges — please report anything surprising (see [Getting help](#getting-help)).

## Quick start
You can generate credentials on the Hub and use them elsewhere — they're standard
temporary AWS credentials.

### Getting read credentials

Load read credentials into your current shell for 30 minutes:

```bash
issue-creds --role download --lifetime 30m
```
This will output `export AWS...` commands. Copy this output to your other environment. 

`--bucket-scope` defaults to `reflective-persistent-prod`; pass it explicitly to
target a different bucket.

### Getting write credentials
Load write credentials into your current shell for 30 minutes:

```bash
issue-creds --role upload
```

This will output `export AWS_...` commands. Copy this output to your other environment.

These credentials will only be valid for the `reflective-persistent-prod` bucket. Pass it the `--bucket-scope {YOUR_BUCKET_HERE}` flag to target a different bucket.
This will also limit you to writing to your namespace in the bucket (your hub username).

### Best practices
- Copy **all three** values — access key, secret key, **and session token**
  (`AWS_SESSION_TOKEN`). Omitting the session token gives a confusing signature
  error.
- Include a region (`--region ...` on the Hub, or set `AWS_DEFAULT_REGION` on the
  target).
- Move them over a secure channel — anything holding them has your access until
  they expire.

## Roles

| role       | what you get                                              | prefix scoping                                  |
|------------|-----------------------------------------------------------|-------------------------------------------------|
| `download` | read objects + list                                       | optional `--prefix` (whole bucket if omitted)   |
| `upload`   | write + multipart + list (no read)                        | defaults to your `JUPYTERHUB_USER/` namespace; `--prefix` overrides |

Pick the **narrowest** role that does the job — it limits the damage if a
credential leaks, and it expires on its own.

## Common options

- `--lifetime` — `30m`, `1h`, `1h30m`, or seconds. Default `30m`, minimum `15m`;
  max `1h`. Please contact us if you need a lifetime longer than 1 hour.
- `--prefix lagranto/runs` — for `download`, restrict to a key prefix; for
  `upload`, write to that prefix instead of your default namespace.
- `--dry-run` — print exactly what would be requested, without calling AWS.
- `--format` — `env` (default), `profile`, `json`, or `credential-process`.


## When credentials expire

They stop working at the expiry time printed to stderr (`# expires ...`), capped
by `--lifetime`. There is **no remote refresh** — just run `issue-creds` again on
the Hub to get fresh ones. If you need longer sessions, raise `--lifetime` (up to
the configured cap).

## Handle them like secrets

These are real AWS credentials for their lifetime. Don't paste them into shared
docs, tickets, or chat; don't commit them. The `credential-process` flow above
keeps them out of your shell history entirely.

## Getting help

- **Something broke or behaved unexpectedly:** [open an issue](https://github.com/ReflectiveCloud/hub-token-vending-machine/issues) and reach out to us on the `#reflective-cloud-users` Slack channel.
- **A credential worked when it shouldn't have, or you found a security problem:**
  do **not** open a public issue — follow the [Security Policy](../SECURITY.md).
