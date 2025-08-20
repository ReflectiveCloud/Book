# An Archive of Pre-processed SAI Simulations

---

## Overview

This archive processes common SAI simulations into a small (~1GB), user-friendly, analysis-ready format. It includes a usage example notebook showing how to derive common analyses of SAI scenarios.

---

## Input Data

### **ARISE-1.5K Simulations**

- UKESM1 and CESM2-WACCM

### **G6sulfur Simulations** (6 models)

- UKESM1, CESM2-WACCM, IPSL-CM6A
- MPI-ESM1-2 (High and low resolution)
- CNRM-ESM2

### **Background/Control Runs**

- **ARISE**: SSP2-4.5 run (and end of historical for UKESM1)
- **G6sulfur**: SSP5-8.5 run (background) and SSP2-4.5 run (baseline/target)

---

## Variable Selection

We prioritize variables based on:

1. **Baseline Climate Variables** defined by [Juckes et al. (2024)](https://egusphere.copernicus.org/preprints/2024/egusphere-2024-2363/)
2. **Community download rates** from [ESGF dashboard](http://esgf-ui.cmcc.it/esgf-dashboard-ui/cmip6.html)

---

## Outputs

- **Maps**: Time-means and standard deviations
- **Time-series**: Global, land and ocean means

---

## Getting Started

### **1. Download Data**

Get the archive from: [https://zenodo.org/records/14802397](https://zenodo.org/records/14802397)

### **2. Setup**

- Unzip the archive
- Place in a folder named `pp_archive/` in your working directory

### **3. Run Example**

Use the notebook: `pp_archive_usage_example.ipynb`

---

## Code Repository

The code to create this archive is available on GitHub: [https://github.com/alistairduffey/SRM_nutshell](https://github.com/alistairduffey/SRM_nutshell)

---

## Data Structure

_[Data structure details to be added]_
