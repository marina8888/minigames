import random


# all cards in this game are split into 1 or more ordered set of cards.
# in cases such as splitting, game requires to work with only the top ordered set
# Stack structure is implemented for all cards including dealer's deck of cards and the player's hands.
# in this case, the number of hands a player has represents the number of elements in a Stack.

# ANYTHING INITIALISED DOESN'T NEED TO BE AN ARGUMENT SQUISHY XXXX
# create a class representing a single card which initialises and prints the card
class Card():

    def __init__(self, suit, value, name=None):
        self.name = name
        self.suit = suit
        self.value = value

    def __str__(self):
        if self.name:
            return self.name + " of " + self.suit + " "
        else:
            return str(self.value) + " of " + self.suit + " "


class CardStack():

    def __init__(self):
        self.cards = [[]]

    def __len__(self):
        return len(self.cards)

    # popping an element
    def pop(self):
        if len(self.cards) >= 1:
            return self.cards.pop()
        else:
            raise IndexError

    # appending an element
    def push(self, single_hand_or_deck: [Card]):
        self.cards.append(single_hand_or_deck)


# my cards represent the cards that each player has as a list. The dealer can also access my cards, but deals from deck.
class Player():

    def __init__(self, name, initial_bet=0):
        self.name = name
        self.money_out = self.bet_per_hand = initial_bet
        self.my_cards = CardStack()
        # split function allows player to split their card deck.
        # number_of_hands value signifies how many sets a player has (up to a maximum of three as players cannot split more than twice per game)
        # players who have said no to a split earlier in game cannot split later. Value turns false if player did not want to split earlier in game.
        self.said_split = True
        self.over_twentyone = False

    def get_value(self):
        total_value = 0
        cards = self.my_cards.pop()
        for card in cards:
            total_value += card.value
        if total_value > 21:
            print("card values are over 21, you have lost")
            self.over_twentyone = False
        else:
            print("card values are under 21, you're still in the game")
        self.my_cards.push(cards)
        return total_value

    def check_blackjack(self):
        ace, royal = False, False
        if len(self.my_cards) == 2:
            for card in self.my_cards:
                if card.name == 'Ace':
                    ace = True
                if card.name in ["Queen", "King", "Jack"]:
                    royal = True
        if ace and royal:
            print("You've won blackjack")
            player_wins_cash = self.bet_per_hand * 1.5
            return player_wins_cash

    def decide_ace_value(self, ace_value=1):
        if ace_value not in [1, 11]:
            print("Invalid ace value")
        for card in self.self.my_cards:
            if card.name == "Ace":
                card.value = ace_value
            else:
                print("No Aces in the set")

    def not_split(self):
        print("This player will not be able to split in the future")
        return False

    def split(self):
        old_hand = []
        new_hand=[]
        if self.said_split == True and len(self.my_cards)<4:
            old_hand=self.my_cards.pop()
            if old_hand[-1]==old_hand[-2]:
                new_hand=old_hand[-1].pop()
                self.my_cards.push(old_hand)
                self.my_cards.push(new_hand)
            else:
                print("no identical last cards for splitting")
        else:
            print('cannot split cards because said no to splitting earlier in game')

        # after inital deal or after the first two cards of any split pair, if the cards have a hard total of 9, 10 or 11,
        # the player can choose to only have one more card played to them and to double their wager

    def double_down(self, dealer_deck: [Card]):
        self.money_out = self.bet_per_hand * 2
        self.my_cards.append(dealer_deck.pop)
        return self.my_cards

    def money_money_money(self, dealer):
        if self.get_value(dealer.deck) > self.get_value(self.my_cards):
            winning_money = dealer.bet_per_hand * 2
            print("Dealer wins " + str((dealer.bet_per_hand * 2)))
            return winning_money


class Dealer(Player):

    def __init__(self, name, intial_bet=0, number_of_decks=1):
        super().__init__(name,initial_bet=intial_bet)
        self.number_of_decks = number_of_decks
        self.deck = self.create_deck(self.number_of_decks)
        self.shuffle()

    # creating a card_deck stack of single_decks (each containing 52 cards)
    def create_deck(self, deck_multiplier):
        single_deck=[]
        for x in range(1, deck_multiplier + 1, 1):
            for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
                single_deck.append(Card(suit, 1, name="Ace"))
                for royal in ["Jack", "Queen", "King"]:
                    single_deck.append(Card(suit, 10, name=royal))
                for i in range(1, 11, 1):
                    single_deck.append(Card(suit, i))
        return single_deck

    # must shuffle all decks together (not just a single deck)
    def shuffle(self):
        random.shuffle(self.deck)

    def hit_me_daddy(self, player: Player):
        card = self.deck.pop()
        player_cards=player.my_cards.pop()
        player_cards.append(card)
        player.my_cards.push(player_cards)
        print("player was dealt: " + str(card))
        player.get_value()

    def inital_deal(self, player: Player):
        card = self.deck.pop()
        player_cards=player.my_cards.pop()
        player_cards.append(card)
        print("player was dealt: " + str(card))
        card = self.deck.pop()
        player_cards.append(card)
        print("player was dealt: " + str(card))
        player.my_cards.push(player_cards)
        player.check_blackjack()
