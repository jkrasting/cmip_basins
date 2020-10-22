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
IND_SJKES = 12  # Sea of Japan / Korean East Sea
IND_OKH = 13  # Sea of Okhotsk
IND_MEASR = 14  # Margnal East Asian Sea Region
IND_BER = 15  # Bering Sea
IND_NOR = 16  # Nordic Seas
IND_GOM = 17  # Gulf of Mexico
IND_TMP1 = 98  # to merge 2 parts of Pacific
IND_TMP2 = 99  # to merge 2 parts of Bering

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
        [-30.7, 69.8],
        [-20.4, 64.58],  # iceland
        [-7.2, 62.0],  # faroe
        [-4.3, 57.5],  # inverness
        [-0.2, 51.5],  # london
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
        [-180.0, 51.3],
        [-178.5, 51.8],  # tanaga island
        [-176.6, 51.9],  # adak
        [-174.3, 52.2],  # atka
        [-169.0, 53.0],  # nikolski
        [-166.7, 53.5],  # unalaska isalnd
        [-164.6, 54.5],
        [-160.2, 55.8],
        [-158.1, 56.9],  # aniakchak
        [-156.6, 58.1],  # becharof lake
        [-156.4, 65.7],  # husila
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
        [180.0, melbourne[1]],
        [melbourne[0], melbourne[1]],
        [melbourne[0], -30],
        [142.4, -22.3],  # queensland
        [142.4, -11.6],  # mapoon, queensland
        [142.4, -8.7],  # bubuji, papua new guinea
        [146.9, -6.7],  # lae
        [137.7, -2.0],
        [134.9, -3.7],  # gariau
        [132.9, -1.3],  # west papau
        [131.0, -0.2],  # waigeo
        [128.5, 2.3],  # morotai island
        [126.3, 7.4],  # caraga
        [125.3, 12.2],  # samar island
        [122.1, 18.4],  # santa ana, luzon
        [120.8, 21.9],  # southern tip taiwan
        [121.9, 25.0],  # gongliao taiwan
        [130.0, 30.8],  # kagoshima
        [130.95, 32.83],  # kumamoto
        [131.1, 34.19],  # Mine
        [136.5, 35.44],  # nagoya
        [139.5, 37.4],  # fukushima
        [140.5, 40.39],  # aomori
        [140.1, 42.43],  # imakane
        [141.5, 43.3],  # hokkaido
        [145.2, 43.3],  # nemuro
        [156.1, 50.7],  # severo-kurislk
        [160.4, 57.4],  # central kamchatka
        [163.7, 55.9],  # kamchatka
        [166.0, 55.0],  # bering island
        [173.1, 52.8],  # attu station
        [180.0, 51.3],
    ]
)

