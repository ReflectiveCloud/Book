# Using the AWS ARISE-SAI-1.5 simulations cloud archive 

example notebooks

See github repo here https://github.com/alistairduffey/AWS_ARISE

The ARISE-SAI-1.5k simulations (Richter et al., 2022; https://www.cesm.ucar.edu/community-projects/arise-sai) are available on Amazon Web Services (AWS), here: https://registry.opendata.aws/ncar-cesm2-arise/

This repo contains python notebooks showing simple usage examples of this cloud archive. 


## Two notebooks: 

#### (1) AWS_ARISE_basic_example.ipynb 
Shows how to use the S3 file system to read in the data and do some basic analysis.

#### (2) kerchunk_example/AWS_ARISE_kerchunk_test.ipynb
Shows how to use the kerchunk package (https://guide.cloudnativegeo.org/kerchunk/intro.html) to save metadata (creating a virtual zarr file) to speed up the read-in and processing steps for some analysis of the ARISE simulations. 




