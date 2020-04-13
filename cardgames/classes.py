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

#my cards represent the cards that each player has as a list. The dealer can also access my cards, but deals from deck.
class Player():

    def __init__(self, name, inital_bet=0):
        self.name = name
        self.bet=inital_bet
        self.my_cards = []

        # split function allows player to split their card deck.
        # number_of_hands value signifies how many sets a player has (up to a maximum of three as players cannot split more than twice per game)
        # players who have said no to a split earlier in game cannot split later. Value turns false if player did not want to split earlier in game.
        self.number_of_hands = 1
        self.said_split = True

    def pop_card(self, Dealer_deck, my_cards):
        last_card = Dealer_deck.pop()
        return my_cards.append(last_card)

    def inital_deal(self,  Dealer_deck, my_cards):
        my_cards= self.pop_card(Dealer_deck, my_cards)
        my_cards = self.pop_card(Dealer_deck, my_cards)
        return my_cards

    def hit(self, Dealer_deck, my_cards):
        return self.pop_card(Dealer_deck, my_cards)

    def stay(self):
            pass

    def split(self):
        if my_cards

    def win_or_loose(self):
        pass

    #after inital deal or after the first two cards of any split pair, if the cards have a hard total of 9, 10 or 11,
    # the player can choose to only have one more card played to them and to double their wager
    def double_down(self):
        pass

class Dealer(Player):

    def __init__(self, name, number_of_decks=1):
        super().__init__(name)
        self.number_of_decks = number_of_decks
        self.deck = self.create_deck(self.number_of_decks)
        self.deck = self.shuffle(self.deck)
        self.last_card=self.pop_card(self.deck)

    def create_deck(self, number_of_decks):
        card_deck = []
        for x in range (1, number_of_decks+1, 1):
            for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
                for royal in ["Jack", "Queen", "King"]:
                    card_deck.append(Card(suit, 10, name=royal))
                for i in range(1, 11, 1):
                    card_deck.append(Card(suit, i))
        return card_deck

    @staticmethod
    def shuffle(cards_to_shuffle):
        shuffle(cards_to_shuffle)
        return cards_to_shuffle

    def pay_to_player(self):
        pass

    def pay_to_self(self):

Marina=Dealer(marina,)
print()

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