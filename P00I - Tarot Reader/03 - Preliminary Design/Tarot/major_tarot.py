from collections import namedtuple
from random import sample, randint

Card = namedtuple('Card', ['value', 'suit'])
suits = ['swords', 'wands', 'coins', 'cups']
major = ['The Fool', 'The Magician', 'The High Priestess', 'The Empress', 'The Emperor', 'The Hierophant', 'The Lovers',
         'The Chariot', 'Strength', 'The Hermit', 'Wheel of Fortune', 'Justice', 'The Hanged Man', 'Death',
         'Temperance', 'The Devil', 'The Tower', 'The Star', 'The Moon', 'The Sun', 'Judgement', 'The World']
cards = []

for value in range(0, 22):
    cards.append(Card(value, major[value]))


printing_deck = False
if printing_deck:
    for card in cards:
        if (card.suit in suits):
            print(card.value, 'of', card.suit)
        else:
            print(card.value, 'the ', card.suit)

draw = sample(cards, k=3)

print('Drawing')
for card in draw:
    dir = randint(0, 1)
    if (card.suit in suits):
        print(dir, " - ", card.value, 'of', card.suit)
    else:
        print("{2} - {0} ({1})".format(card.suit, card.value, dir))

