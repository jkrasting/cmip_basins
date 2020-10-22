import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
from cmip_basins.basins import generate_basin_codes
import cmip_basins.gfdl as gfdl
import cmip_basins.cmip6 as cmip6


# define 1x1 grid
lon = np.arange(0.5, 360.5)
lat = np.arange(89.5, -90.5, -1)
grid = xr.Dataset()
grid["lon"] = xr.DataArray(lon, dims=("lon"))
grid["lat"] = xr.DataArray(lat, dims=("lat"))

# make plot CMIP6 codes
plt.figure()
ax = plt.subplot(111, projection=ccrs.PlateCarree())
cmip6.dbasins.plot_regions(ax=ax, add_label=False, line_kws=dict(color="r"))
ax.coastlines(resolution='50m')
plt.title('polygons cmip6')

codes = generate_basin_codes(grid, lon="lon", lat="lat",
                             persian=True, style='cmip6')

plt.figure()
ax = plt.subplot(111, projection=ccrs.PlateCarree())
codes.plot(ax=ax, x="lon", y="lat", cmap="tab20")
ax.coastlines(resolution='50m')
plt.title('basin codes cmip6')

# make plot GFDL codes
plt.figure()
ax = plt.subplot(111, projection=ccrs.PlateCarree())
gfdl.dbasins.plot_regions(ax=ax, add_label=False, line_kws=dict(color="r"))
ax.coastlines(resolution='50m')
plt.title('polygons gfdl')

codes = generate_basin_codes(grid, lon="lon", lat="lat",
                             persian=True, style='gfdl')

plt.figure()
ax = plt.subplot(111, projection=ccrs.PlateCarree())
codes.plot(ax=ax, x="lon", y="lat", cmap="tab20")
ax.coastlines(resolution='50m')
plt.title('basin codes gfdl')

plt.show()
