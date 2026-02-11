# Accessing community datasets on the hub

---

See **[this google sheet](https://docs.google.com/spreadsheets/d/1cjgJQSrDV_IQVN68HoTQpy_xGQQhPy4wz1N0u8E2Pe4/edit?usp=sharing)** for the up to date list of datasets on the Cloud Hub's AWS bucket. 

See **[this google sheet](https://docs.google.com/spreadsheets/d/1gNgWTGHZ3BsKzuqri2lVTJa8JW2lFuQQwUmzLS8boG0/edit?usp=sharing)** for guidance on where to find and how to work with various recent SAI simulations (not just those on the Cloud Hub). 

---

G6-1.5K-HiLLA simulations for four models - UKESM1.1, CESM2-WACCM6, E3SMv3 and MIROC-ES2H, are stored under `s3://reflective-persistent-prod-large/<model>/<experiment>/`.


---
### Exploring the datasets

Available data can be viewed from a terminal on the cloud using commands like, e.g. 
```
aws s3 ls s3://reflective-persistent-prod-large/CESM2-WACCM6 --human-readable --recursive
```


From within a notebook, bucket contents can be listed via: 
```
import s3fs
s3 = s3fs.S3FileSystem()
s3.ls('s3://reflective-persistent-prod-large/')
```

And the code below shows one example of reading in a netcdf file stored on this bucket:
```
import xarray
import fsspec
file = 's3://reflective-persistent-prod-large/UKESM1-1/G6-1p5K-HiLLA/r2i1p1f1/pr_mon_UKESM1_u-ds275_203501-208512.nc'
with fsspec.open(example_G6HiLLA_path, mode='rb') as file:
    ds = xr.open_dataset(file, engine="h5netcdf")
```
