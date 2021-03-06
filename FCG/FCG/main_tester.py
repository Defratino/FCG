import pygame
import Player
import Level
import Platform
import display_constants

pygame.init()

game_display = pygame.display.set_mode((display_constants.DISPLAY_WIDTH, display_constants.DISPLAY_HEIGHT))
clock = pygame.time.Clock()

l1 = Level.Level('2S', 'kS')
p1 = Player.Player(game_display, 3, 10, (23, 102, 67), l1)
pla1 = Platform.Platform(game_display, 0, 200, 400, 5, l1)
pla2 = Platform.Platform(game_display, 0, 250, 400, 5, l1)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # start event

    p1.move()
    p1.collisions()

    # end event

    game_display.fill((10, 240, 220))

    # start draw

    p1.draw()
    l1.draw()
    pla1.draw()
    pla2.draw()

    # end draw

    # cleanups start
    l1.clean_up()

    dtime = clock.tick(display_constants.FPS)
    pygame.display.update()