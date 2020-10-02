# -*- coding: utf-8 -*-
# @Author: apyju
# @Date:   2018-11-26 17:36:12
# @Last Modified by:   apyju
# @Last Modified time: 2018-12-14 14:35:52
import pygame
from spritesheet import SpriteSheet
from constantes import *


class Platform(pygame.sprite.Sprite):
    """Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet(elements_decors, BLACK, 30)
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class MovingPlatform(Platform):
    """ This is a fancier platform that can actually move. """
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        """ Move the platform.
            If the player is in the way, it will shove the player
            out of the way. This does NOT handle what happens if a
            platform shoves a player into another object. Make sure
            moving platforms have clearance to push the player around
            or add code to handle what happens if they don't. """

        # Move left/right
        self.rect.x += self.change_x
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        cur_pos = self.rect.y - self.level.world_shift
        if cur_pos > self.boundary_bottom or cur_pos < self.boundary_top:
            self.change_y *= -1

        # cur_pos = self.rect.x - self.level.world_shift
        if self.rect.left < self.boundary_left or self.rect.right > self.boundary_right:
            self.change_x *= -1
