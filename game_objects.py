"""
The game objects module to provide Blackjack game.
"""


import random
from bet_exception import BetException


class Chips:
    """Managing chips and bets."""

    min_bet = 25
    max_bet = 1000

    def __init__(self):
        self.total = 100  # total amount of money points
        self.bet = 0

    def win_bet(self):
        """Adding win bet to user's total amount."""
        self.total += self.bet

    def lose_bet(self):
        """Subtracting lost bet from user's total amount."""
        self.total -= self.bet

    def set_bet(self, bet):
        """Set user given bet."""
        if bet < self.min_bet or bet > self.max_bet:
            raise BetException('Given bet value is not in the range between 25 and 1000.')
        if bet > self.total:
            raise BetException(f"Sorry, you don't have enough chips points - {self.total} total.")
        self.bet = bet


class Card:
    """Managing players' cards objects."""

    suit = ''
    rank = ''

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

    def get_suit(self):
        """Get a card suit."""
        return self.suit

    def get_rank(self):
        """Get a card rank."""
        return self.rank


class Deck:
    """Cards deck management."""

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
             'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
    deck = []

    def __init__(self):
        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

        self.shuffle()

    def __str__(self):
        return '\n'.join(str(card) for card in self.deck)

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.deck)

    def deal(self):
        """Takes the next card from the deck."""
        return self.deck.pop(0)


class Hand:
    """Player's hands management."""

    values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6,
              'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
              'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
    ace_name = 'Ace'
    win_value = 21

    def __init__(self):
        self.cards = []
        self.value = 0

    def add_card(self, card):
        """Adds the card to the user's hand."""
        self.cards.append(card)
        self.value += self.values[card.rank]

        if card.rank == self.ace_name:
            self.adjust_for_ace()

    def adjust_for_ace(self):
        """Provides points adjustments when the user gets ace."""
        if self.value > self.win_value:
            self.value -= 10


class Player:
    """Player's data management."""

    hand = object
    chips = object

    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.chips = Chips()

    def get_hand(self):
        """Get a player's hand."""
        return self.hand

    def get_chips(self):
        """Get a player's chips."""
        return self.chips
