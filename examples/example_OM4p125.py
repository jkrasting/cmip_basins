from cmip_basins.basins import generate_basin_codes
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

ds = xr.open_dataset('/archive/Raphael.Dussin/datasets/OM4p125/OM4p125_grid_20200921_noiceshelves_unpacked/ocean_static.nc')

codes = generate_basin_codes(ds)

# number of points unaccounted for
nmissing = len(np.where(np.isnan(codes))[0])
print(f'we have {nmissing} points without a code')

codes.plot(x='lon',y='lat', cmap='tab20')
plt.show()
