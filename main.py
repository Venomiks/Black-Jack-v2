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

class Opponent(Cards):

    cards_in_hand_2 = [random.choice(cards.play), random.choice(cards.play)]
    print(f'oponents cards: {cards_in_hand_2[0]} {cards_in_hand_2[1]}')

    sum_of_cards_2 = sum(cards_in_hand_2)

opponent = Opponent()


deck = []

#iterating through cards and modifying deck
for i in cards.cards_in_hand:
    if i == 11 or i == 1:
        deck.append('ace')
    elif i == 10:
        deck.append(random.choice(cards.tens))
    else:
        deck.append(i)



def cards_in_play():
    # summing the cards value
    sum_of_cards = sum(cards.cards_in_hand)
    print(f'your cards: {deck[0]} {deck[1]}')

    # checking the sum of cards in hand, if it reaches over 21 then you lose
    if opponent.sum_of_cards_2 < sum_of_cards:
        print("you win")
    elif sum_of_cards > 21:
        print("you win")
    else:
        print("you lose")

    print(f'sum of your cards is: {sum_of_cards}')

cards_in_play()
