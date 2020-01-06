"""
A Blackjack game using classes
"""

import random
import time

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
        print("\n A new deck of cards have been created")
        
    def __str__(self):
        return "\nThe number of cards left in the deck is: "+str(len(self.cards))
    
    def Shuffle_deck(self):
        """
Shuffles the deck of cards
"""
        random.shuffle(self.cards)
        print("\nThe deck is shuffled and is ready to deal")
        
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
        self.done=False
        
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
        """
        prints number of cards in this hand
        """
        size=len(self.holding)
        print("\n Cards in hand: \n",size)
        
    def count_hand(self):
        """
        Once the players hand goes over 21: if Aces adjusts the hands value, else causes them to bust
        """
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            print("\nThis Ace is worth 1 because you would otherwise bust")
        elif self.value > 21 and not self.aces:
            self.busted=True
            print(f"\n\nLooks like you busted with all your cards adding up to: {self.value}. Here are your cards:", self.holding); time.sleep(1)


    def return_all_cards(self):
        """
        returns the top card in the players hand (mainly used to rest the game for a new turn)
        """
        deck.cards.append(self.holding.pop())


    def reset_values(self):
        """
        resets the values of each hand to allow a new game to be played
        """
        self.value=0
        self.aces=0
        self.busted=False
        self.done=False
        



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


    def play_hand(self):
        self.hide_cards=False
        print(f"\n\nNow that all the players have had their turn it is time for the dealer to play"); time.sleep(2)
        while self.value in range(0,17) and not self.busted:
            print(f"\nThe dealer has a card value of {self.value} and is holding:",self.holding)
            print("\nThis means the dealer must hit until they reach at least 17"); time.sleep(1)
            self.add_card(deck.give_card())
        if self.value in range(17,22):
            print(f"\nThe dealer will stay at {self.value}. They are holding:",self.holding)
            time.sleep(2)


    def count_hand(self):
        """
        Once the players hand goes over 21: if Aces adjusts the hands value, else causes them to bust
        """
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            print("\nAn Ace is now worth 1 because you would otherwise bust")
        elif self.value > 21 and not self.aces:
            self.busted=True
            print(f"\n\n\nThe dealer has busted with all their cards adding up to: {self.value}. Here are your cards:", self.holding); time.sleep(2)


    def reset_values(self):
        """
        resets the values of each hand to allow a new game to be played
        """
        self.value=0
        self.aces=0
        self.busted=False
        self.hide_cards=True

class Player(Hand):


    def __init__(self,name,chips=100):
        self.player_name=name
        self.chips=chips
        self.bet=None
        #self.double_down=False
        super().__init__() #allows inheritance of variables from Hand(class)
    

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


    def select_action(self):
        """
        ASks players if they want to hit or stay *add doubledown later

        returns their response.lower() 
        """
        answer=None
        while answer not in ["hit","stay"]:
            answer= input("Would you like to hit or stay?").lower()
        return answer


    def play_hand(self):
        """
        Meat and bones where the player is asked to hit, stay, or double down*(to be added after).

        """
        while not self.done and not self.busted:
            print("\n",dealer)
            print(f"\n\n{self.player_name} it is your move. Your cards equal a value of {self.value} and are:",self.holding)
            move=self.select_action()
            if move == "hit":
                print("\nGiving you another card")
                self.add_card(deck.give_card())
                if not self.busted:
                    print(f"You have been delt:\nThe {self.holding[-1]}"); time.sleep(1)
            if move == "stay":
                print(f"\nYou have decided to stay with a hand value of {self.value}")
                self.done=True


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


    def pay_bet(self, multiplier):
        """
        Pays the bet amount to the player then zeros the bet amount
        """
        if multiplier == 1:
            print(f"\n{self.player_name}Looks like you pushed with the dealer, both of you have a hand value of {self.value}. Your bet of {self.bet} chips will be returned to you.\n")
            self.chips += (self.bet*multiplier)
            self.bet=None
        elif multiplier == 2:
            print(f"\nCongrads {self.player_name}, You have won with a hand value of {self.value}. Your bet of {self.bet} chips has been added to your chip stack\n")
            self.chips += (self.bet*multiplier)
            self.bet=None


    def check_win(self):
        """
        ran after all betting rounds to pay off the winner, updates chips and bet with the appropiate amounts 
        """
        if not dealer.busted and not self.busted:
            if dealer.value < self.value:
                self.pay_bet(2)
            elif dealer.value == self.value:
                self.pay_bet(1)
            else:
                print(f"\nSorry {self.player_name}, the dealer has {dealer.value} and you only have {self.value}. You have lost {self.bet} chips.")
                self.bet=None
        elif self.busted:
            print(f"\n{self.player_name} busted with a hand value of {self.value}. You lost {self.bet} chips.")
            self.bet=None
        elif dealer.busted and not self.busted:
            self.pay_bet(2)





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
    """
    Takes the bets for all the players
    """
    for player in players:
        player.take_bet()


def betting_round():
    """
    Plays the hand of each player and dealer by using the Player classes function play_hand()
    """
    for player in players_plus_dealer:
        player.play_hand()


def pay_day():
    """
    Compares each player's hand value to the dealers to decided if they win. If they did not loss they are paid accordingly
    """
    time.sleep(3)
    for player in players:
        player.check_win()
        time.sleep(.5)


def reset():
    """
    takes all the cards and returns them to the deck, suffles the deck, and resets player values =
    """
    for player in players_plus_dealer:
        while player.holding:
            player.return_all_cards()
    deck.Shuffle_deck()


def main():
    game_on=True
    add_players() #asks how many players and names them
    
    players_plus_dealer.append(dealer)
    while game_on:
        place_bets()#Ask the Player for their bet #Make sure that the Player's bet does not exceed their available chips
        dealer.deal_cards()
        print(dealer)#Show only one of the Dealer's cards, the other remains hidden
        show_player_values()#Show both of the Player's cards
        betting_round()#Ask the Player if they wish to Hit, and take another card #If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again. #If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
        pay_day()#Determine the winner and adjust the Player's chips accordingly
        reset()#This will need to return all the cards to the deck and decide if any players do not have any chips left
        #play_again()#Ask the Player if they'd like to play again
        game_on= False

    def current_game():
        """
        Used for replaying game. Does not ask for players names
        """
deck=Deck() #creates the deck
dealer=Dealer() #creates the dealer
main()