#!/bin/bash

wget ftp://ftp.gfdl.noaa.gov/perm/Alistair.Adcroft/MOM6-testing/OM4_025/ocean_static.nc

basins.py ocean_static.nc
