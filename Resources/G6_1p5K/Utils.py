import os
import glob
import pandas as pd
import numpy as np
import xarray as xr
import cftime
from Config import lat_band_dict

# note, in general we have to account for different month lengths
def weighted_annual_resample(ds, var):
    """
    weight by days in each month
    adapted from NCAR docs 
    https://ncar.github.io/esds/posts/2021/yearly-averages-xarray/
    """
    # Determine the month length
    month_length = ds.time.dt.days_in_month

    # Calculate the weights
    wgts = (month_length.groupby("time.year") / month_length.groupby("time.year").sum()).load()

    # Make sure the weights in each year add up to 1
    np.testing.assert_allclose(wgts.groupby("time.year").sum(xr.ALL_DIMS), 1.0)

    numerator = (ds[var] * wgts).resample(time="YS").sum(dim="time")
    denominator = wgts.resample(time="YS").sum(dim="time")
    ds_out = (numerator/denominator).to_dataset(name=var)
    ds_out['year'] = ds_out.time.dt.year
    return ds_out


def spatial_mean(ds, region, zonal_mean=False, var='tas',
                lat_name='latitude', lon_name='longitude'):
    ds = ds.rename({lat_name:'latitude', lon_name:'longitude'})
    ds_ts = ds.sel(latitude=slice(lat_band_dict[region][0], lat_band_dict[region][1]))[var]
    if not zonal_mean:
        ds_ts = ds_ts.mean(dim=['longitude'])
    weights = np.cos(np.deg2rad(ds_ts['latitude']))
    ds_ts_w = ds_ts.weighted(weights)
    ds_ts = ds_ts_w.mean(dim='latitude')
    return ds_ts.to_dataset(name=var)

def set_time_to_center_of_bounds(ds, time_bounds_name='time_bounds'):
    time_bounds = ds[time_bounds_name]
    time_midpoints = time_bounds.mean(dim=time_bounds.dims[-1])
    new_ds = ds.assign_coords(time=time_midpoints)
    return new_ds


