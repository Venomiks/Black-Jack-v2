import random

# Class for cards and cards generator
class Cards:

    ace = [1, 11]
    ace_random = random.choice(ace)

    king_queen_jack = 10

    tens = ["king", "queen", "jack"]

    play = [1, 2, 3, 4, 5, 6, 7, 8, 9, ace_random, king_queen_jack]

    cards_in_hand = [random.choice(play), random.choice(play)]
cards = Cards()


deck = []

#iterating through cards and modifying deck
for i in cards.cards_in_hand:
    if i == 11 or i == 1:
        deck.append('ace')
    elif i == 10:
        deck.append(random.choice(cards.tens))
    else:
        deck.append(i)




# summing the cards value
sum_of_cards = sum(cards.cards_in_hand)
print(deck[0], deck[1])

print(f'your sum of cards is: {sum_of_cards}')