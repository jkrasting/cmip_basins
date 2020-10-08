import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
from cmip_basins.basins import *

# define 1x1 grid
lon = np.arange(0.5, 360.5)
lat = np.arange(89.5, -90.5, -1)

# make plot
fig = plt.figure(figsize=(25, 10))
ax = plt.subplot(111, projection=ccrs.PlateCarree())
mask = dbasins.mask(lon, lat)
mask = xr.where(mask == ind_tmp, ind_PAC, mask)

# pcolormesh does not handle NaNs, requires masked array
mask_ma = np.ma.masked_invalid(mask)
h = ax.pcolormesh(lon, lat, mask_ma, transform=ccrs.PlateCarree(), cmap="jet",)
dbasins.plot_regions(ax=ax, add_label=False, line_kws=dict(color="r"))
ax.coastlines()

plt.show()
# plt.savefig("basins.png")

grid = xr.Dataset()
grid["lon"] = xr.DataArray(lon, dims=("lon"))
grid["lat"] = xr.DataArray(lat, dims=("lat"))
codes = generate_basin_codes(grid, lon="lon", lat="lat")

plt.figure()
ax = plt.subplot(111, projection=ccrs.PlateCarree())
codes.plot(ax=ax, x="lon", y="lat", cmap="tab20")
ax.coastlines()

plt.show()
