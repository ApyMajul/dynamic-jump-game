# -*- coding: utf-8 -*-
# @Author: apyju
# @Date:   2018-12-23 18:22:24
# @Last Modified by:   apyju
# @Last Modified time: 2018-12-23 19:40:31
import pygame
from pygame.locals import *


def ecriture():
    # font_code = pygame.font.SysFont('arial', 25)
    # code_space = pygame.Surface((100, 50))
    # code_space.fill((0, 0, 0))

    mot = ""
    lettres = ""
    mot_masque = []
    for event in pygame.event.get():
        masque = []
        if event.type == KEYDOWN:
            lettre = chr(event.key)
            masque.append("*")
            lettres += lettre
        mot_masque.append(masque)
        print(mot_masque)


# info = font_code.render(str(mot_masque), 1, (0, 0, 0))
# fenetre.blit(code_space, (300, 300))
# fenetre.blit(info, (300, 300))


# info_vie = font_info.render('Vie: ' + str(player.vie), 1, (0, 0, 0))
# fenetre.blit(menu_info, (menu_info_X, menu_info_Y))


# def get_key():
#     while 1:
#         event = pygame.event.poll()
#         if event.type == KEYDOWN:
#             return event.key
#         else:
#             pass


# def display_box(fenetre, message):
#     """print a message in a box in middle"""
#     fontobject = pygame.font.Font(None, 18)
#     pygame.draw.rect(fenetre, (0, 0, 0), ((SCREEN_WIDTH / 2) -
#                                           100, (SCREEN_HEIGHT / 2) - 10, 200, 20), 0)
#     pygame.draw.rect(fenetre, (255, 255, 255), ((SCREEN_WIDTH / 2) -
#                                                 102, (SCREEN_HEIGHT / 2) - 12, 204, 24), 1)
#     if len(message) != 0:
#         fenetre.blit(fontobject.render(message, 1, (255, 255, 255)), ((SCREEN_WIDTH / 2) -
#                                                                       100, (SCREEN_HEIGHT / 2) - 10))
#     pygame.display.flip()


# def ask(fenetre, question):
#     pygame.font.init()
#     current_string = []
#     display_box(fenetre, question + " : " + string.join(current_string, ""))
#     while 1:
#         inkey = get_key()
#         if inkey == K_BACKSPACE:
#             current_string = current_string[0:-1]
#         elif inkey == K_RETURN:
#             break
#         elif inkey == K_MINUS:
#             current_string.append("_")
#         elif inkey <= 127:
#             current_string.Append(chr(inkey))
#         display_box(fenetre, question + " : " + string.join(current_string, ""))
#     return string.join(current_string, "")
