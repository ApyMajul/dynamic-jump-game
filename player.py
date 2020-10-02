# -*- coding: utf-8 -*-
# @Author: apyju
# @Date:   2018-11-27 18:08:53
# @Last Modified by:   apyju
# @Last Modified time: 2018-12-22 12:12:15
import pygame
from pygame.locals import *
from spritelist import *
from spritesheet import SpriteSheet
from platforms import MovingPlatform


class Player(pygame.sprite.Sprite):

    stand_left = []
    stand_right = []
    monte_r = []
    monte_l = []
    tombe_r = []
    tombe_l = []
    walking_frames_r = []
    walking_frames_l = []
    damage_r = []
    damage_l = []
    attack_r = []
    attack_l = []
    direction = "R"
    level = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet(kakashi, GREEN)

        # image fixe
        image = sprite_sheet.get_image(*walk[5])
        self.stand_right.append(image)
        image = pygame.transform.flip(image, True, False)
        self.stand_left.append(image)

        # tombe
        image = sprite_sheet.get_image(*jump[0])
        self.tombe_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.tombe_l.append(image)

        # monte
        image = sprite_sheet.get_image(*jump[1])
        self.monte_r.append(image)
        image = pygame.transform.flip(image, True, False)
        self.monte_l.append(image)

        # image pour la marche
        for img in walk:
            image = sprite_sheet.get_image(*img)
            self.walking_frames_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.walking_frames_l.append(image)

        # image pour l'attaque
        for img in attack:
            image = sprite_sheet.get_image(*img)
            self.attack_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.attack_l.append(image)

        # image pour damage
        for img in damage:
            image = sprite_sheet.get_image(*img)
            self.damage_r.append(image)
            image = pygame.transform.flip(image, True, False)
            self.damage_l.append(image)

        # Set the image the player starts with
        self.index = 0
        self.images = self.stand_right
        self.image = self.stand_right[self.index]

        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(0, 0, 34, 67)
        self.animation_time = 150
        self.current_time = 0

        # déplacements
        self.vx = 0
        self.vy = 0

        # autre
        self.vie = 15
        self.attaque = 0
        self.damage = 0
        self.doublejump = 0

    def draw(self, surface):
        # mettre à jour la taille de l'image
        draw_rect = pygame.Rect(self.rect.x, self.rect.y + (self.rect.height -
                                                            self.image.get_height()), self.image.get_width(), self.image.get_height())
        surface.blit(self.image, draw_rect)

    def update(self, dt):
        self.calc_grav()

        # self.rect.update(dt)
        # dt_sec = pygame.time.Clock().tick(60)
        dt_sec = dt / 100
        self.rect.x += self.vx
        # pos = self.rect.y + self.level.world_shift

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = self.index
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        # See if we block_hit_listhit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.vx < 0:
                self.rect.left = block.rect.right
            elif self.vx > 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.right = block.rect.left

        self.rect.y += self.vy
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.vy > 0:
                self.rect.bottom = block.rect.top
            elif self.vy < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.vy = 0
            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
            self._update_frame()

        obstacles_list = pygame.sprite.spritecollide(self, self.level.obstacles_list, False)
        for obstacle in obstacles_list:
            self.vie -= 5

        # lorsqu'on cogne un enemi
        hit_list = pygame.sprite.spritecollide(self, self.level.enemy_list, False)
        for enemy in hit_list:
            if self.attaque == 1:
                enemy.vie -= 15

            elif self.attaque == 0:
                self.vie -= 1
                if enemy.direction < 0:
                    self.rect.left = enemy.rect.right
                    self.damage += 1
                    self.rect.x -= 150

                elif enemy.direction > 0:
                    self.rect.right = enemy.rect.left
                    self.damage -= 1
                    self.rect.x += 150

            self._update_frame()

    def react(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.attaque = 1
                elif event.key == K_LEFT:
                    self.vx -= 2
                    self.direction = "L"
                elif event.key == K_RIGHT:
                    self.vx += 2
                    self.direction = "R"
                elif event.key == K_UP:
                    self.jump()

                self._update_frame()

            elif event.type == KEYUP:
                if event.key == K_LEFT:
                    self.vx += 2
                elif event.key == K_RIGHT:
                    self.vx -= 2

                self._update_frame()

    def _update_frame(self):

        # self.rect.width = self.image.get_width()
        # self.rect.height = self.image.get_height()

        if self.attaque > 0 and self.direction == "R":
            self.images = self.attack_r
            if self.index == 5:
                self.attaque = 0
        elif self.attaque > 0 and self.direction == "L":
            self.images = self.attack_l
            if self.index == 5:
                self.attaque = 0

        elif self.damage > 0:
            self.images = self.damage_r
            if self.index == 5:
                self.damage = 0
        elif self.damage < 0:
            self.images = self.damage_l
            if self.index == 5:
                self.damage = 0

        elif self.vy < 0 and self.direction == "R":
            self.images = self.tombe_r
        elif self.vy < 0 and self.direction == "L":
            self.images = self.tombe_l

        elif self.vy > 0 and self.direction == "R":
            self.images = self.monte_r
        elif self.vy > 0 and self.direction == "L":
            self.images = self.monte_l

        elif self.vx > 0:
            self.images = self.walking_frames_r
        elif self.vx < 0:
            self.images = self.walking_frames_l

        elif self.vx == 0 and self.vy == 0 and self.direction == "R":
            self.images = self.stand_right
        elif self.vx == 0 and self.vy == 0 and self.direction == "L":
            self.images = self.stand_left

    def calc_grav(self):
        """calculate effect of gravity. """
        if self.vy == 0:
            self.vy = 1
        else:
            self.vy += .35

        # see if we are on the ground
        if self.rect.y >= zdj_height - self.rect.height and self.vy >= 0:
            self.vy = 0
            self.rect.y = zdj_height - self.rect.height
            self._update_frame()

    def jump(self):
        """ Called when user hits 'jump' button. """
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0:
            # or self.rect.bottom >= zdj_height:
            self.vy -= 7
            self.doublejump = 1
        elif self.vy < 0 and self.doublejump < 2:
            self.vy = -7
            self.doublejump += 1
