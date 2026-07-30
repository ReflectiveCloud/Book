# Choosing environments

When you start the Cloud Hub, a choice of different images is offered as a drop-down menu. We maintain a "Reflective" image, which contains many common packages used for earth science (xarray, pangeo stack etc.), as well as some additions for working in the Cloud (e.g. arrraylake for working with zarr stores on Earthmover). This environment develops over time, so it's possible that you will come back to old code and find it needs an old version of the environment to run. This is possible (see below). There are also several default images available: the "Pangeo" environment is a safe choice if you just want the geospatial stack, and "Scipy" is a more bare-bones environment. 

Note that you can always temporarily install (or update) packages during a session using `pip install`.   


## Using Custom Images On the Hub

Sometimes you may need to use a previous version of our environment due to updates to packages that may have broken your workflow. If you run into any unexpected issues with code that was previously working on the hub, you can use the previous environment. When starting the Hub, click the "Environment" drop down and scroll to the bottom. Click on "Bring your own image". Then enter quay.io/2i2c/reflective-image:{IMAGE_TAG}. Grab the `{IMAGE_TAG}` from the table of images below. Make sure to that http:// isn't included with the URL if you copy and paste it. If it is, just remove it. Start the hub, and you will be using the version of the image that you specify.

## Reflective Image Tag History
Each tag is a git commit SHA from [reflective-org/reflective-image](https://github.com/reflective-org/reflective-image). Dates are the source commit dates; newest first.
| Tag | Usable | Published | Size | Changes vs. previous image |
|---|---|---|---|---|
| `52b0ccfd1fca` | :white_check_mark: | Jul 30, 2026 | 2.7 GiB | Pinned `pyopenssl >= 24` to fix issues connecting to aws S3 buckets; `added and pinned arraylake==1.2.0`; ([#6](https://github.com/reflective-org/reflective-image/commit/52b0ccfd1fca1b584656ae15f14472bad7330222)) | 
| `5ba270bf5081` | :x: | Jul 23, 2026 | 2.7 GiB | Added `.gitignore`; pinned upgrades beyond pangeo-notebook base: `xarray==2026.7.0`, `zarr==3.2.1`, `icechunk==2.1.1`; added `issue-creds` (credential issuing) ([#5](https://github.com/reflective-org/reflective-image/commit/5ba270bf5081)) |
| `5cb60c85bbb0` | :white_check_mark: | Mar 13, 2026 | 3.0 GiB | s3fs fix: aligned S3 stack via pip (`s3fs`, `fsspec`, `boto3`, `botocore`); added `cdo` and `nco` ([#4](https://github.com/reflective-org/reflective-image/commit/5cb60c85bbb0)) |
| `31aa6abf39c9` | :white_check_mark: | Feb 24, 2026 | 2.8 GiB | AI integration fix: `postBuild` now actually runs during image build, so VS Code extensions are truly installed (previous tag only echoed the install command); installs run as notebook user with `--force` ([#3](https://github.com/reflective-org/reflective-image/commit/31aa6abf39c9)) |
| `5757ed417852` |  :x: |Feb 24, 2026 | 2.4 GiB | Added AI tooling: `jupyter-ai[all]` via pip; added `openai.chatgpt` and `anthropic.claude-code` VS Code extensions to install list ([#2](https://github.com/reflective-org/reflective-image/commit/5757ed417852)) |
| `7bb4358204a5` |  :x: |Jan 30, 2026 | 1.9 GiB | Added VS Code support: `code-server>=4.0`, `jupyter-vscode-proxy`, `jupyter-server-proxy`; new `postBuild` (ms-python, svelte extensions — echo only, not installed) and `start` script setting `VSCODE_PROXY_URI` ([#1](https://github.com/reflective-org/reflective-image/commit/7bb4358204a5)) |
| `bafdf91292d2` | :white_check_mark: | Oct 8, 2025 | 1.8 GiB | Removed version pins in `environment.yml`: `jupyterhub-singleuser` and `nbgitpuller` now unpinned ([commit](https://github.com/reflective-org/reflective-image/commit/bafdf91292d2)) |
| `31d6a9045cb1` | :white_check_mark: | Oct 8, 2025 | 1.9 GiB | Removed `image-tests` copy from `Dockerfile`; oldest tag still in the registry ([commit](https://github.com/reflective-org/reflective-image/commit/31d6a9045cb1)) |

