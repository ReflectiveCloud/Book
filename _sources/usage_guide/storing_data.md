# Storing files

There are two types of storage on the cloud hub:

* user directories, under /home, for notebooks, scripts and very small data files

* shared cloud buckets - storage on our S3 buckets associated with the hub

  

### User Directories

You can navigate this storage like a normal file browser when you open the hub. They behave as a normal UNIX file system. From a terminal on the hub, directories can be navigated and moved around as on a local machine:

  

### Cloud buckets

For medium-sized data used as part of ongoing projects, two S3 buckets can be used:

  

* The scratch bucket at `s3://reflective-scratch-prod/<username>`, (also saved in the convenience variable `$SCRATCH_BUCKET`)

* The persistent bucket, at `s3://reflective-persistent-prod/<username>`, (also saved in the convenience variable `$PERSISTENT_BUCKET`)

  

Data saved in the scratch bucket is **deleted every 7 days**, so the scratch bucket should be used only for intermediate data produced temporarily during analysis, or as a staging location.

  

Data produced as part of analyses and in active use, or data which you need to upload for use in a project should typically be stored in the persistent bucket.

  

Please only ever write to the folder under your own username on the persistent bucket, except if agreed beforehand with Reflective, as will be the case for some community datasets which we want to store in a more visible location.

  

The environment variables `SCRATCH_BUCKET` and `PERSISTENT_BUCKET` come preloaded with your username, e.g. s3://reflective-persistent-prod/alistairduffey for AD. This is on purpose to track file ownership and prevent overwriting of other users' data. Using these environment variables rather hard coded file paths is therefore preferable for safety!

  

#### Do not put ever sensitive data (e.g. passwords) on the hub!

* Data under user directories can be accessed by hub admins.

* Data on cloud buckets is freely accessible by any user of the hub.

  
  

### Example - writing a netcdf file to the scratch bucket

The code below shows an example of writing a netcdf file from the hub. It uses two steps as netcdf files (unlike zarr) can't be written directly onto an S3 bucket.

For more examples and information, see [2i2c docs here](https://docs.2i2c.org/user/data/object-storage/working-with-object-storage/), and the [NASA Earthdata Cloud Cookbook](https://nasa-openscapes.github.io/earthdata-cloud-cookbook/how-tos/using-s3-storage.html) and [CryoCloud docs](https://2i2c.org/cryocloud-myst/cryocloudscratchbucket).



```

s3 = s3fs.S3FileSystem()

scratch = os.environ['SCRATCH_BUCKET']

out_path_on_scratch = f"{scratch}/test_loc.nc" # Where we want to store it

  

# Create a temporary intermediate netcdf on user directory, then move it to the bucket

with tempfile.NamedTemporaryFile(suffix = ".nc") as tmp:

ds.to_netcdf(tmp.name) # save to a temporary file

s3.put(tmp.name, out_path_on_scratch) # move that file to the scratch bucket

```
