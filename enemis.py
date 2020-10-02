# -*- coding: utf-8 -*-
# @Author: apyju
# @Date:   2018-11-28 09:45:46
# @Last Modified by:   apyju
# @Last Modified time: 2018-12-23 12:48:57
import pygame
from pygame.locals import *
from spritesheet import SpriteSheet
from constantes import *
from spritelist import *


class Perso(pygame.sprite.Sprite):
    # level = None
    vie = 5
    force = 0
    speed = 1

    def __init__(self, *personnage):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet(img_enemis, BLUE2)

        self.personnage = []
        self.walking_frames_r = []
        self.walking_frames_l = []
        self.level = None

        # affichage
        for img in personnage:
            image = sprite_sheet.get_image(*img)
            self.walking_frames_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)

        self.index = 0
        self.images = self.walking_frames_r
        self.image = self.walking_frames_r[self.index]
        self.rect = self.image.get_rect()
        self.animation_time = 150
        self.current_time = 0
        self.direction = 1

        # déplacements
        self.vx = 0
        self.vy = 0

    def update(self, dt):
        self.move()
        # self.calc_grav()

        dt_sec = dt / 17
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = self.index
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.x += self.vx
        # ne pas sortir de l'écran
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.direction *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction *= -1
        # See if we block_hit_listhit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.vx < 0:
                self.rect.left = block.rect.right
                self.direction *= -1
            elif self.vx > 0:
                self.rect.right = block.rect.left
                self.direction *= -1

        self.rect.y += self.vy
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.vy > 0:
                self.rect.bottom = block.rect.top
            elif self.vy < 0:
                self.rect.top = block.rect.bottom
            self.vy = 0

    def _update_frame(self):
        if self.vx > 0:
            self.images = self.walking_frames_r
        elif self.vx < 0:
            self.images = self.walking_frames_l

    # def calc_grav(self):
    #     """calculate effect of gravity. """
    #     if self.vy == 0:
    #         self.vy = 1
    #     else:
    #         self.vy += .35


class Enemi1(Perso):

    def __init__(self, personnage):
        # personnage = enemi1
        Perso.__init__(self, *personnage)

    def move(self):
        # on calcule la gravité ici
        if self.vy == 0:
            self.vy = 1
        else:
            self.vy += .35

        # regarder s'il a un sol
        self.rect.x += 2 * self.direction
        self.rect.y += 2
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
        self.rect.x -= 2 * self.direction

        # s'il y a un sol il avance sinon il se retourne
        if len(block_hit_list) > 0:
            self.vx = self.direction * self.speed
        else:
            self.direction *= -1
            self.vx = self.direction * self.speed
        self._update_frame()


class Enemi2(Perso):

    def __init__(self, personnage):
        # personnage = enemivolant1
        Perso.__init__(self, *personnage)

    def move(self):
        # regarder son positionnement vs le player
        dir = 0
        signe = self.level.player.rect.y - self.rect.y
        signe2 = self.level.player.rect.x - self.rect.x

        # si le player est au dessus ou sur la même ligne on va vers lui
        if self.level.player.rect.y <= self.rect.y:
            if signe > 0:
                dir = 1
            elif signe < 0:
                dir = -1
            elif signe == 0:
                dir = 0

            if signe2 > 0:
                self.direction = 1
            elif signe2 < 0:
                self.direction = -1

        self.vy = dir * self.speed
        self.vx = self.direction * self.speed
        self._update_frame()


# class Enemis(pygame.sprite.Sprite):

#     stand_left = []
#     stand_right = []
#     walking_frames_r = []
#     walking_frames_l = []
#     mourir = []
#     level = None

#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)

#         sprite_sheet = SpriteSheet(img_enemis, BLUE2)

#         # # image fixe
#         # image = sprite_sheet.get_image(*enemivolant1[0])
#         # self.stand_right.append(image)
#         # image = pygame.transform.flip(image, True, False)
#         # self.stand_left.append(image)

#         for img in enemivolant1:
#             image = sprite_sheet.get_image(*img)
#             self.walking_frames_r.append(image)
#             image = pygame.transform.flip(image, True, False)
#             self.walking_frames_l.append(image)

#         # for img in fumee:
#         #     image = sprite_sheet.get_image(*img)
#         #     self.mourir.append(image)

#         # Set a referance to the image rect.
#         self.index = 0
#         # self.images = self.stand_right
#         self.image = self.walking_frames_r[self.index]
#         self.rect = self.image.get_rect()
#         self.animation_time = 0.15
#         self.current_time = 0
#         self.direction = 1

#         # déplacements
#         self.vx = 0
#         self.vy = 0

#         # autres
#         self.vie = 5
#         self.force = 0
#         self.speed = 1

#     def update(self, dt):
#         self.calc_grav()
#         self.move()

#         # self.rect.update(dt)
#         dt_sec = dt / 1000
#         self.rect.x += self.vx

#         self.current_time += dt_sec
#         if self.current_time >= self.animation_time:
#             self.current_time = 0
#             self.index = self.index
#             self.index = (self.index + 1) % len(self.images)
#             self.image = self.images[self.index]

#         # ne pas sortir de l'écran
#         if self.rect.right > SCREEN_WIDTH:
#             self.rect.right = SCREEN_WIDTH
#             self.direction *= -1
#         if self.rect.left < 0:
#             self.rect.left = 0
#             self.direction *= -1

#         # See if we block_hit_listhit anything
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         for block in block_hit_list:
#             if self.vx < 0:
#                 self.rect.left = block.rect.right
#                 self.direction *= -1
#             elif self.vx > 0:
#                 self.rect.right = block.rect.left
#                 self.direction *= -1

#         self.rect.y += self.vy
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         for block in block_hit_list:
#             if self.vy > 0:
#                 self.rect.bottom = block.rect.top
#             elif self.vy < 0:
#                 self.rect.top = block.rect.bottom
#             self.vy = 0

#     def _update_frame(self):
#         if self.vx > 0:
#             self.images = self.walking_frames_r
#         elif self.vx < 0:
#             self.images = self.walking_frames_l

#     def calc_grav(self):
#         """calculate effect of gravity. """
#         if self.vy == 0:
#             self.vy = 1
#         else:
#             self.vy += .35

#     def move(self):
#         # regarder s'il a un sol
#         self.rect.x += 2 * self.direction
#         self.rect.y += 2
#         block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         self.rect.y -= 2
#         self.rect.x -= 2 * self.direction

#         # s'il y a un sol il avance sinon il se retourne
#         if len(block_hit_list) > 0:
#             self.vx = self.direction * self.speed
#         else:
#             self.direction *= -1
#             self.vx = self.direction * self.speed
#         self._update_frame()
