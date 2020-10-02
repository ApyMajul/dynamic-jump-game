# -*- coding: utf-8 -*-
# @Author: apyju
# @Date:   2018-11-26 15:56:37
# @Last Modified by:   apyju
# @Last Modified time: 2019-02-07 14:59:24
import sys
sys.path.insert(0, "jeux")

import pygame
from pygame.locals import *
from player import *
from levels import *
from constantes import *
from spritelist import *
from message import *

pygame.init()

# Création de la fenêtre
fenetre = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icone = pygame.image.load(hufflepuff)
pygame.display.set_icon(icone)
pygame.display.set_caption(titre_fenetre)
menu_info = pygame.Surface((menu_info_width, menu_info_height))
menu_info.fill((255, 165, 0))
font_info = pygame.font.SysFont('arial', 25)
zdj = pygame.Surface((zdj_width, zdj_height))

player = Player()
clock = pygame.time.Clock()

# Create all the levels
level_list = []
level_list.append(Level_01(player, n1, fond1))
level_list.append(Level_01(player, n2, fond2))
level_list.append(Level_01(player, n3, fond3))
# level_list.append(Level_01(player, 'n4', fond4))
# level_list.append(Level_01(player, 'n5', fond5))

continuer = True
while continuer:
    # chargement et affichage de l'écran d'accueil
    accueil = pygame.image.load(screenload).convert()
    second = pygame.image.load(secondecran).convert()
    fenetre.blit(accueil, (0, 0))
    continuer_acceuil = True
    continuer_jeux = False
    continuer_mission = False
    current_level_no = 0
    dt = clock.tick(60)

    pygame.display.flip()

    while continuer_acceuil:

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer_acceuil = False
                continuer = False

            elif event.type == KEYDOWN and event.key == K_SPACE:
                continuer_acceuil = False
                continuer_mission = True

            elif event.type == KEYDOWN and event.key == K_RETURN:
                continuer_acceuil = False
                continuer_jeux = True

    current_level = level_list[current_level_no]
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
    player.rect.x = current_level.start[0]
    player.rect.bottom = current_level.start[1]
    active_sprite_list.add(player)

    while continuer_mission:
        fenetre.blit(second, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer_mission = False
                continuer = False

            elif event.type == KEYDOWN and event.key == K_RETURN:
                continuer_mission = False
                continuer_jeux = True

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_mission = False
                continuer_acceuil = True

    while continuer_jeux:

        dt = clock.tick(60)

        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                # continuer = False
                continuer_jeux = False
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_jeux = False
                # continuer = False

        player.react(events)
        active_sprite_list.update(dt)
        current_level.update(dt)

        # If the player gets near the up or bottom side, shift the world
        if player.rect.y >= 500 and current_level.world_shift > 0:
            diff = player.rect.y - 500
            player.rect.y = 500
            current_level.shift_world(-diff)

        if player.rect.y <= 100 and current_level.world_shift < current_level.level_limit:
            diff = 100 - player.rect.y
            player.rect.y = 100
            current_level.shift_world(diff)

        # Limite du joueur gauche et droite
        if player.rect.left < 0:
            player.rect.left = 0
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH

        if player.vie <= 0:
            continuer_jeux = False

        # Si le joueur atteint la sortie
        exit = pygame.sprite.spritecollide(player, current_level.exit, False)
        for sortie in exit:
            if current_level_no < len(level_list) - 1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
                player.rect.x = current_level.start[0]
                player.rect.y = current_level.start[1]

            else:
                continuer_jeux = False

        # gestion du menu info
        info_vie = font_info.render('Vie: ' + str(player.vie), 1, (0, 0, 0))
        fenetre.blit(menu_info, (menu_info_X, menu_info_Y))
        fenetre.blit(info_vie, (10, 25))
        fenetre.blit(zdj, (zdj_X, zdj_Y))

        current_level.draw(zdj)
        player.draw(zdj)
        # active_sprite_list.draw(zdj)
        pygame.display.flip()

pygame.quit()
