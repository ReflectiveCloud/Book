# Storing and uploading data

There are two types of storage on the cloud hub:

* user directories, under /home, for notebooks, scripts and very small data files

* shared cloud buckets - storage on our S3 buckets associated with the hub

  

### User Directories

You can navigate this storage like a normal file browser when you open the hub. They behave as a normal UNIX file system. From a terminal on the hub, directories can be navigated and moved around as on a local machine. 

Note that you have only 10 GB of /home directory storage. This is set low because all larger data should be written to S3 buckets, as described below. The directory storage should only be used for code, figures, and small files. 

  

### Cloud buckets

For medium-sized data used as part of ongoing projects, two S3 buckets can be used:

  

* The scratch bucket at `s3://reflective-scratch-prod/<username>`, (also saved in the convenience variable `$SCRATCH_BUCKET`)

* The persistent bucket, at `s3://reflective-persistent-prod/<username>`, (also saved in the convenience variable `$PERSISTENT_BUCKET`)

  

Data saved in the scratch bucket is **deleted every 7 days**, so the scratch bucket should be used only for intermediate data produced temporarily during analysis, or as a staging location.

  

Data produced as part of analyses and in active use, or data which you need to upload for use in a project should typically be stored in the persistent bucket.

  

Please only ever write to the folder under your own username on the persistent bucket, except if agreed beforehand with Reflective, as will be the case for some community datasets which we want to store in a more visible location.

  

The environment variables `SCRATCH_BUCKET` and `PERSISTENT_BUCKET` come preloaded with your username, e.g. s3://reflective-persistent-prod/alistairduffey. This is on purpose to track file ownership and prevent overwriting of other users' data. Using these environment variables rather than hard coded file paths is therefore preferable for safety!

  

#### Do not put ever sensitive data (e.g. passwords) on the hub!

* Data under user directories can be accessed by hub admins.

* Data on S3 buckets is freely accessible by any user of the hub, even if under your username.

  
  
### Uploading data to the hub

- for **small-to-medium** files, you can upload in the jupyterlab interface (via the GUI), or run wget scripts on the hub to download from the web, and then move files to buckets using ``` aws s3 mv <source> <destination>``` or via the python commands below.
- for **larger** datasets (>10s GB), you will need to make credentials on the hub via the issue-creds tool, see [here](https://reflectivecloud.github.io/Book/usage_guide/credentials_tool.html), which allows for comand line uploading.


### Our policy for community dataset uploads

We encourage users to add datasets that will be useful to other members of the research community.

- **Data produced as part of an ongoing project:** write to the scratch or persistent bucket under your own username directory, as described above.
- **Completed datasets smaller than 100 GB:** any dataset of relevance to the solar radiation management (SRM) research community is welcome. We ask that you provide basic information about the dataset so we can keep track of the available data.
- **Datasets larger than 100 GB:** Reflective will decide case-by-case whether to store the data. Decisions are based on the dataset's expected scientific impact and alignment with Reflective's ethos of transparent, reproducible SRM research. Ongoing cloud storage is relatively costly, so we are unlikely to store datasets larger than ~1 TB without a compelling case for widespread use (e.g. new GeoMIP experiments).

**Please fill out [this form](https://tally.so/r/0QYea0) before uploading so we can track what is on the Hub and make others aware of available data**

Where possible, we encourage depositing datasets in a dedicated archive such as Zenodo to generate a permanent, DOI'd version, in addition to Reflective Cloud storage. The purpose of our storage is to make data easy to access on the cloud, not to act as an authoritative data publisher.

We intend to maintain hosted data for a minimum of 3 years, and will notify users 6 months in advance of any dataset removal. This is not a permanent archive: Reflective makes no commitment to longer-term access, public access, or data back-up.



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
