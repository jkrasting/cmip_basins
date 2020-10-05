import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import regionmask


melbourne = (145.0, -37.8)
cape_town = (18.4, -33.9)

perth = (115.9, -32.0)  # lon

SO = np.array(
    [
        [-180, melbourne[1]],
        [-68.1, melbourne[1]],
        [-68.1, cape_town[1]],
        [cape_town[0], cape_town[1]],
        [perth[0], cape_town[1]],
        [perth[0], -30],
        [melbourne[0], -30],
        [melbourne[0], melbourne[1]],
        [180.0, melbourne[1]],
        [180, -90],
        [-180, -90],
    ]
)

ATL = np.array(
    [
        [-49.0, 80.0],  # lab sea greenland
        [-47.3, 65.0],  # greenland
        [-18.6, 65.0],  # iceland
        [15.1, 65.0],  # sweden
        [9.16, 56.4],  # denmark
        [2.3, 47.1],  # bourges
        [-5.6, 40.0],  # caceres
        [-5.6, 30.1],  # morocco
        [cape_town[0], 7],
        [cape_town[0], cape_town[1]],
        [-68.1, cape_town[1]],
        [-68.1, 7],  # venezuela
        [-79.7, 9.1],  # gabon
        [-99.1, 19.4],  # mexico city
        [-106.7, 35.1],  # albequerque
        [-66.9, 52.9],  # labrador city
        [-70.4, 65.0],  # baffin island 1
        [-72.7, 69.9],  # nunavut
        [-85.9, 80.0],  # eureka
    ]
)

PAC1 = np.array(
    [
        [-180.0, 65.0],
        [-140.0, 65.0],
        [-106.7, 35.1],  # albequerque
        [-99.1, 19.4],  # mexico city
        [-79.7, 9.1],  # gabon
        [-68.1, 7],  # venezuela
        [-68.1, melbourne[1]],
        [-180.0, melbourne[1]],
    ]
)

PAC2 = np.array(
    [
        [98.8, 65.0],
        [180.0, 65.0],
        [180.0, melbourne[1]],
        [melbourne[0], melbourne[1]],
        [melbourne[0], -30],
        [123.1, -10.7],  # rote island
        [105.2, -6.6],  # panaitan island
        [101.6, 3.1],  # kuala lumpur
        [98.8, 9.1],
    ]
)

ARC = np.array(
    [
        [-180.0, 90.0],
        [180.0, 90.0],
        [180.0, 65.0],
        [98.8, 65.0],  # krasnoyarsk
        [35.0, 60.0],  # leningrad
        [25.0, 69.0],  # karasjok
        [15.1, 65.0],  # st petersburg
        [-47.3, 65.0],  # sermersooq 1
        [-49.0, 80.0],  # sermersooq 2
        [-85.9, 80.0],  # ellesmere island
        [-72.7, 69.9],  # baffin island 2
        [-70.4, 65.0],  # baffin island 1
        [-84.7, 64.8],  # coral harbour
        [-90.0, 66.0],  # keewatin
        [-140.0, 65.0],
        [-180.0, 65.0],
    ]
)

HUD = np.array(
    [
        [-90.0, 66.0],  # keewatin
        [-84.7, 64.8],  # coral harbour
        [-70.4, 65.0],  # baffin island
        [-66.9, 52.9],  # labrador city
        [-78.1, 48.0],  # val-d'or
        [-107.2, 59.3],  # fond-du-lac
    ]
)

IND = np.array(
    [
        [cape_town[0], 7],
        [43.8, 12.4],  # bab al-mandab
        [57.4, 22.9],  # nizwa
        [55.6, 24.1],  # al ain
        [57.0, 27.1],  # minab
        [62.1, 25.4],  # turbat
        [98.8, 23.0],  # mangmao
        [98.8, 9.1],  # surat thani
        [105.2, -6.6],  # panaitan island
        [123.1, -10.7],  # rote island
        [melbourne[0], -30],
        [perth[0], -30],
        [perth[0], cape_town[1]],
        [cape_town[0], cape_town[1]],
    ]
)

MED = np.array(
    [
        [2.3, 47.1],  # bourges
        [11.6, 48.0],  # munich
        [28.7, 41.0],  # istanbul
        [37.3, 37.1],  # gaziantep
        [36.8, 30.6],  # jordan
        [31.2, 30.1],  # cairo
        [-5.6, 30.1],  # morocco
        [-5.6, 40.0],  # caceres
    ]
)

BLK = np.array(
    [
        [28.7, 41.0],  # istanbul
        [23.2, 42.7],  # sofia
        [30.1, 48.7],  # uman
        [44.2, 48.7],  # volograd
        [43.9, 36.2],  # erbil
    ]
)

BAL = np.array(
    [
        [15.1, 65.0],  # st petersburg
        [25.0, 69.0],  # karasjok
        [35.0, 60.0],  # leningrad
        [11.6, 48.0],  # munich
        [2.3, 47.1],  # bourges
    ]
)

RED = np.array(
    [
        [36.8, 30.6],  # jordan
        [44.2, 18.5],  # yadamah
        [43.8, 12.4],  # bab al-mandab
        [36.0, 15.2],  # eritra
        [30.5, 25.4],  # kharga
        [31.2, 30.1],  # cairo
    ]
)

PER = np.array(
    [
        [57.4, 22.9],  # nizwa
        [49.3, 23.1],  # umm athelah
        [47.0, 29.7],  # kuwait
        [47.6, 30.5],  # basrah
        [50.2, 30.6],  # behbahan
        [57.0, 27.1],  # minab
        [55.6, 24.1],  # al ain
    ]
)

basins = regionmask.Regions(
    [SO, ATL, PAC1, PAC2, ARC, IND, MED, BLK, HUD, BAL, RED, PER]
)

# define 1x1 grid
lon = np.arange(0.5, 360.5)
lat = np.arange(89.5, -90.5, -1)

# make plot
fig = plt.figure(figsize=(25, 10))
ax = plt.subplot(111, projection=ccrs.PlateCarree())
mask = basins.mask(lon, lat)
# pcolormesh does not handle NaNs, requires masked array
mask_ma = np.ma.masked_invalid(mask)
h = ax.pcolormesh(lon, lat, mask_ma, transform=ccrs.PlateCarree(), cmap="jet",)
basins.plot_regions(ax=ax, add_label=False)
ax.coastlines()

plt.savefig("basins.png")
