from guizero import *
from random import shuffle

'''
GUI to display four hands for playing bridge
'''

# Global lists
PLAYERS = ["North", "East", "South", "West"]
SUIT_SYMBOLS = ["♠", "♥", "♦", "♣"]
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7",
         "6", "5", "4", "3", "2"]

# Global constants
CARDS_PER_DECK = 52
NUM_OF_PLAYERS = len(PLAYERS)
NUM_OF_SUITS = len(SUITS)
CARDS_PER_HAND = CARDS_PER_DECK // NUM_OF_PLAYERS

# Global lists of widgets
txt_suits = []
show_hands = []


def show(hands):
    ptr = 0

    for i in range(NUM_OF_PLAYERS):

        for j in range(NUM_OF_SUITS):
            line = SUIT_SYMBOLS[j] + " "

            for k in range(CARDS_PER_HAND):
                # include only the cards in the suit
                if hands[i][k][1] == SUITS[j]:
                    line += hands[i][k][2] + " "

            txt_suits[ptr].value = line
            ptr += 1


def deal():

    deck = []  # empty deck

    # Initialize deck with integer values
    for card in range(CARDS_PER_DECK):
        # Append card index, card suit, card rank
        deck.append((card, SUITS[card // 13], RANKS[card % 13]))  # append index to the list

    # Shuffle the deck
    shuffle(deck)

    # Create a hand for each player
    north = []
    east = []
    south = []
    west = []

    # Create a list of all the hands
    hands = [east, south, west, north]

    # Deal the deck to the players
    while len(deck) != 0:
        for hand in hands:
            hand.append(deck.pop(0))

    # sort each hand
    for hand in hands:
        hand.sort()

    # Print each hand
    for i in range(len(PLAYERS)):
        print(PLAYERS[i], hands[i])

    show(hands)


def main():
    global show_hands

    window = App(title="Bridge Hands", width=500, height=450, layout="grid")

    # set up column widths
    Text(window, text=" " * 10, grid=[0, 0])
    Text(window, text=" " * 30, grid=[1, 0])
    Text(window, text=" " * 30, grid=[2, 0])
    Text(window, text=" " * 30, grid=[3, 0])

    # Create a box for each hand
    hand_north = Box(window, grid=[2, 0], layout="grid")
    hand_east = Box(window, grid=[3, 1], layout="grid")
    hand_south = Box(window, grid=[2, 2], layout="grid")
    hand_west = Box(window, grid=[1, 1], layout="grid")

    # Create a list of the hands
    show_hands = [hand_north, hand_east, hand_south, hand_west]

    # Put the player's name in each box
    for i in range(NUM_OF_PLAYERS):
        Text(show_hands[i], text=PLAYERS[i], grid=[0, 0])

        # Build a list of text fields for each suit
        spades = Text(show_hands[i], align="left", grid=[0, 1])
        hearts = Text(show_hands[i], align="left", grid=[0, 2])
        diamonds = Text(show_hands[i], align="left", grid=[0, 3])
        clubs = Text(show_hands[i], align="left", grid=[0, 4])

        for each in spades, hearts, diamonds, clubs:
            txt_suits.append(each)

    PushButton(window, text="DEAL", command=deal, grid=[2, 3])

    deal()

    window.display()


main()
