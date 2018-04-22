import pygame
import math

class Bullet:

    def __init__(self, game_display, origin, direction, size, color = (0, 0, 0)):
        self.game_display = game_display
        self.x = origin.x
        self.y = origin.y
        self.direction = direction
        self.size = size
        self.color = color

    def go(self):
        self.x += math.cos(self.direction) * 5
        self.y += math.sin(self.direction) * 5

    def draw(self):
        pygame.draw.rect(self.game_display, self.color, [self.x, self.y, self.size, self.size])