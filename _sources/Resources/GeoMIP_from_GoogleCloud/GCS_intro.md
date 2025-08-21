# GeoMIP Analysis Using the CMIP6 Google cloud Store 

---

## Overview

This section contains a **Jupyter notebook** demonstrating how to work with GeoMIP (G6sulfur) and CMIP (e.g. ScenarioMIP SSP2-4.5 and SSP5-8.5 simulations) data which is **[stored on the Google Cloud](https://console.cloud.google.com/marketplace/product/noaa-public/cmip6?rapt=AEjHL4P5UmZK8PvWY86y3IVR4jbCaOBt6fL1U86KV1E0Pz3TE9DXxLVVRSrn811LeVovU5CcTJ3eWcOvtRgD9_7ozLTANjQ63q6DP2X48cmxyHXYb-aEjo0)** in a cloud-optimised, **zarr**, form. The CMIP6 archive was produced as part of the **[LEAP project](https://catalog.leap.columbia.edu/feedstock/cmip6)**. In August 2025, Reflective organised the addition of G6sulfur data from all 6 participating models, for a set of around 1000 commonly used outputs. This resource demonstrates usage of the store, which supports fast and user-friendly cloud-based workflows. 

---
## Acknowledgements
We thank Julius Busecke for his work ingesting the GeoMIP data, and the LEAP project for providing computing resources. 

---

## Notebook Location

The notebooks shown here is also stored under `/shared/Code_examples` on the Cloud Hub. 

---

## Notebooks

### **1. Data Access and a plotting example**

**[G6sulfur_from_cloud_demo.ipynb](G6sulfur_from_cloud_demo.ipynb)**

This notebook demonstrates how to read in data using the **intake-esgf package**, and as an example, recreates figure 1 from **[Visioni et al., 2021](https://acp.copernicus.org/articles/21/10039/2021/acp-21-10039-2021.html)**.

**What you'll learn:**

- Searching for GeoMIP data on the CMIP6 GCS store
- Working with zarr stores via xarray and intake-esm
- Iterating over datasets to quickly reproduce common analyses

## Key Benefits

### **Direct Data Access**

- **No pre-downloading required** - Access data directly from the zarr store
- **Real-time data discovery** - Search and find datasets as needed
- **Lazy loading** - Download only the part of the data you need, only when you need it

### **Reproducible Research**

- **Version control** - Track exactly which data versions you used
- **Portable code** - Share notebooks that work anywhere with ESGF access

---

## Additional Resources

- **[intake-esm Documentation](https://intake-esm.readthedocs.io/en/stable/index.html)** - Comprehensive guide to the package
- **[Google cloud data store](https://console.cloud.google.com/marketplace/product/noaa-public/cmip6?rapt=AEjHL4P5UmZK8PvWY86y3IVR4jbCaOBt6fL1U86KV1E0Pz3TE9DXxLVVRSrn811LeVovU5CcTJ3eWcOvtRgD9_7ozLTANjQ63q6DP2X48cmxyHXYb-aEjo0)** - Web-portal to see stored data (not recommended for finding what is available as it is not easily navigated)
- **[GeoMIP Project](https://climate.envsci.rutgers.edu/geomip/)** - Official GeoMIP information
- **[Pangeo documentation](https://climate-datalab.org/cmip6-walkthrough/)** - Lots of helpful information, with further code examples for working with zarr stores and the google cloud. 

---
