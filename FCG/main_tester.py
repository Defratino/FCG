import pygame
import Player

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

p1 = Player.Player(game_display, 3, 10, (23, 102, 67))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # start event

    p1.move()

    # end event

    game_display.fill((10, 240, 220))

    # start draw

    p1.draw()

    # end draw

    dtime = clock.tick(FPS)
    pygame.display.update()
