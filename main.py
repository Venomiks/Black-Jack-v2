import random

# Class for cards and cards generator
class Cards:

    ace = [1, 11]
    ace_random = random.choice(ace)

    king_queen_jack = 10

    tens = ["king", "queen", "jack"]

    play = [1, 2, 3, 4, 5, 6, 7, 8, 9, ace_random, king_queen_jack]

    cards_in_hand = [random.choice(play), random.choice(play)]
    #  opponents cards etc
    opponent = [random.choice(play), random.choice(play)]

cards = Cards()

print(f'oponents cards: {cards.opponent[0]} {cards.opponent[1]}')

sum_of_cards_2 = sum(cards.opponent)



deck = []
op_deck = []

#iterating through cards and modifying deck
for i in cards.cards_in_hand:
    if i == 11 or i == 1:
        deck.append('ace')
    elif i == 10:
        deck.append(random.choice(cards.tens))
    else:
        deck.append(i)
print(f'your cards: {deck[:]}')

# summing the cards value
sum_of_cards = sum(deck[0:])
print(f'sum of your cards: {sum_of_cards}')

def cards_in_play():
    # checking the sum of cards in hand, if it reaches over 21 then you lose
    if sum_of_cards_2 < sum_of_cards:
        print("you win")
    elif sum_of_cards == 21:
        print("you win")
    elif sum_of_cards > 21:
        print("you lose")
    # print(f'sum of your cards is: {sum_of_cards}')


# cheking for player to pick more cards
choice = input("Wanna pick more cards? yes/no")
# for j in choice:
if choice == "yes":
    deck.append(random.choice(cards.play))
    print(f'your cards: {deck[0:]}')
    print(f'sum of your cards: {sum(deck)}')
else:
    pass
# print(deck)

cards_in_play()
