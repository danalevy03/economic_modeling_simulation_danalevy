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
        cards = tuple(cards)
        self._cards = cards

    def shuffle(self):
        import random
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)
    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

class PokerHand:
    def __init__(self, deck):
        hand = []
        for i in range(5):
            hand.append(deck.cards[i])
        self._hand = hand

    @property
    def hand(self):
        return self._hand


    def __str__(self):
        return str(self.hand)

    @property
    def is_flush(self):
        suit = self.hand[0].suit
        for i in range(1,5):
            if self.hand[i].suit != suit:
                return False
        return True


# calculate the probability of having a flush for 100
i = 0
flushes = 0
while True:
    i += 1
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_flush:
        flushes += 1
        print("Found a flush:")
        print(hand)
        if flushes == 100:
            break

prob = flushes / i * 100
print(f"Probability of having a flush in a poker hand: {prob}%")






