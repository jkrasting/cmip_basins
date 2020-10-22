#!/usr/bin/env python

"""basins module that includes definitions and creation function """


import numpy as np
import regionmask

# basins codes used:

IND_SO = 1  # Southern Ocean
IND_ATL = 2  # Atlantic Ocean
IND_PAC = 3  # Pacific Ocean
IND_ARC = 4  # Arctic Ocean
IND_IND = 5  # Indian Ocean
IND_MED = 6  # Mediterranean Sea
IND_BLK = 7  # Black Sea
IND_HUD = 8  # Hudson Bay
IND_BAL = 9  # Baltic Sea
IND_RED = 10  # Red Sea
IND_PER = 11  # Persian Gulf
IND_TMP1 = 99  # to merge 2 parts of Pacific


# polygon points:

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
        [-42.0, 66.5],  # greenland
        [-41.0, 66.0],
        [-40.0, 65.0],  # greenland
        [-18.6, 65.0],  # iceland
        [15.1, 65.0],  # sweden
        [14.49, 56.99],  # South Sweden
        [12.56, 56.04],  # Helsinger
        [12.29, 55.63],  # Copenhagen
        [11.60, 55.49],  # Zealand
        [10.72, 55.32],  # Funen
        [9.23, 54.79],  # Flensburg
        [9.82, 53.50],  # Hamburg
        [2.3, 47.1],  # bourges
        [-0.04, 43.07],  # lourdes
        [-5.6, 40.0],  # caceres
        [-5.6, 30.1],  # morocco
        [cape_town[0], 7],
        [19.0, -33.0],  # just inland from cape town
        [cape_town[0], cape_town[1]],
        [-68.1, cape_town[1]],
        [-68.1, 7],  # venezuela
        [-75.68, 6.22],  # Medellin, Columbia
        [-77.68, 8.12],  # Yaviza, Panama
        [-79.08, 9.32],  # Guna Yala, Panama
        [-81.29, 8.31],  # Veraguas, Panama
        [-83.76, 9.82],  # Costa Rica
        [-86.09, 12.14],  # Nicaragua
        [-88.42, 14.12],  # Honduras/El Sal
        [-90.77, 15.10],  # Quiche, Guatemala
        [-96.04, 17.56],  # Oaxaca, MX
        [-99.1, 19.4],  # mexico city
        [-106.7, 35.1],  # albequerque
        [-76.46, 49.60],  # Baie James. QC
        [-71.71, 60.72],  # Riviere Koksoak, QC
        [-70.83, 63.06],  # Kimmirut, Nunavut
        [-69.62, 64.14],  #
        [-68.61, 66.46],  # Kipisa, NU
        [-68.20, 67.72],  # Baffin island
        [-62.02, 66.71],  # Cape Dyer
        [-52.46, 68.29],  # Davis strait, Greenland side
    ]
)

PAC1 = np.array(
    [
        [-180.0, 67.0],
        [-179.84, 66.85],  # Russia
        [-177.52, 66.69],  # Russia
        [-174.10, 66.02],  # Russia
        [-169.86, 66.09],  # Naukan, Russia
        [-169.06, 65.80],  # Big Diomede
        [-167.97, 65.61],  # Wales, AK
        [-140.0, 65.0],
        [-106.7, 35.1],  # albequerque
        [-99.1, 19.4],  # mexico city
        [-96.04, 17.56],  # Oaxaca, MX
        [-90.77, 15.10],  # Quiche, Guatemala
        [-88.42, 14.12],  # Honduras/El Sal
        [-86.09, 12.14],  # Nicaragua
        [-83.76, 9.82],  # Costa Rica
        [-81.29, 8.31],  # Veraguas, Panama
        [-79.08, 9.32],  # Guna Yala, Panama
        [-77.68, 8.12],  # Yaviza, Panama
        [-75.68, 6.22],  # Medellin, Columbia
        [-68.1, 7],  # venezuela
        [-68.1, melbourne[1]],
        [-180.0, melbourne[1]],
    ]
)

PAC2 = np.array(
    [
        [98.8, 65.0],
        [180.0, 67.0],
        [180.0, melbourne[1]],
        [melbourne[0], melbourne[1]],
        [melbourne[0], -30],
        [123.1, -10.7],  # rote island
        [119.95, -9.75],  # Sumba Regency
        [117.31, -8.73],  # West Nusa
        [116.33, -8.60],  # Lombok
        [115.18, -8.45],  # Bali
        [113.95, -8.09],  # east Java
        [106.41, -6.56],  # west Java
        [105.39, -5.25],  # south Sumatra
        [102.19, 0.07],  # Sumatra
        [103.85, 1.69],  # singapore
        [98.86, 9.03],  # Thailand
        [98.8, 9.1],  # surat thani
        [99.07, 16.73],  # Tak, Thailand
        [98.8, 23.0],  # mangmao
        [95.33, 27.42],  # Tinkusia, india
    ]
)

