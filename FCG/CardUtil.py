import random
import colors

all_cards_available = \
    [
        "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "0S", "jS", "qS", "kS", "aS",
        "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "0H", "jH", "qH", "kH", "aH",
        "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "0C", "jC", "qC", "kC", "aC",
        "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "0D", "jD", "qD", "kD", "aD",
    ]

card_color = \
    {
        'S': colors.BLACK,
        'C': colors.BLACK,
        'H': colors.RED,
        'D': colors.RED
    }


def get_random_card():
    random.shuffle(all_cards_available)
    card = all_cards_available[0]
    all_cards_available.remove(card)
    return card

def get_top_cards(num):
    arr = []
    for i in range(num):
        card = all_cards_available[0]
        all_cards_available.remove(card)
        arr.append(card)
    return arr
