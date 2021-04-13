import random

class Card:

    """
    The Card class represents a single playing card and is initialised by passing a suit and number.
    """

    def __init__(self, suit, number):
        self._suit = suit
        self._number = number

    def __repr__(self):
        return self._number + " of " + self._suit

    def move(self, origin, destination):
        if self in origin:
            posOrigin = origin.index(self)
            origin.pop(posOrigin)
            destination.insert(0,self)
        else:
            print(str(self) + " is not in " + str(origin))

    @property
    def suit(self):

        """
        Gets or sets the suit of a card
        """

        return self._suit

    @suit.setter
    def suit(self, suit):
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    @property
    def number(self):
        """
        Gets or sets the number of a card
        """
        return self._number

    @number.setter
    def number(self, number):
        valid = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        if number in valid:
            self._number = number
        else:
            print("That's not a valid number")


class Deck:

    """
    The Deck class represents a deck of playing cards in order.
    """

    def __init__(self):
        self._cards = []
        self.populate()

    @property
    def cards(self):
        return self._cards

    def populate(self):

        """
        The populate method fills the deck with cards in order
        """

        suits = ["hearts", "clubs", "diamonds", "spades"]
        numbers = [str(n) for n in range(2,11)] + ["J", "Q", "K", "A"]
        self._cards = [ Card(s, n) for s in suits for n in numbers ]

    def shuffle(self):

        """
        The shuffle method sorts the code within the deck into a random order
        """

        random.shuffle(self._cards)

    def deal(self, hand):

            """
            The deal method automaticaly adds a single card to an array that is specified within the code
            """

            dealt_card = self._cards.pop(0)
            hand._cards.append(dealt_card)

    def __repr__(self):
        cards_in_deck = len(self._cards)
        return "Deck of " + str(cards_in_deck) + " cards"

class Hand:

    """
    The Hand class represents a hand of playing cards held by a single player in a typical card game.
    """

    def __init__(self):
        self._cards = []

    @property
    def cards(self):
        return self._cards

    def __repr__(self):
        i = 1
        rep = ""
        for card in self._cards:
            rep = rep+str(i)+". "+str(card)+"\n"
            i += 1
        return rep

class Discard_Pile:

    """
    The Discard_Pile class represents a discard pile in a card game.
    """

    def __init__(self):
        self._discard_pile = []

    @property
    def cards(self):
        return self._discard_pile

    def discard(self, hand, card_number):

        """
        The discard method moves a card from a hand into a seperate list
        """

        discarded_card = hand._cards.pop(0)
        self._discard_pile.append(self._discard_pile)

    def get_face_card(self):

        """
        The get_face_card method retrieves the first card from the discard pile list
        """

        face_discard_card = self._discard_pile[0]
        return face_discard_card

    def __repr__(self):
        return str(self._discard_pile)
