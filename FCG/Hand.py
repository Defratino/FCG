import pygame

class Hand:

    def __init__(self, game_display, cards):
        self.cards = cards
        self.game_display = game_display

    def draw(self):
        for i in range(len(self.cards)):
            pygame.draw.rect(self.game_display, (0,0,0), [i * 70 + 20, 500, 50, 70])