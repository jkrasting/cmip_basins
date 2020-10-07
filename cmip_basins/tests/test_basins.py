import pytest
import xarray as xr
import numpy as np
from cmip_basins import basins

@pytest.mark.parametrize("persian", [True, False])
def test_generate_basin_codes(persian):

    from cmip_basins.basins import generate_basin_codes
    # define 1x1 grid
    lon = np.arange(0.5, 360.5)
    lat = np.arange(89.5, -90.5, -1)

    grid = xr.Dataset()
    grid["lon"] = xr.DataArray(lon, dims=("lon"))
    grid["lat"] = xr.DataArray(lat, dims=("lat"))
    codes = generate_basin_codes(grid, lon="lon", lat="lat", persian=persian)

    assert isinstance(codes, xr.core.dataarray.DataArray)
    codes = codes.fillna(0.)
    assert (codes.values.min() == 0)
    assert (codes.values.max() in [10,11])
