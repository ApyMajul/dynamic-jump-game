# -*- coding: utf-8 -*-
from constantes import *

# JOUEUR
# il faut centrer les animations et faire en sorte que height et weight soient constants

# transformer un perso en dictionnaire comprenant toutes les animations avec son nom comme clé

walk = [
    [21, 194, 32, 65],
    [21, 194, 32, 65],
    [64, 192, 24, 67],
    [97, 192, 27, 67],
    [132, 194, 31, 66],
    [174, 193, 22, 67],
    [209, 194, 24, 66],
]

jump = [
    [22, 563, 34, 67],
    [22, 563, 34, 67],
    [69, 568, 45, 62],
    [141, 596, 31, 44],
]

teleport = [
    [378, 615, 46, 57],
    [437, 609, 34, 63],
]

attack = [
    [28, 1115, 37, 65],
    [28, 1115, 37, 65],
    [75, 1117, 36, 63],
    [126, 1115, 48, 65],
    [185, 1101, 48, 79],
    [247, 1107, 39, 73],
]

attack2 = [
    [710, 2291, 93, 54],
    [710, 2291, 93, 54],
    [818, 2291, 75, 52],
    [818, 2291, 75, 52],
    [906, 2291, 77, 56],
    [906, 2291, 77, 56],
]


damage = [
    [21, 842, 47, 48],
    [80, 838, 51, 52],
    [170, 840, 56, 46],
    [239, 859, 70, 27],
    [319, 866, 69, 24],
    [398, 836, 34, 50],
]


# Décors
GRASS_LEFT = (576, 720, 70, 70)
GRASS_RIGHT = (576, 576, 70, 70)
GRASS_MIDDLE = (504, 576, 70, 70)
STONE_PLATFORM_LEFT = (432, 720, 70, 40)
STONE_PLATFORM_MIDDLE = (648, 648, 70, 40)
STONE_PLATFORM_RIGHT = (792, 648, 70, 40)
ECHELLE = (504, 72, 70, 70)
EXIT = (288, 360, 70, 70)
START = (288, 432, 70, 70)
LAVE = (432, 817, 70, 45)


# enemis
enemi1 = [
    [340, 396, 30, 37],
    [379, 397, 32, 36],
]

enemi2 = [
    [600, 396, 30, 37],
    [639, 397, 32, 36],
]

enemisterrain = [enemi1, enemi2]

enemivolant1 = [
    [89, 558, 25, 40],
    [132, 572, 22, 34],
]

enemivolant2 = [
    [602, 305, 22, 24],
    [642, 296, 22, 33],
]

enemisvolants = [enemivolant1, enemivolant2]


# effets
fumee = [
        [1199, 492, 46, 37],
        [1258, 476, 45, 53],
        [1318, 467, 45, 53],
        [1375, 460, 44, 50],
        [1431, 459, 40, 46],
]

projectile = [272, 1327, 54, 32]
