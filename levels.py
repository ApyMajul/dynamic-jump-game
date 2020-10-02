# -*- coding: utf-8 -*-
# @Author: apyju
# @Date:   2018-11-26 16:43:12
# @Last Modified by:   apyju
# @Last Modified time: 2018-12-23 12:32:10
import pygame
from constantes import *
import platforms
import spritelist
from enemis import *
from spritesheet import SpriteSheet
from random import *


def generer(fichier):
    with open(fichier, 'r') as fichier:
        structure_niveau = []
        for ligne in fichier:
            ligne_niveau = []
            for sprite in ligne:
                if sprite != '/n':
                    ligne_niveau.append(sprite)
            structure_niveau.append(ligne_niveau)
            structure = structure_niveau

    return structure


class Level:
    """This is a generic super-class used to define a level.
    Create a child class for each level witj level-specific
    info. """
    # platform_list = None
    # decor_list = None
    # enemy_list = None
    # background = None
    # exit = None

    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        """Pass in a handle to player. Needed for when collide with
        player"""
        self.decor_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.exit = pygame.sprite.Group()
        self.obstacles_list = pygame.sprite.Group()
        self.player = player
        self.start = []

    def update(self, dt):
        """update everything on this level"""
        self.decor_list.update()
        self.platform_list.update()
        self.obstacles_list.update()
        for enemi in self.enemy_list:
            if enemi.vie <= 0:
                self.enemy_list.remove(enemi)
        self.enemy_list.update(dt)

    def draw(self, screen):
        """draw everything on this level"""
        screen.fill(BLUE)
        screen.blit(self.background, (0, - self.level_limit - (self.world_shift) * -1))
        # self.world_shift))
        self.decor_list.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.obstacles_list.draw(screen)

    def shift_world(self, shift_y):
        """when user move left/right and we need to scroll"""
        self.world_shift += shift_y

        for enemis in self.enemy_list:
            enemis.rect.y += shift_y

        for platform in self.platform_list:
            platform.rect.y += shift_y

        for obstacle in self.obstacles_list:
            obstacle.rect.y += shift_y

        for element in self.decor_list:
            element.rect.y += shift_y

        for sorti in self.exit:
            sorti.rect.y += shift_y


class Level_01(Level):
    """definition for level 1 """

    def __init__(self, player, fichier, background):
        Level.__init__(self, player)

        self.fichier = fichier
        self.structure = 0
        self.background = pygame.image.load(background).convert()
        self.nb_enemis = 2
        self.level_limit = 780
        # self.background.set_colorkey(constantes.BLACK)

        level = []
        decor = []
        sortie = []
        move = []
        enemis = []
        obstacles = []
        self.structure = generer(fichier)

        num_ligne = 0
        for ligne in self.structure:
            num_case = 0
            for sprite in ligne:
                x = num_case * 30
                y = (num_ligne * 30) - self.level_limit
                if sprite == 'm':
                    level.append([spritelist.GRASS_MIDDLE, x, y])
                if sprite == 'i':
                    level.append([spritelist.STONE_PLATFORM_MIDDLE, x, y])
                if sprite == 'h':
                    decor.append([spritelist.ECHELLE, x, y])
                if sprite == 'a':
                    decor.append([spritelist.EXIT, x, y])
                    sortie.append([spritelist.EXIT, x, y])
                if sprite == 'd':
                    decor.append([spritelist.START, x, y])
                    self.start.append(x)
                    self.start.append(y)
                if sprite == 't':
                    move.append([spritelist.STONE_PLATFORM_MIDDLE, x, y, 1])
                if sprite == 's':
                    move.append([spritelist.STONE_PLATFORM_MIDDLE, x, y, 2])
                if sprite == 'e':
                    enemis.append([x, y, 1])
                if sprite == 'y':
                    enemis.append([x, y, 2])
                if sprite == 'l':
                    obstacles.append([spritelist.LAVE, x, y])
                num_case += 1
            num_ligne += 1

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            # block.player = self.player
            self.platform_list.add(block)

        for element in decor:
            block = platforms.Platform(element[0])
            block.rect.x = element[1]
            block.rect.y = element[2]
            self.decor_list.add(block)

        for sorti in sortie:
            block = platforms.Platform(sorti[0])
            block.rect.x = sorti[1]
            block.rect.y = sorti[2]
            self.exit.add(block)

        for perso in enemis:
            if perso[2] == 1:
                aleatoire = choice(spritelist.enemisterrain)
                enemi = Enemi1(aleatoire)
                # enemi.rect.x = perso[0]
                # enemi.rect.y = perso[1]
                enemi.level = self

            if perso[2] == 2:
                aleatoire = choice(spritelist.enemisvolants)
                enemi = Enemi2(aleatoire)
                # enemi.rect.x = perso[0]
                # enemi.rect.y = perso[1]
                # enemi.level = self
            enemi.rect.x = perso[0]
            enemi.rect.y = perso[1]
            enemi.level = self
            self.enemy_list.add(enemi)

        for obstacle in obstacles:
            block = platforms.Platform(obstacle[0])
            block.rect.x = obstacle[1]
            block.rect.y = obstacle[2]
            self.obstacles_list.add(block)

        for platform in move:
            block = platforms.MovingPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.level = self
            if platform[3] == 1:
                block.change_x = 1
                block.boundary_left = platform[1] - 100
                block.boundary_right = platform[1] + 100
            elif platform[3] == 2:
                block.change_y = -1
                block.boundary_top = block.rect.y - 50
                block.boundary_bottom = block.rect.y + 50
            block.player = self.player
            self.platform_list.add(block)
