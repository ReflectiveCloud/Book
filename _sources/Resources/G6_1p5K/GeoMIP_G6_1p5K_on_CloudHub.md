# G6-1.5K-SAI/HiLLA on the Cloud Hub

The example notebook in this repo demonstrates working with the archive of GeoMIP G6-1.5K-SAI and G6-1.5K-HiLLA (MCB coming soon..) data on the Reflective Cloud Hub's AWS archive, to produce a summary plot of the injection magnitudes and temperature reponse across models and scenarios for these recent simulations. 

The code here is only part of the workflow -- there is also a regridding step for E3SM data. The full code is on GitHub [here](https://github.com/ReflectiveCloud/GeoMIP_G6-1.5K_cloud_data) and on the Reflective Cloud hub under /shared/Code_examples/G6-1.5K_example/. 

Data from G6-1.5K- simulations for four models - UKESM1.1, CESM2-WACCM6, E3SMv3 and MIROC-ES2H, are freely available on the [Reflective Cloud Hub](https://reflectivecloud.github.io/Book/intro.html), stored on a private S3 bucket accessible from within the hub, under s3://reflective-persistent-prod-large/

See [Lee et al. (2026)](https://doi.org/10.5194/egusphere-2025-5742) for an overview of the G6-1.5K-SAI simulations, and [Visioni et al. (2024)](https://journals.ametsoc.org/view/journals/bams/105/12/BAMS-D-24-0274.1.xml) for a description of the protocol. The G6-1.5K-HiLLA protocol is discussed in [Visioni et al., (2025)](https://doi.org/10.1175/BAMS-D-25-0191.1) and testbed simulation results are presented in [Duffey et al. (preprint)](https://doi.org/10.5194/egusphere-2025-5356). 


<img width="1000" alt="G6_SAIandHiLLA_overview_all" src="https://github.com/user-attachments/assets/d245c80e-965e-495e-a8e8-7f558b505cb8" />


