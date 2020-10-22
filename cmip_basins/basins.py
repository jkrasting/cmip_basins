#!/usr/bin/env python

"""basins module that includes definitions and creation function """


import argparse
import xarray as xr
import cmip_basins.gfdl as gfdl
import cmip_basins.cmip6 as cmip6


def generate_basin_codes(
    grid, lon="geolon", lat="geolat", mask="wet", persian=False, style="cmip6"
):
    """generate CMIP6 basin codes

    Parameters
    ----------

    grid : xarray.Dataset
        contains grid information: lon, lat, [mask]

    lon : str
        name of longitude array in grid

    lat : str
        name of latitude array in grid

    mask : str
        name of mask array in grid

    persian : bool (default=False)
        have persian gulf as separate code, else merge with indian ocean

    style : str (default=cmip6)
        select polygon set (cmip6/gfdl)

    Returns
    -------

    codes : xr.DataArray
        basin codes
    """

    lon_raw = grid[lon]
    lon = xr.where(lon_raw < -180, lon_raw + 360.0, lon_raw)
    lat = grid[lat]

    if style == "gfdl":
        ind_tmp1 = gfdl.IND_TMP1
        ind_tmp2 = gfdl.IND_TMP2
        ind_ber = gfdl.IND_BER
        ind_ind = gfdl.IND_IND
        ind_pac = gfdl.IND_PAC
        ind_per = gfdl.IND_PER
        dbasins = gfdl.dbasins
    elif style == "cmip6":
        ind_tmp1 = cmip6.IND_TMP1
        ind_ind = cmip6.IND_IND
        ind_pac = cmip6.IND_PAC
        ind_per = cmip6.IND_PER
        dbasins = cmip6.dbasins

    codes = dbasins.mask(lon, lat)
    codes = xr.where(codes == ind_tmp1, ind_pac, codes)  # join PAC1 and PAC2
    if style == "gfdl":
        codes = xr.where(codes == ind_tmp2, ind_ber, codes)  # join BER1 and BER2

    # add persian gulf to indian ocean
    if not persian:
        codes = xr.where(codes == ind_per, ind_ind, codes)

    if mask in grid:
        masked = grid[mask].values
        codes = xr.where(masked == 0, 0, codes)
    else:
        codes.fillna(0)

    codes["lon"] = lon_raw
    return codes


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Adds cmip basin codes to grid file")

    parser.add_argument(
        "grid_file",
        metavar="grid_file",
        type=str,
        help="Grid file for which to create basin codes",
    )
    parser.add_argument(
        "--lon",
        type=str,
        required=False,
        default="geolon",
        help="name of longitude variable to use",
    )
    parser.add_argument(
        "--lat",
        type=str,
        required=False,
        default="geolat",
        help="name of latitude variable to use",
    )
    parser.add_argument(
        "--mask",
        type=str,
        required=False,
        default="wet",
        help="name of mask variable to use",
    )
    parser.add_argument(
        "-o",
        "--fileout",
        type=str,
        required=False,
        default="basin_codes.nc",
        help="name of output file with basin codes added",
    )
    parser.add_argument(
        "-s",
        "--style",
        type=str,
        required=False,
        default="gfdl",
        help="basin mask style (either gfdl or cmip6)",
    )

    args = vars(parser.parse_args())
    print("generating basin codes...")

    Grid = xr.open_dataset(args["grid_file"])
    fileout = args["fileout"]
    args.pop("grid_file")
    args.pop("fileout")

    Grid["basin"] = generate_basin_codes(Grid, **args)

    if args["style"] == "gfdl":
        Grid["basin"].attrs = gfdl.labels
    elif args["style"] == "cmip6":
        Grid["basin"].attrs = cmip6.labels
    Grid.to_netcdf(fileout, format="NETCDF3_64BIT")

    import matplotlib.pyplot as plt

    Grid.basin.plot()
    plt.show()
