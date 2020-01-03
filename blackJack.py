"""
A Blackjack game using classes
"""

import random

# Constants
suits=["Spades","Hearts","Diamonds","Clubs"]
ranks=[2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

# Variables
players=[]
players_plus_dealer=[]



class Card():
    
    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
        self.is_ace=False
        self.value=self.decide_value(self.rank)
    
    def __repr__(self):
        return str(self.rank)+" of " +self.suit
    
    def decide_value(self,card_rank):
        if type(card_rank) == int:
            return card_rank
        elif card_rank in ["Jack","Queen","King"]:
            return 10
        else:
            self.is_ace=True
            return 11
        
class Deck():
    
    def __init__(self):
        self.cards=[]
        self.populate_deck()#Create a deck of 52 cards
        self.Shuffle_deck()#Shuffle the deck
        
    def __str__(self):
        return "\nThe number of cards left in the deck is: "+str(len(self.cards))
    
    def Shuffle_deck(self):
        """
Shuffles the deck of cards
"""
        random.shuffle(self.cards)
        print("\n A new deck of cards have been created, shuffled, and is ready to deal!")
        
    def populate_deck(self):
        """
Creates the deck of cards
"""
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank,suit))
                
    def give_card(self):
        """
Takes the top card of the deck and returns it
"""
        return self.cards.pop()
                
                
class Hand():
    
    def __init__(self):
        self.holding=[]
        self.value=0
        self.aces=0
        self.busted=False
        
    def add_card(self,to_add):
        """
Takes a card from the deck instance and addds it to this hand
"""
        self.holding.append(to_add)
        self.value += to_add.value
        if to_add.is_ace:
            self.aces += 1
        self.count_hand()
    
    def review_hand(self):
        size=len(self.holding)
        print("\n Cards in hand: \n",size)
        
    def count_hand(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            print("\nHad to take away 10\nNew value is:",self.value)
        elif self.value > 21 and not self.aces:
            self.busted=True
            print(f"\ngame over! Looks like you busted with all your cards adding up to:", self.value)
        
        



class Dealer(Hand):
    

    def __init__(self):
        self.hide_cards=True
        super().__init__()


    def __str__(self):
        while self.hide_cards:
            try:
                return ("\nThe dealer is showing the "+ str(self.holding[1]))
            except:
                return ("\nThe dealer does not have any cards")
        else:
            return ("\n The dealer has "+ str(self.value))


    def deal_cards(self):
        while len(self.holding) <2:
            for player in players_plus_dealer:
                player.add_card(deck.give_card())


class Player(Hand):


    def __init__(self,name,chips=100):
        self.player_name=name
        self.chips=chips
        self.bet=None
        #self.double_down=False

        super().__init__()
    

    def __str__(self):
        """
        prints the players bet and balence, if either is missing it will print what it has
        """
        if self.bet and not self.busted:
            answer=self.player_name+" has a hand value of: "+str(self.value)+"\nThey have "+str(self.chips)+" chips in their possession with a bet of "+str(self.bet)+" on the table"
        if not self.bet and not self.busted:
            answer=self.player_name+" has a hand value of: "+str(self.value)+"\nThey have "+str(self.chips)+" chips in their possession with no chips bet yet"
        if self.busted:
            answer=self.player_name+" has busted this hand with a value of : "+str(self.value)+"\nThey have "+str(self.chips)+" chips left in their possession"
        return  answer


    def actual_game(self):
        """
        Meat and bones where the player is asked to hit, stay, or double down*(to be added after).

        """

    def take_bet(self):
        """
        Takes the players bet, tests it is + int within the range of the players chips. Once checked updates chips and bet with the appropiate amounts 
        """
        wager=0
        chips_actual= self.chips+1
        while wager not in range(1,chips_actual):
            try:
                print(f"\n{self.player_name},\nIt is your turn to place a bet. You can bet up {self.chips} chips.")
                wager=int(input("\nHow many chips do you want to bet?"))
            except:
                print(f"\nYour bet must be between 1 and {self.chips}. Try again and make sure you enter an intiger\n")
                continue
        else:
            self.chips=self.chips-wager
            self.bet=wager


    def return_bet(self):
        """
        ran after all betting rounds to pay off the winner, updates chips and bet with the appropiate amounts 
        """
        pass



def ask_players_playing():
    """
    Asks and returns how many players are going to play
    """
    num_player=0
    while num_player not in range(1,6):
        try:
            num_player=int(input("How many player? There can be between 1 and 5"))

        except:
            print("That is not a valid choice")
            continue
    
    else:
        return num_player
        

def ask_player_name():
    """
Ask and returns player name
    """
    name=input("\nwhat is your name?").lower()
    return name.capitalize()
        
def add_players():
    """
appends players to the list players[]
    """
    num_players=ask_players_playing()
    i=0
    while i < num_players:
        player=Player(ask_player_name())
        players.append(player)
        players_plus_dealer.append(player)
        i += 1

def show_player_values():
    """
prints the card values for all players (Not the dealer)
    """
    for player in players:
        print("\n",player)


def place_bets():
    for player in players:
        player.take_bet()

def main():
    game_on=True
    add_players() #asks how many players and names them
    dealer=Dealer() #creates the dealer
    players_plus_dealer.append(dealer)
    while game_on:
        place_bets()#Ask the Player for their bet #Make sure that the Player's bet does not exceed their available chips
        dealer.deal_cards()
        print(dealer)#Show only one of the Dealer's cards, the other remains hidden
        show_player_values()#Show both of the Player's cards
        #playersRound()#Ask the Player if they wish to Hit, and take another card #If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
        #dealersRound()#If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
        #payDay()#Determine the winner and adjust the Player's chips accordingly
        #playAgain()#Ask the Player if they'd like to play again #This will need to return all the cards to the deck and decide if any players do not have any chips left
        game_on= False

    def current_game():
        """
        Used for replaying game. Does not ask for players names
        """
deck=Deck() #creates the deck
main()