import pygame


class Player:

    def __init__(self, game_display, speed, size, color):
        self.x = 10
        self.y = 10
        self.game_display = game_display
        self.speed = speed
        self.size = size
        self.color = color

    def move(self):
        pass # Add player controller

    def draw(self):
        pygame.draw.rect(self.game_display, self.color, [self.x, self.y, self.size, self.size])
