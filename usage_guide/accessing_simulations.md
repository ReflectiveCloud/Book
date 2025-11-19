# Accessing community datasets on the hub

[this guide is in development.  more info - and more data - is coming soon]

G6-1.5K-HiLLA simulations for three models - UKESM1.1, CESM2-WACCM6 and E3SMv3 - are stored under `s3://reflective-persistent-prod-large/<model>/<experiment>/<ensemble_member>/<table>/`.

These data can be viewed from a terminal on the cloud using commands like, e.g. 
```
aws s3 ls s3://reflective-persistent-prod-large/CESM2-WACCM6 --human-readable --recursive
```

From within a notebook, bucket contents can be listed via: 
```
import s3fs
s3 = s3fs.S3FileSystem()
s3.ls('s3://reflective-persistent-prod-large/')
```

And te code below shows one example of reading in a netcdf file stored on this bucket:
```
import xarray
import fsspec
file = 's3://reflective-persistent-prod-large/UKESM1-1/G6-1p5K-HiLLA/r2i1p1f1/pr_mon_UKESM1_u-ds275_203501-208512.nc'
with fsspec.open(example_G6HiLLA_path, mode='rb') as file:
    ds = xr.open_dataset(file, engine="h5netcdf")
```
