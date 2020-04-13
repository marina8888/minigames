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


# my cards represent the cards that each player has as a list. The dealer can also access my cards, but deals from deck.
class Player():

    def __init__(self, name, inital_bet=0):
        self.name = name
        self.money_out = self.bet_per_hand = inital_bet
        self.my_cards = []

        # split function allows player to split their card deck.
        # number_of_hands value signifies how many sets a player has (up to a maximum of three as players cannot split more than twice per game)
        # players who have said no to a split earlier in game cannot split later. Value turns false if player did not want to split earlier in game.
        self.number_of_hands = 1
        self.said_split = True
        self.over_twentyone = False

    def get_value(self, player_deck: [Card]):
        total_value = 0
        for card in player_deck:
            total_value += card.value
            if total_value > 21:
                print("card values are over 21, you have lost")
                # self.freeze()
                self.over_twentyone = True
            else:
                print("card values are under 21, you're still in the game")
        return total_value

    def check_blackjack(self, player_deck: [Card]):
        ace, royal = False, False
        if len(player_deck) == 2:
            for card in player_deck:
                if card.name == 'Ace':
                    ace = True
                if card.name in ["Queen", "King", "Jack"]:
                    royal = True
        if ace and royal:
            print("You've won blackjack")
            player_wins_cash = self.bet_per_hand * 1.5
            # self.freeze()
            return player_wins_cash

    def inital_deal(self, dealer_deck: [Card], player_deck: [Card]):
        player_deck.append(dealer_deck.pop)
        player_deck.append(dealer_deck.pop)
        print([card.__str__() for card in player_deck])
        return player_deck

    def hit(self, dealer_deck: [Card], player_deck: [Card]):
        player_deck.append(dealer_deck.pop)
        print([card.__str__() for card in player_deck])
        return player_deck

    def stay(self, player_deck: [Card], ace_value=1):
        if ace_value not in [1, 11]:
            print("Invalid ace value")
        for card in player_deck:
            if card.name == "Ace":
                card.value = ace_value
            else:
                print("No Aces in the set")

    def not_split(self):
        print("This player will not be able to split in the future")
        return False

    def split(self, player_deck: [Card]):
        if self.said_split == True:
            if player_deck[-1] == player_deck[-2]:
                self.number_of_hands += 1
                split_my_cards, split2_my_cards = [], []
                if self.number_of_hands == 2:
                    split_my_cards = split_my_cards.append(player_deck.pop())
                    return split_my_cards
                if self.number_of_hands == 3:
                    split2_my_cards = split2_my_cards.append(split_my_cards.pop())
                    return split2_my_cards
            else:
                print("no identical last cards for splitting")
        else:
            print("cannot split cards because said no to splitting earlier in game")

        # after inital deal or after the first two cards of any split pair, if the cards have a hard total of 9, 10 or 11,
        # the player can choose to only have one more card played to them and to double their wager

    def double_down(self, dealer_deck: [Card], player_deck: [Card]):
        self.money_out = self.bet_per_hand * 2
        player_deck.append(dealer_deck.pop)
        return player_deck

    def money_money_money(self, dealer, player_deck: [Card]):
        if self.get_value(dealer.deck) > self.get_value(player_deck):
            winning_money = dealer.bet_per_hand * 2
            print("Dealer wins " + str((dealer.bet_per_hand * 2)))
            return winning_money


class Dealer(Player):

    def __init__(self, name, number_of_decks=1):
        super().__init__(name)
        self.number_of_decks = number_of_decks
        self.deck = self.create_deck(self.number_of_decks)
        self.deck = shuffle(self.deck)
        self.last_card = self.pop_card(self.deck)

    def create_deck(self, deck_multiplier):
        card_deck = []
        for x in range(1, deck_multiplier + 1, 1):
            for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
                card_deck.append(Card(suit, 1, name="Ace"))
                for royal in ["Jack", "Queen", "King"]:
                    card_deck.append(Card(suit, 10, name=royal))
                for i in range(1, 11, 1):
                    card_deck.append(Card(suit, i))
        return card_deck

    def shuffle(self, cards_to_shuffle):
        shuffle(cards_to_shuffle)
        return cards_to_shuffle


Marina = Dealer(marina, )
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
