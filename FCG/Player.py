import math

import numpy
import pygame

from Scripts import collision_all
from objects import Bullet


class Player:

    def __init__(self, game_display, speed, size, color, level):
        self.x = 10
        self.y = 10
        self.game_display = game_display
        self.speed = speed
        self.size = size
        self.color = color
        self.level = level
        self.x_speed = 0
        self.y_speed = 0
        self.last_keys = {"UP":False, "DOWN":False}
        self.frame_keys = {"UP":True, "DOWN":True}

    def move(self):
        # key managment
        k = pygame.key.get_pressed()
        # keys which are pressed only at this frame
        self.frame_keys["UP"] = (k[pygame.K_UP] or k[pygame.K_w]) and not self.last_keys["UP"]
        self.frame_keys["DOWN"] = (k[pygame.K_DOWN] or k[pygame.K_s]) and not self.last_keys["DOWN"]

        # the keys which are pressed last frame
        self.last_keys["UP"] = k[pygame.K_UP] or k[pygame.K_w]
        self.last_keys["DOWN"] = k[pygame.K_DOWN] or k[pygame.K_s]

        # horizontal speed & movement
        self.x_speed = 0
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            self.x_speed += self.speed
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            self.x_speed -= self.speed

        # vertical speed: jump & fall
        if collision_all(self, self.level.platforms, 0, 1) and not collision_all(self, self.level.platforms):
            if self.frame_keys["UP"]:
                self.y_speed = -12
            if self.frame_keys["DOWN"]:
                self.y_speed = 1
        else:
            self.y_speed += 1

        # shoot bullet
        if pygame.mouse.get_pressed()[0]:
            self.shoot()

    def collisions(self):
        # key managment
        k = pygame.key.get_pressed()

        # x collision
        if collision_all(self, self.level.platforms, self.x_speed, 0):
            while not (collision_all(self, self.level.platforms, numpy.sign(self.x_speed), 0)):
                self.x += numpy.sign(self.x_speed)
            self.x_speed = 0

        # x movement
        self.x += self.x_speed

        # y collision
        if (not self.frame_keys["DOWN"]) and (self.y_speed > 0):
            if collision_all(self, self.level.platforms, 0, self.y_speed) and not collision_all(self,
                                                                                                self.level.platforms):
                while not (collision_all(self, self.level.platforms, 0, numpy.sign(self.y_speed))):
                    self.y += numpy.sign(self.y_speed)
                self.y_speed = 0

        # y movement
        self.y += self.y_speed

    def shoot(self):
        mouse_coordinates = pygame.mouse.get_pos()
        mouse_x = mouse_coordinates[0]
        mouse_y = mouse_coordinates[1]
        angle_to_go = math.atan2(mouse_y - self.y, mouse_x - self.x)
        self.level.bullets.append(Bullet.Bullet(self.game_display, self, angle_to_go, 2))

    def draw(self):
        pygame.draw.rect(self.game_display, self.color, [self.x, self.y, self.size, self.size])