ARC = np.array(
    [
        [-180.0, 90.0],
        [180.0, 90.0],
        [180.0, 67.0],
        [98.8, 65.0],  # krasnoyarsk
        [35.93, 60.93],  # Russia
        [21.30, 68.04],  # North Sweden
        [15.1, 65.0],  # sweden
        [-18.6, 65.0],  # iceland
        [-40.0, 65.0],  # greenland
        [-41.0, 66.0],
        [-42.0, 66.5],  # greenland
        [-52.46, 68.29],  # Davis strait, Greenland side
        [-62.02, 66.71],  # Cape Dyer
        [-68.20, 67.72],  # Baffin island
        [-78.18, 71.13],  # Baffin island
        [-83.69, 71.03],  # Baffin island
        [-84.35, 68.07],  # Baffin, NU
        [-86.93, 66.88],  # Keewatin, NU
        [-93.19, 66.34],  # Keewatin, NU
        [-100.53, 64.47],  # Keewatin, NU
        [-140.0, 65.0],
        [-167.97, 65.61],  # Wales, AK
        [-169.06, 65.80],  # Big Diomede
        [-169.86, 66.09],  # Naukan, Russia
        [-174.10, 66.02],  # Russia
        [-177.52, 66.69],  # Russia
        [-179.84, 66.85],  # Russia
        [-180.0, 67.0],
    ]
)

HUD = np.array(
    [
        [-70.83, 63.06],  # Kimmirut, Nunavut
        [-71.71, 60.72],  # Riviere Koksoak, QC
        [-76.46, 49.60],  # Baie James. QC
        [-87.01, 52.01],  # Ontario
        [-99.04, 57.21],  # Manitoba
        [-100.53, 64.47],  # Keewatin, NU
        [-93.19, 66.34],  # Keewatin, NU
        [-86.93, 66.88],  # Keewatin, NU
        [-84.35, 68.07],  # Baffin, NU
        [-83.69, 71.03],  # Baffin island
        [-78.18, 71.13],  # Baffin island
        [-68.20, 67.72],  # Baffin island
        [-68.61, 66.46],  # Kipisa, NU
        [-69.62, 64.14],  #
    ]
)

IND = np.array(
    [
        [cape_town[0], 7],
        [36.0, 15.2],  # eritra
        [43.17, 12.50],  # bab al-mandab
        [43.60, 12.84],  # bab al-mandab
        [57.4, 22.9],  # nizwa
        [55.6, 24.1],  # al ain
        [57.0, 27.1],  # minab
        [62.1, 25.4],  # turbat
        [95.33, 27.42],  # Tinkusia, india
        [98.8, 23.0],  # mangmao
        [99.07, 16.73],  # Tak, Thailand
        [98.8, 9.1],  # surat thani
        [98.86, 9.03],  # Thailand
        [103.85, 1.69],  # singapore
        [102.19, 0.07],  # Sumatra
        [105.39, -5.25],  # south Sumatra
        [106.41, -6.56],  # west Java
        [113.95, -8.09],  # east Java
        [115.18, -8.45],  # Bali
        [116.33, -8.60],  # Lombok
        [117.31, -8.73],  # West Nusa
        [119.95, -9.75],  # Sumba Regency
        [123.1, -10.7],  # rote island
        [melbourne[0], -30],
        [perth[0], -30],
        [perth[0], cape_town[1]],
        [cape_town[0], cape_town[1]],
        [19.0, -33.0],  # just inland from cape town
    ]
)

MED = np.array(
    [
        [2.3, 47.1],  # bourges
        [11.6, 48.0],  # munich
        [28.7, 41.0],  # istanbul
        [33.02, 40.03],  # ankara
        [37.3, 37.1],  # gaziantep
        [36.8, 30.6],  # jordan
        [31.2, 30.1],  # cairo
        [-5.6, 30.1],  # morocco
        [-5.6, 40.0],  # caceres
        [-0.04, 43.07],  # lourdes
    ]
)

BLK = np.array(
    [
        [28.7, 41.0],  # istanbul
        [24.78, 43.51],  # pleven
        [30.1, 48.7],  # uman
        [44.2, 48.7],  # volograd
        [43.9, 36.2],  # erbil
        [33.02, 40.03],  # ankara
    ]
)

BAL = np.array(
    [
        [9.82, 53.50],  # Hamburg
        [9.23, 54.79],  # Flensburg
        [10.72, 55.32],  # Funen
        [11.60, 55.49],  # Zealand
        [12.29, 55.63],  # Copenhagen
        [12.56, 56.04],  # Helsinger
        [14.49, 56.99],  # South Sweden
        [15.1, 65.0],  # sweden
        [21.30, 68.04],  # North Sweden
        [35.93, 60.93],  # Russia
        [30.42, 59.85],  # st petersburg
        [21.06, 52.42],  # warsaw
        [12.18, 51.24],  # Liepzig
    ]
)

RED = np.array(
    [
        [36.8, 30.6],  # jordan
        [44.2, 18.5],  # yadamah
        [43.60, 12.84],  # bab al-mandab
        [43.17, 12.50],  # bab al-mandab
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


dbasins = regionmask.Regions(
    [SO, ATL, PAC1, PAC2, ARC, IND, MED, BLK, HUD, BAL, RED, PER],
    [
        IND_SO,
        IND_ATL,
        IND_TMP1,
        IND_PAC,
        IND_ARC,
        IND_IND,
        IND_MED,
        IND_BLK,
        IND_HUD,
        IND_BAL,
        IND_RED,
        IND_PER,
    ],
)


labels = {
    "flag_meanings": "1:Southern Ocean, 2:Atlantic Ocean, "
    + "3:Pacific Ocean, 4:Arctic Ocean, "
    + "5:Indian Ocean, 6:Mediterranean Sea, "
    + "7:Black Sea, 8:Hudson Bay, 9:Baltic Sea, "
    + "10:Red Sea, 11:Persian Gulf",
    "flag_values": "1,2,3,4,5,6,7,8,9,10,11",
}
