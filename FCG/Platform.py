import pygame
import CardUtil

class Player:

    def __init__(self, game_display,  x, y, length, height, level):
        self.x = 10
        self.y = 10
        self.length = length
        self.height = height
        self.game_display = game_display
        self.color = CardUtil.card_color[level.symbol]

    def draw(self):
        pygame.draw.rect(self.game_display,
                        self.color,
                        [self.x, self.y, self.length, self.height])
