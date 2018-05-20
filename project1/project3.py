from random import shuffle

CARDS_PER_DECK = 52
PLAYERS = ["East", "South", "West", "North"]
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]
RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7",
         "6", "5", "4", "3", "2"]


def main():
    deck = []    # empty deck

    # Initialize deck with integer values
    for card in range(CARDS_PER_DECK):
        # Append card index, card suit, card rank
        deck.append((card, SUITS[card // 13], RANKS[card % 13]))   # append index to the list

    print(deck)

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


main()
