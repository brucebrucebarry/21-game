"""
A Blackjack game using classes
"""

import random

# Constants
suits = ["Spades","Hearts","Diamonds","Clubs"]
ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

# Variables
players=[]



class Card():
    
    def __init__(self, rank, suit):
        self.rank= rank
        self.suit= suit
        self.is_ace= False
        self.value= self.decide_value(self.rank)
    
    def __repr__(self):
        return str(self.rank)+" of " +self.suit
    
    def decide_value(self,card_rank):
        if type(card_rank) == int:
            return card_rank
        elif card_rank in ["Jack","Queen","King"]:
            return 10
        else:
            self.is_ace= True
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
        self.holding= []
        self.value= 0
        self.aces= 0
        self.busted= False
        
    def addCard(self,to_add):
        """
Takes a card from the deck instance and addds it to this hand
"""
        self.holding.append(to_add)
        self.value += to_add.value
        if to_add.is_ace:
            self.aces += 1
        self.count_hand()
    
    def review_hand(self):
        size= len(self.holding)
        print("\n Cards in hand: \n",size)
        
    def count_hand(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            print("\nHad to take away 10\nNew value is:",self.value)
        elif self.value > 21 and not self.aces:
            self.busted = True
            print("game over! Looks like you busted with all your cards adding up to:", self.value)
        
        



class Dealer(Hand):
    
    def __init__(self):
        self.hide_cards= True
        super().__init__()

    def __str__(self):
        while self.hide_cards:
            return ("\nThe dealer is showing the "+ str(self.holding[1]))
        else:
            return ("\n The dealer has "+ str(self.value))


class Player(Hand):

    def __init__(self, name, chips= 100):
        self.player_name = name
        self.chips = chips
        self.bet = None
        super().__init__()
    
    def __str__(self):
        if self.bet:
            answer= self.player_name+" has a hand value of: "+str(self.value)+"\nThey have "+str(self.chips)+" chips with a bet of "+str(self.bet)
        else:
            answer= self.player_name+" has a hand value of: "+str(self.value)+"\nThey have "+str(self.chips)+" chips with no monry bet yet"
        return  answer

    def showBet(self):
        """
prints the players bet and balence, if either is missing it will print what it has
        """
        print(f"")

def ask_players_playing():
    """
Asks and returns how many players are going to play
    """

    while True:
        try:
            num_player= int(input("How many player? There can be between 1 and 5"))

        except:
            print("That is not a valid choice")
            continue
    
        return num_player
        
    else:
        print("\nLooks like we already have a full table. No new players will be added and we will continue playing with:")
        show_player_values()
        return 0
        

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

        players.append(Player(ask_player_name()))
        i +=1

def show_player_values():
    """
prints the card values for all players (Not the dealer)
    """
    for player in players:
        print(player)




def main():
    game_on= True
    
    while game_on:
        deck=Deck() #creates the deck
        dealer=Dealer() #creates the dealer
        add_players() #asks how many players and names them
        show_player_values()
        #placeBets() 
#Ask the Player for their bet
#Make sure that the Player's bet does not exceed their available chips
        #openingDeal()
#Deal two cards to the Dealer and two cards to the Player
#Show only one of the Dealer's cards, the other remains hidden
#Show both of the Player's cards
        #playersRound()
#Ask the Player if they wish to Hit, and take another card
#If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
        #dealersRound()
#If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
        #payDay()
#Determine the winner and adjust the Player's chips accordingly
        #playAgain()
#Ask the Player if they'd like to play again
        game_on= False
main()