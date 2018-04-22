import display_constants


class Level:

    def __init__(self, base_card_factor, base_card_symbol):
        self.bullets = []
        self.platforms = []
        self.factor = base_card_factor[0]
        self.symbol = base_card_symbol[1]

    def draw(self):
        for platform in self.platforms:
            platform.draw()

        for bullet in self.bullets:
            bullet.go()
            bullet.draw()

    def clean_up(self): # Cleans all arrays of useless data
        for bullet in self.bullets:
            if 0 > bullet.x > display_constants.DISPLAY_WIDTH:
                self.bullets.remove(bullet)
            elif 0 > bullet.y > display_constants.DISPLAY_HEIGHT:
                self.bullets.remove(bullet)