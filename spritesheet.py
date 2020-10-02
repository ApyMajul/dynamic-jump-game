# -*- coding: utf-8 -*-
# @Author: apyju
# @Date:   2018-11-27 18:13:19
# @Last Modified by:   apyju
# @Last Modified time: 2018-11-27 18:15:15
import pygame


class SpriteSheet(object):
    """Class used to grab images out of a sprite sheet."""
    # This point to our sprite sheet image
    sprite_sheet = None

    def __init__(self, file_name, COLOR, size=0):
        """Pass in the file name of the sprite sheet. """
        # load the sprite sheet
        self.COLOR = COLOR
        self.size = size
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        """Grab a single image out of a larger SpriteSheet
        passs in the x, y location of the sprite
        and the widht and height of the sprite """

        # create a new blank image
        image = pygame.Surface([width, height]).convert()

        # copy the sprite from the large sheet into the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # assuming black works as the trasnparent color
        image.set_colorkey(self.COLOR)

        if self.size != 0:
            image = pygame.transform.scale(image, (self.size, self.size))

        return image
