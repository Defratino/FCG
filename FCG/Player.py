import pygame
import numpy
from Scripts import collision_all

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

    def move(self):
        k = pygame.key.get_pressed()
        self.x_speed = 0
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            self.x_speed += self.speed
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            self.x_speed -= self.speed

        if collision_all(self, self.level.platforms, 0, 1) and not collision_all(self, self.level.platforms):
            self.y_speed = 0
            if k[pygame.K_UP] or k[pygame.K_w]:
                self.y_speed = -12
            if k[pygame.K_DOWN] or k[pygame.K_s]:
                self.y_speed = 1
        else:
            self.y_speed += 1

    def collisions(self):
        k = pygame.key.get_pressed()

        # x collision
        if collision_all(self, self.level.platforms, self.x_speed, 0):
            while not(collision_all(self, self.level.platforms, numpy.sign(self.x_speed), 0)):
                self.x += numpy.sign(self.x_speed)
            self.x_speed = 0

        # x movement
        self.x += self.x_speed

        # y collision
        if not(k[pygame.K_DOWN] or k[pygame.K_s]) and self.y_speed > 0:
            if collision_all(self, self.level.platforms, 0, self.y_speed) and not collision_all(self, self.level.platforms):
                while not(collision_all(self, self.level.platforms, 0, numpy.sign(self.y_speed))):
                    self.y += numpy.sign(self.y_speed)
                self.y_speed = 0

        # y movement
        self.y += self.y_speed


    def draw(self):
        pygame.draw.rect(self.game_display, self.color, [self.x, self.y, self.size, self.size])
