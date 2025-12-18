#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:48:34 2024

@author: nbodini
"""
import xarray as xr

# Open NetCDF files
ds_A1 = xr.open_dataset('A1_sonic.nc')
ds_A2 = xr.open_dataset('A2_sonic.nc')
ds_A5 = xr.open_dataset('A5_sonic.nc')

# Accessing data variables
print("Data variables available:")
print(ds_A1.data_vars)

# Accessing coordinates
print("\nCoordinates available:")
print(ds_A1.coords)

# Accessing a specific variable
wind_speed_A1 = ds_A1['WS']
print("\nWind speed data in A1:")
print(wind_speed_A1)

# Accessing a specific time slice
time_slice = slice('2023-08-24T01:00:00', '2023-08-24T02:00:00')
wind_speed_A1_slice = wind_speed_A1.sel(time=time_slice)
print("\nWind speed data in A1 for the time slice:")
print(wind_speed_A1_slice)

