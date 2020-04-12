from random import shuffle


# create a class repressenting a single card which initialises and prints the card
class Card():

    def __init__(self, suit, value, name=None):
        self.name = name
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.name:
            return self.name + " of " + self.suit + " "
        else:
            return self.value + " of " + self.suit + " "


class Player():

    def __init__(self, name):
        self.name = name
        self.my_cards = []

    def bet(self):


    def hit(self, card):
        Player.table_deck.append(card)

    def stay(self):
        pass

    def split(self):


class Dealer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.deck = self.create_deck()
        self.deck = self.shuffle()

    @staticmethod
    def create_deck():
        card_deck = []
        for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for royal in ["Jack", "Queen", "King"]:
                card_deck.append(Card(suit, 10, name=royal))
            for i in range(1, 11, 1):
                card_deck.append(Card(suit, i))
        return card_deck

    def shuffle(self):
        shuffle(self.deck)
        return self.deck

    def deal_to_player(self,):
        pass

    def pay_to_player(self):
        pass

    def
    def pay_to_self(self):




    # # I am a getter for the @properties
    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, newname):
    #     self._name = newname
    #
    # @name.deleter
    # def name(self):
    #     del self._name