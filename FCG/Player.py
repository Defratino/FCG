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
        k = pygame.key.get_pressed()
        if k[pygame.K_RIGHT] or k[pygame.K_d]:
            self.x += self.speed
        if k[pygame.K_LEFT] or k[pygame.K_a]:
            self.x -= self.speed

        if k[pygame.K_UP] or k[pygame.K_w]:
            self.y -= self.speed
        if k[pygame.K_DOWN] or k[pygame.K_s]:
            self.y += self.speed

    def draw(self):
        pygame.draw.rect(self.game_display, self.color, [self.x, self.y, self.size, self.size])
