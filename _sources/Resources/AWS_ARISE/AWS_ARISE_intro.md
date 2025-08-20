# Using the AWS ARISE-SAI-1.5 Simulations Cloud Archive

---

## Overview

This repository contains **Python notebooks** demonstrating simple usage examples of the AWS ARISE-SAI-1.5k simulations cloud archive.

---

## Repository Information

- **GitHub Repository**: [https://github.com/alistairduffey/AWS_ARISE](https://github.com/alistairduffey/AWS_ARISE)
- **Data Source**: [NCAR CESM2 ARISE on AWS Open Data Registry](https://registry.opendata.aws/ncar-cesm2-arise/)

---

## About ARISE-SAI-1.5k Simulations

The **ARISE-SAI-1.5k simulations** (Richter et al., 2022) are available on Amazon Web Services (AWS). These simulations are part of the [CESM Community Projects](https://www.cesm.ucar.edu/community-projects/arise-sai) and provide valuable data for Solar Radiation Management research.

---

## Available Notebooks

### **1. Basic Example**

**[AWS_ARISE_basic_example.ipynb](AWS_ARISE_basic_example.ipynb)**

Shows how to use the **S3 file system** to read in the data and perform basic analysis tasks.

**What you'll learn:**

- Accessing data from AWS S3
- Basic data reading and manipulation
- Simple analysis workflows

### **2. Kerchunk Example**

**[kerchunk_example/AWS_ARISE_kerchunk_test.ipynb](kerchunk_example/AWS_ARISE_kerchunk_test.ipynb)**

Demonstrates how to use the **[kerchunk package](https://guide.cloudnativegeo.org/kerchunk/intro.html)** to save metadata and create virtual zarr files, significantly speeding up read-in and processing steps for ARISE simulation analysis.

**What you'll learn:**

- Using kerchunk for metadata management
- Creating virtual zarr files
- Optimizing data access and processing
- Advanced analysis workflows

---

## Use Cases

These notebooks are designed for researchers who want to:

- **Access ARISE-SAI-1.5k simulations** from AWS cloud storage
- **Learn cloud-native data analysis** techniques
- **Optimize data processing** workflows using kerchunk
- **Perform reproducible research** with cloud-based climate data

---

## Getting Started

1. **Clone the repository**: `git clone https://github.com/alistairduffey/AWS_ARISE`
2. **Choose your notebook**: Start with the basic example for fundamental concepts
3. **Explore kerchunk**: Move to the advanced example for optimization techniques
4. **Adapt for your research**: Modify the examples for your specific analysis needs

---

## Additional Resources

- **[Kerchunk Documentation](https://guide.cloudnativegeo.org/kerchunk/intro.html)** - Comprehensive guide to the kerchunk package
- **[AWS Open Data Registry](https://registry.opendata.aws/)** - Discover more open datasets
- **[CESM Community Projects](https://www.cesm.ucar.edu/community-projects)** - Explore other climate modeling initiatives

---