ARC = np.array(
    [
        [-180.0, 90.0],
        [180.0, 90.0],
        [180.0, 51.3],
        [180.0, 67.0],
        [167.0, 63.0],
        [165.0, 61.4],  # kamchatka
        [164.8, 64.5],  # penzhinsky, kamchatka
        [35.93, 60.93],  # Russi
        [21.30, 68.04],  # North Sweden
        [17.63, 78.7],  # svalbard
        [-11.9, 81.5],
        [-30.0, 78.5],
        [-30.7, 69.8],
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
        [-156.4, 65.7],  # husila
        [-168.1, 65.6],  # wales
        [-169.7, 66.0],  # naukan
        [-180.0, 67.0],
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
        [126.9, -8.5],  # timor
        [125.9, -11.2],  # darwin
        [131.8, -22.3],  # yuendumu, northern territory
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

SJKES = np.array(
    [
        [129.2, 35.2],  # tongyeong
        [130.95, 32.83],  # kumamoto
        [131.1, 34.19],  # Mine
        [136.5, 35.44],  # nagoya
        [139.5, 37.4],  # fukushima
        [140.5, 40.39],  # aomori
        [140.1, 42.43],  # imakane
        [141.5, 43.3],  # hokkaido
        [142.17, 44.79],  # wakkanai
        [142.1, 46.1],  # shebunino
        [142.5, 47.1],  # sinegorsk
        [142.4, 48.9],  # medvezh'ye
        [142.4, 53.4],  # zaliv baykal
        [140.7, 53.1],  # nikolaevsk
        [126.4, 43.9],  # jilin city
        [126.9, 37.6],  # seoul
    ]
)

OKH = np.array(
    [
        [160.4, 57.4],  # central kamchatka
        [156.1, 50.7],  # severo-kurislk
        [145.2, 43.3],  # nemuro
        [141.5, 43.3],  # hokkaido
        [142.17, 44.79],  # wakkanai
        [142.1, 46.1],  # shebunino
        [142.5, 47.1],  # sinegorsk
        [142.4, 48.9],  # medvezh'ye
        [142.4, 53.4],  # zaliv baykal
        [140.7, 53.1],  # nikolaevsk
        [135.9, 53.1],  # burukan
        [130.2, 58.2],  # sakha
        [164.8, 64.5],  # penzhinsky, kamchatka
        [165.0, 61.4],  # kamchatka
        [162.6, 60.3],  # kamchatka
    ]
)

MEASR = np.array(
    [
        [126.4, 43.9],  # jilin city
        [117.7, 40.9],  # chengde
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
        [126.9, -8.5],  # timor
        [125.9, -11.2],  # darwin
        [131.8, -22.3],  # yuendumu, northern territory
        [142.4, -22.3],  # queensland
        [142.4, -11.6],  # mapoon, queensland
        [142.4, -8.7],  # bubuji, papua new guinea
        [146.9, -6.7],  # lae
        [137.7, -2.0],
        [134.9, -3.7],  # gariau
        [132.9, -1.3],  # west papau
        [131.0, -0.2],  # waigeo
        [128.5, 2.3],  # morotai island
        [126.3, 7.4],  # caraga
        [125.3, 12.2],  # samar island
        [122.1, 18.4],  # santa ana, luzon
        [120.8, 21.9],  # southern tip taiwan
        [121.9, 25.0],  # gongliao taiwan
        [130.0, 30.8],  # kagoshima
        [130.95, 32.83],  # kumamoto
        [129.2, 35.2],  # tongyeong
        [126.9, 37.6],  # seoul
        [126.4, 43.9],  # jilin city
    ]
)

BER1 = np.array(
    [
        [163.7, 55.9],  # kamchatka
        [166.0, 55.0],  # bering island
        [173.1, 52.8],  # attu station
        [180.0, 51.3],
        [180.0, 67.0],
        [167.0, 63.0],
        [165.0, 61.4],  # kamchatka
        [162.6, 60.3],  # kamchatka
        [160.4, 57.4],
    ]
)

BER2 = np.array(
    [
        [-180.0, 67.0],
        [-169.7, 66.0],  # naukan
        [-168.1, 65.6],  # wales
        [-156.4, 65.7],  # husila
        [-156.6, 58.1],  # becharof lake
        [-158.1, 56.9],  # aniakchak
        [-160.2, 55.8],
        [-164.6, 54.5],
        [-166.7, 53.5],  # unalaska isalnd
        [-169.0, 53.0],  # nikolski
        [-174.3, 52.2],  # atka
        [-176.6, 51.9],  # adak
        [-178.5, 51.8],  # tanaga island
        [-180.0, 51.3],
    ]
)

NOR = np.array(
    [
        [-7.2, 62.0],  # faroe
        [-20.4, 64.58],  # iceland
        [-30.7, 69.8],
        [-30.0, 78.5],
        [-11.9, 81.5],
        [17.63, 78.7],  # svalbard
        [21.30, 68.04],  # North Sweden
        [15.1, 65.0],  # sweden
        [14.49, 56.99],  # South Sweden
        [12.56, 56.04],  # Helsinger
        [12.29, 55.63],  # Copenhagen
        [11.60, 55.49],  # Zealand
        [10.72, 55.32],  # Funen
        [9.23, 54.79],  # Flensburg
        [9.82, 53.50],  # Hamburg
        [2.3, 47.1],  # bourges
        [-0.2, 51.5],  # london
        [-4.3, 57.5],  # inverness
    ]
)

GOM = np.array(
    [
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
        [-83.6, 32.8],  # macon
        [-81.4, 28.4],  # orlando
        [-80.5, 25.1],  # key largo
        [-80.8, 23.1],  # la teja
        [-77.9, 21.4],  # camaguey
        [-75.2, 20.1],  # guantanamo
        [-68.6, 18.6],  # punta cana
        [-66.4, 18.2],  # central puerto rico
        [-63.2, 18.0],  # anguilla
        [-62.8, 17.2],  # st kitts
        [-62.2, 16.7],  # montserrat
        [-61.7, 16.1],  # guadeloupe
        [-61.5, 15.4],  # dominica
        [-61.2, 14.6],  # martinque
        [-61.1, 13.9],  # st lucia
        [-61.6, 13.0],  # st vincent and the grenadines
        [-61.7, 12.3],  # grenada
        [-61.5, 10.7],  # trinidad and tobago
    ]
)


dbasins = regionmask.Regions(
    [
        SO,
        ATL,
        PAC1,
        PAC2,
        ARC,
        IND,
        MED,
        BLK,
        HUD,
        BAL,
        RED,
        PER,
        SJKES,
        OKH,
        MEASR,
        BER1,
        BER2,
        NOR,
        GOM,
    ],
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
        IND_SJKES,
        IND_OKH,
        IND_MEASR,
        IND_BER,
        IND_TMP2,
        IND_NOR,
        IND_GOM,
    ],
)


labels = {
    "flag_meanings": "1:Southern Ocean, 2:Atlantic Ocean, "
    + "3:Pacific Ocean, 4:Arctic Ocean, "
    + "5:Indian Ocean, 6:Mediterranean Sea, "
    + "7:Black Sea, 8:Hudson Bay, 9:Baltic Sea, "
    + "10:Red Sea, 11:Persian Gulf, "
    + "12:Sea of Japan / Korean East Sea, "
    + "13:Sea of Okhotsk, "
    + "14:Marginal East Asian Sea Region, "
    + "15:Bering Sea, 16: Nordic Seas, "
    + "17:Gulf of Mexico",
    "flag_values": "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17",
}
