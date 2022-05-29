import random

# Class for cards and cards generator
class Cards:

    ace = [1, 11]
    ace_random = random.choice(ace)

    king_queen_jack = 10

    play = [1, 2, 3, 4, 5, 6, 7, 8, 9, ace_random, king_queen_jack]

    cards_in_hand = [random.choice(play), random.choice(play)]
    #  opponents cards etc
    opponent = [random.choice(play), random.choice(play)]

cards = Cards()


while True:

    deck = []
    op_deck = []



    #iterating through cards and modifying deck
    for i in cards.cards_in_hand:
        if i == 11 or i == 1:
            deck.append(random.choice(cards.ace))
        elif i == 10:
            deck.append(cards.king_queen_jack)
        else:
            deck.append(i)


    #iterating through cards and modifying deck
    for j in cards.opponent:
        if j == 11 or j == 1:
            op_deck.append(random.choice(cards.ace))
        elif j == 10:
            op_deck.append(cards.king_queen_jack)
        else:
            op_deck.append(j)

    # summing the cards value
    print(f'oponents cards: {op_deck[:]}')
    print(f'your cards: {deck}')

    choice = input("Wanna pick more cards? yes/no")

    # cheking for player to pick more cards
    if choice == "yes":
        deck.append(random.choice(cards.play))
        op_deck.append(random.choice(cards.play))
        print(f'your cards: {deck[:]}')
        print(f'your opponents cards: {op_deck[:]}')
    else:
        pass

    def cards_in_play():
        # checking the sum of cards in hand, if it reaches over 21 then you lose
        if sum(op_deck[:]) < sum(deck[:]) and sum(deck[:]) < 21 or sum(deck[:]) == 21:
            print("you win")
        elif sum(deck[:]) > 21:
            print("you lose")
        else:
            print("you lose")


    cards_in_play()
    answer = input("wanna play again? yes/no: ")

    if answer == 'no':
        break




