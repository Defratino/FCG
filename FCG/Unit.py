class Unit:

    def __init__(self, generic_card):
        self.power = generic_card.power
        self.symbol = generic_card.symbol
        self.special = False
        try:
            self.power = int(self.power)
        except ValueError:
            self.special = True
