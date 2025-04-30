### An archive of pre-processed SAI simulations

This repository contains code to post-process common SAI simulations into a small (~1GB), user-friendly, archive of data in an analysis-ready format. It also has a usage example notebook, showing how to use this pre-procesed archive to derive some common analyses of SAI scenarios. 


Code to make the archive is stored  here: https://github.com/alistairduffey/SAI_pp_archive/tree/main
 

Inputs:
* ARISE-1.5K simulations (UKESM1 and CESM2-WACCM)
* G6sulfur simulations for 6 models: UKESM1, CESM2-WACCM, IPSL-CM6A, MPI-ESM1-2 (High and low resolution), CESM2-WACCM, and CNRM-ESM2

For each SAI simulation, background/control runs are also used. For ARISE, this is the SSP2-4.5 run (and the end of the historical run for UKESM1). For G6sulfur, this is both the SSP5-8.5 run (the 'background') and the SSP2-4.5 run (the 'baseline' and 'target').

We calculate outputs for a limited a set of variables. We have prioritised these variables following the list of Baseline Climate Variables defined by Juckes et al.  (https://egusphere.copernicus.org/preprints/2024/egusphere-2024-2363/), and within this, by the rate of download by the community (as shown here http://esgf-ui.cmcc.it/esgf-dashboard-ui/cmip6.html). 

Outputs:
* Maps of time-means and standard deviations
* Time-series of global, land and ocean means


To run the code in Usage_example/, first download the data archive from zenodo (https://zenodo.org/records/14802397), then place this unzipped archive in a folder 'pp_archive/' at the root of this project directory.  



#### A note on calendars
UKESM uses a 360 day calendar, so there is no need to apply month weights when calculating annual means. For CESM2 and others, we do need to do this, hence the additional step in meaning in these scripts, using month weighting functions (in utils.py).

#### Variables

For UKESM1, the following variables are included:

Variables used are as follows:

| Label          | Realm       | Title                                                    | Units       | Standard Name                                     |
|----------------|-------------|----------------------------------------------------------|-------------|---------------------------------------------------|
| Amon.prw       | Atmosphere  | Water Vapor Path                                         | kg m-2      | atmosphere_mass_content_of_water_vapor            |
| Amon.evspsbl   | Land        | Evaporation Including Sublimation and Transpiration      | kg m-2 s-1  | water_evapotranspiration_flux                     |
| Amon.clivi     | Atmosphere  | Ice Water Path                                           | kg m-2      | atmosphere_mass_content_of_cloud_ice              |
| Amon.clt       | Atmosphere  | Total Cloud Cover Percentage                             | %           | cloud_area_fraction                               |
| Amon.clwvi     | Atmosphere  | Condensed Water Path                                     | kg m-2      | atmosphere_mass_content_of_cloud_condensed_water  |
| Amon.hfss      | Surface     | Surface Upward Sensible Heat Flux                        | W m-2       | surface_upward_sensible_heat_flux                 |
| Amon.rlds      | Radiation   | Surface Downwelling Longwave Radiation                   | W m-2       | surface_downwelling_longwave_flux_in_air          |
| Amon.rldscs    | Radiation   | Surface Downwelling Clear-Sky Longwave Radiation         | W m-2       | surface_downwelling_longwave_flux_in_air_assuming_clear_sky |
| Amon.rlus      | Radiation   | Surface Upwelling Longwave Radiation                     | W m-2       | surface_upwelling_longwave_flux_in_air            |
| Amon.rlut      | Radiation   | TOA Outgoing Longwave Radiation                          | W m-2       | toa_outgoing_longwave_flux                        |
| Amon.rlutcs    | Radiation   | TOA Outgoing Clear-Sky Longwave Radiation                | W m-2       | toa_outgoing_longwave_flux_assuming_clear_sky     |
| Amon.rsds      | Radiation   | Surface Downwelling Shortwave Radiation                  | W m-2       | surface_downwelling_shortwave_flux_in_air         |
| Amon.rsdscs    | Radiation   | Surface Downwelling Clear-Sky Shortwave Radiation        | W m-2       | surface_downwelling_shortwave_flux_in_air_assuming_clear_sky |
| Amon.rsdt      | Radiation   | TOA Incident Shortwave Radiation                         | W m-2       | toa_incoming_shortwave_flux                       |
| Amon.rsus      | Radiation   | Surface Upwelling Shortwave Radiation                    | W m-2       | surface_upwelling_shortwave_flux_in_air           |
| Amon.rsuscs    | Radiation   | Surface Upwelling Clear-Sky Shortwave Radiation          | W m-2       | surface_upwelling_shortwave_flux_in_air_assuming_clear_sky |
| Amon.rsut      | Radiation   | TOA Outgoing Shortwave Radiation                         | W m-2       | toa_outgoing_shortwave_flux                       |
| Amon.rsutcs    | Radiation   | TOA Outgoing Clear-Sky Shortwave Radiation               | W m-2       | toa_outgoing_shortwave_flux_assuming_clear_sky    |
| Amon.pr        | Surface     | Precipitation                                            | kg m-2 s-1  | precipitation_flux                                |
| Amon.tas       | Surface     | Near-Surface Air Temperature                             | K           | air_temperature                                   |
| Amon.uas       | Surface     | Eastward Near-Surface Wind                               | m s-1       | eastward_wind                                     |
| Amon.vas       | Surface     | Northward Near-Surface Wind                              | m s-1       | northward_wind                                    |
| Amon.hfls      | Surface     | Surface Upward Latent Heat Flux                          | W m-2       | surface_upward_latent_heat_flux                   |
| Amon.hurs      | Surface     | Near-Surface Relative Humidity                           | %           | relative_humidity                                 |
| Amon.huss      | Surface     | Near-Surface Specific Humidity                           | 1           | specific_humidity                                 |
| Amon.prc       | Surface     | Convective Precipitation                                 | kg m-2 s-1  | convective_precipitation_flux                     |
| Amon.prsn      | Surface     | Snowfall Flux                                           | kg m-2 s-1  | snowfall_flux                                     |
| Amon.ps        | Surface     | Surface Air Pressure                                    | Pa          | surface_air_pressure                              |
| Amon.psl       | Surface     | Sea Level Pressure                                      | Pa          | air_pressure_at_mean_sea_level                    |
| Amon.sfcWind   | Surface     | Near-Surface Wind Speed                                 | m s-1       | wind_speed                                        |
| Amon.tasmax    | Surface     | Daily Maximum Near-Surface Air Temperature              | K           | air_temperature                                   |
| Amon.tasmin    | Surface     | Daily Minimum Near-Surface Air Temperature              | K           | air_temperature                                   |
| Amon.tauu      | Surface     | Surface Downward Eastward Wind Stress                   | Pa          | surface_downward_eastward_stress                  |
| Amon.tauv      | Surface     | Surface Downward Northward Wind Stress                  | Pa          | surface_downward_northward_stress                 |
| Amon.ts        | Surface     | Surface Temperature                                     | K           | surface_temperature                               |
| Lmon.evspsblsoi| Land        | Water Evaporation from Soil                             | kg m-2 s-1  | water_evaporation_flux_from_soil                  |
| Lmon.lai       | Land        | Leaf Area Index                                         | 1           | leaf_area_index                                   |
| Lmon.mrfso     | Land        | Soil Frozen Water Content                               | kg m-2      | soil_frozen_water_content                         |
| Lmon.mrro      | Land        | Total Runoff                                            | kg m-2 s-1  | runoff_flux                                       |
| Lmon.mrros     | Land        | Surface Runoff                                          | kg m-2 s-1  | surface_runoff_flux                               |
| Lmon.mrso      | Land        | Total Soil Moisture Content                             | kg m-2      | mass_content_of_water_in_soil                     |
| Lmon.mrsos     | Land        | Moisture in Upper Portion of Soil Column                | kg m-2      | mass_content_of_water_in_soil_layer               |
| Omon.hfds      | Ocean       | Downward Heat Flux at Sea Water Surface                 | W m-2       | surface_downward_heat_flux_in_sea_water           |
| Omon.mlotst    | Ocean       | Ocean Mixed Layer Thickness Defined by Sigma T          | m           | ocean_mixed_layer_thickness_defined_by_sigma_t    |
| Omon.sos       | Ocean       | Sea Surface Salinity                                    | 0.001       | sea_surface_salinity                              |
| Omon.tauuo     | Ocean       | Sea Water Surface Downward X Stress                     | N m-2       | downward_x_stress_at_sea_water_surface            |
| Omon.tauvo     | Ocean       | Sea Water Surface Downward Y Stress                     | N m-2       | downward_y_stress_at_sea_water_surface            |
| Omon.tos       | Ocean       | Sea Surface Temperature                                 | degC        | sea_surface_temperature                           |
| Omon.zos       | Ocean       | Sea Surface Height Above Geoid                          | m           | sea_surface_height_above_geoid                    |


For CESM2-WACCM ARISE simualtions, a shorter subset variables is included (the 10 most downloaded variables from the ESGF store):

| Label          | Realm       | Title                                                    | Units       | Standard Name                                     |
|----------------|-------------|----------------------------------------------------------|-------------|---------------------------------------------------|
| Amon.evspsbl   | Land        | Evaporation Including Sublimation and Transpiration      | kg m-2 s-1  | water_evapotranspiration_flux                     |
| Amon.rsds      | Radiation   | Surface Downwelling Shortwave Radiation                  | W m-2       | surface_downwelling_shortwave_flux_in_air         |
| Amon.pr        | Surface     | Precipitation                                            | kg m-2 s-1  | precipitation_flux                                |
| Amon.hurs      | Surface     | Near-Surface Relative Humidity                           | %           | relative_humidity                                 |
| Amon.psl       | Surface     | Sea Level Pressure                                      | Pa          | air_pressure_at_mean_sea_level                    |
| Amon.tasmax    | Surface     | Daily Maximum Near-Surface Air Temperature              | K           | air_temperature                                   |
| Amon.tasmin    | Surface     | Daily Minimum Near-Surface Air Temperature              | K           | air_temperature                                   |
| Amon.ts        | Surface     | Surface Temperature                                     | K           | surface_temperature                               |
| Amon.tas       | Surface     | Near-Surface Air Temperature                             | K           | air_temperature                                   |
| SImon.siconca  | Sea ice     | Sea-ice area percentage (atmospheric grid)               | %           | sea_ice_area_fraction                              |

For the G6sulfur simulations, variables from the list above are included depending on availability on the CEDA ESGF data node. 

