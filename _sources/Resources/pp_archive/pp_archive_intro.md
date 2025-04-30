# An archive of pre-processed SAI simulations

process common SAI simulations into a small (~1GB), user-friendly, archive of data in an analysis-ready format. It also has a usage example notebook, showing how to use this pre-procesed archive to derive some common analyses of SAI scenarios. 


Inputs:
* ARISE-1.5K simulations (UKESM1 and CESM2-WACCM)
* G6sulfur simulations for 6 models: UKESM1, CESM2-WACCM, IPSL-CM6A, MPI-ESM1-2 (High and low resolution), CESM2-WACCM, and CNRM-ESM2

For each SAI simulation, background/control runs are also used. For ARISE, this is the SSP2-4.5 run (and the end of the historical run for UKESM1). For G6sulfur, this is both the SSP5-8.5 run (the 'background') and the SSP2-4.5 run (the 'baseline' and 'target').
We calculate outputs for a limited a set of variables. We have prioritised these variables following the list of Baseline Climate Variables defined by Juckes et al.  (https://egusphere.copernicus.org/preprints/2024/egusphere-2024-2363/), and within this, by the rate of download by the community (as shown here http://esgf-ui.cmcc.it/esgf-dashboard-ui/cmip6.html). 

Outputs:
* Maps of time-means and standard deviations
* Time-series of global, land and ocean means


To run the code in pp_archive_usage_example.ipynb, first download the data archive from zenodo, then place the unzipped archive in a folder 'pp_archive/' in your working directory.  


To download the data, go to https://zenodo.org/records/14802397
The code to make the archive is on Github here https://github.com/alistairduffey/SRM_nutshell


## Data structure


