"""
Milestone Project 2 - Blackjack Game
In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
"""

#imported modules
import random

#varibles and constants
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (2,3,4,5,6,7,8,9,10,"J","Q","K","A")

def ask_name():
	answer= None
	while not answer:
		answer= input("\nWhat is your name?")
	return answer

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = self.value()
        

    def __repr__(self):
    	return  self.rank + ' of ' + self.suit


    def value(self):
    	"""
Used during creation of the card to decide its value
    	"""
    	if self.rank in ["J","Q","K"]:
    		return 10
    	elif self.rank == "A":
    		return 11
    	elif self.rank in range(2, 11):
    		self.rank = str(self.rank)
    		return int(self.rank)


class Deck():

	def __init__(self):
		#Create a deck of 52 cards
		self.deck=[]
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))
		print("The deck is now created")

	def __str__(self):
		length=str(len(self.deck))
		return ("There are "+length+" cards in the deck")

	def shuffle(self):
		#Shuffle the deck
		random.shuffle(self.deck)
		print("\nThe deck is now shffled\n")

	def showDeck(self):
		"""
Prints each card in the deck
		"""
		for card in self.deck:
			x=card
			print(x)

	def topCard(self):
		"""
takes the top card from the deck and returns it
		"""
		card=self.deck.pop(0)
		value=card.value
		print(f"{card} is the top card and it is worth {value}")
		return (card,value)


class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0

	def __repr__(self):
		answer=""
		for card in self.cards:
			answer += str(card) + " "
		return answer

	def addCard(self,toAdd):
		self.cards.append(toAdd[0])
		self.value += toAdd[1]

	def handInfo(self):
		print(f"\n{len(self.cards)} cards in this hand worth {self.value}:\n{self.cards}")


class Player(Hand):

	def __init__(self):
		self.name = ask_name()
		self.chips = 100

deck = Deck()
deck.shuffle()
print(deck)
player1=Player()
player1.handInfo()


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