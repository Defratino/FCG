import pygame
import CardUtil


class Platform:
    def __init__(self, game_display, x, y, width, height, level):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.game_display = game_display
        self.color = CardUtil.card_color[level.symbol]
        level.platforms.append(self)

    def draw(self):
        pygame.draw.rect(self.game_display,
                         self.color,
                         [self.x, self.y, self.width, self.height])
