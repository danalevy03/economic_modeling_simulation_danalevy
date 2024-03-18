class Card:
    SUITS = ["♣","♦","♥","♠"]
    RANKS = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

    def __init__(self, suit, rank):
        if suit not in self.SUITS:
            raise Exception(f"Invalid suite. Allowed suites are: {self.SUITS}")
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank. Allowed ranks are: {self.RANKS}")
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    #need to be able to print the card!
    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                cards.append(Card(suit=suit, rank=rank))
        self._cards = cards

    @property
    def cards(self):
        return self._cards



card = Card("♣", "A")
print(card)
card2 = Card("♦", "10")
print(card2)
card3 = Card(rank="K", suit="♠")
print(card3)
