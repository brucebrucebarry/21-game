import random

suits = ["Spades","Hearts","Diamonds","Clubs"]
ranks = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]

class Card():
    
    def __init__(self, rank, suit):
        self.rank= rank
        self.suit= suit
        self.isAce= False
        self.value= self.decideValue(self.rank)
    
    def __repr__(self):
        return str(self.rank)+" of " +self.suit
    
    def decideValue(self,cardRank):
        if type(cardRank) == int:
            return cardRank
        elif cardRank in ["Jack","Queen","King"]:
            return 10
        else:
            self.isAce= True
            return 11
        
class Deck():
    
    def __init__(self):
        self.cards=[]
        self.populateDeck()#Create a deck of 52 cards
        self.ShuffleDeck()#Shuffle the deck
        
    def __str__(self):
        return "\nThe number of cards left in the deck is: "+str(len(self.cards))
    
    def ShuffleDeck(self):
        """
Shuffles the deck of cards
"""
        random.shuffle(self.cards)
        print("\n A new deck of cards have been created, shuffled, and is ready to deal!")
        
    def populateDeck(self):
        """
Creates the deck of cards
"""
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank,suit))
                
    def giveCard(self):
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
        
    def addCard(self,toAdd):
        """
Takes a card from the deck instance and addds it to this hand
"""
        self.holding.append(toAdd)
        self.value += toAdd.value
        if toAdd.isAce:
            self.aces += 1
        self.countHand()
    
    def reviewHand(self):
        size= len(self.holding)
        print("\n Cards in hand: \n",size)
        
    def countHand(self):
        if self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            print("\nHad to take away 10\nNew value is:",self.value)
        elif self.value > 21 and not self.aces:
            self.busted = True
            print("game over! Looks like you busted with all your cards adding up to:", self.value)
        else:
            print(self.aces,self.value)
        
        



class Dealer(Hand):
    
    def __init__(self):
        self.hideCards= True
        super().__init__()
        

#Ask the Player for their bet
#Make sure that the Player's bet does not exceed their available chips
#Deal two cards to the Dealer and two cards to the Player
#Show only one of the Dealer's cards, the other remains hidden
#Show both of the Player's cards
#Ask the Player if they wish to Hit, and take another card
#If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
#If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
#Determine the winner and adjust the Player's chips accordingly
#Ask the Player if they'd like to play again
        
        
deck=Deck()
dealer=Dealer()
dealer.addCard(deck.giveCard())
dealer.addCard(deck.giveCard())