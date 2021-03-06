"""Module for testing"""

import pytest
import xarray as xr
import numpy as np
from cmip_basins import generate_basin_codes


@pytest.mark.parametrize("persian", [True, False])
@pytest.mark.parametrize("style", ["cmip6", "gfdl"])
def test_generate_basin_codes(persian, style):
    """Unit tests

    Args:
        persian (bool): logical to include Persian Gulf in Indian basin
        style (str): polygon set to use
    """

    # define 1x1 grid
    lon = np.arange(0.5, 360.5)
    lat = np.arange(89.5, -90.5, -1)

    grid = xr.Dataset()
    grid["lon"] = xr.DataArray(lon, dims=("lon"))
    grid["lat"] = xr.DataArray(lat, dims=("lat"))
    codes = generate_basin_codes(
        grid, lon="lon", lat="lat", persian=persian, style=style
    )

    assert isinstance(codes, xr.core.dataarray.DataArray)
    codes = codes.fillna(0.0)
    assert codes.values.min() == 0
    if style == "gfdl":
        assert codes.values.max() == 17
    elif style == "cmip6":
        assert codes.values.max() in [10, 11]
