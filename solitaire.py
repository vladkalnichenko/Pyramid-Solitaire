import random

card= ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'B♠', 'D♠', 'K♠',
	   'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'B♥', 'D♥', 'K♥',
	   'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'B♦', 'D♦', 'K♦',
	   'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'B♣', 'D♣', 'K♣']

def question_1():
	print("Choose your action ->")
	print("What you want to do ? \n   " )
	print("-Please, Press a --> If you want to choose your cards from the field \n   ")
	print("-Please, Press b --> If you want to take cards both from the field and deck  \n   ")
	print("-Please, Press c --> If you desired to change card in the deck  \n   ")

def question_2():
	question_1()
	print("-Please, Press d --> If you want to delete card with value 13 from the board  \n")

def create_cards():
	random.shuffle(card)
	list_of_cards=[]#все наши карточки тут
	for symbols in range(len(card)):
		card_tmp = Card(card[symbols][:-1],card[symbols][-1])
		list_of_cards.append(card_tmp)

	deck_cards = (list_of_cards[0:24]) # карты что в деке
	list_1 = (list_of_cards[24:25])
	list_2 = (list_of_cards[25:27])
	list_3 = (list_of_cards[27:30])
	list_4 = (list_of_cards[30:34])
	list_5 = (list_of_cards[34:39])
	list_6 = (list_of_cards[39:45])
	list_7 = (list_of_cards[45:52])

	playing_layers=[] # карты что на поле разложенные по слоям (список в списке)
	for l in (list_7,list_6,list_5,list_4,list_3,list_2,list_1):

		playing_layers.append(l)
	return deck_cards,playing_layers

class Card():

	def __init__(self,rank,suit ):
		self.suit = suit
		self.rank = rank
		self.set_value()

	def set_value(self):
		if self.rank == 'A':
			self.value = 1
		elif self.rank == '2':
			self.value =2
		elif self.rank == '3':
			self.value =3
		elif self.rank == '4':
			self.value =4
		elif self.rank == '5':
			self.value =5
		elif self.rank == '6':
			self.value =6
		elif self.rank == '7':
			self.value =7
		elif self.rank == '8':
			self.value =8
		elif self.rank == '9':
			self.value =9
		elif self.rank == '10':
			self.value =10
		elif self.rank == 'B':
			self.value =11
		elif self.rank == 'D':
			self.value =12
		elif self.rank=='K':
			self.value=13

	def __add__(self, other):
		return self.value + other.value

	def __str__(self):
		return self.rank + self.suit


class Deck():
	def __init__(self,cards):
		self.cards=cards
		self.activeCard = self.cards[0]
		self.currentIndex = 0

	def if_removed(self):
		self.currentIndex-=1

	def currentIndexChange(self,change_to_Null_index=0):
		if change_to_Null_index == 1 :
			self.currentIndex=0
		else :
			self.currentIndex=self.currentIndex+1

	def getNextDeckCard(self):
		try :
			self.currentIndexChange()
			return self.cards[self.currentIndex]
		except IndexError:
			self.currentIndexChange(1)
			return self.cards[self.currentIndex]

	def changeActiveCard(self):
		self.activeCard=self.getNextDeckCard()

	def using_card_from_the_deck(self):
		self.cards.remove(self.activeCard)
		self.if_removed()

class Game :

	def __init__(self):

		self.deckCards, self.pyramide_layers = create_cards()
		self.deck = Deck(self.deckCards)
		self.active_layer_index = 0

	def changeActiveLayerIndex(self):

		if self.active_layer_index + 1 > 6 :
			raise ValueError
		self.active_layer_index +=1

	def getActiveLayer(self):
		return self.pyramide_layers[self.active_layer_index]

	def hello(self):
		while True:
			print("Write 1 - start \n"
				  "0 - EXIT ")
			while True:
				try:
					answer = int(input())
					break
				except ValueError:
					print("Write 1 or 0, please .")
					continue
			if answer == 1:
				self.start()
			else :
				print("THANK YOU FOR PLAYING ")
				import sys
				sys.exit(1)
			break

	def outputGameSituation(self):

		print(50 * "%")
		print(f"OUR DECK\n  {self.deck.activeCard}")

		for N_layer in range(len(self.pyramide_layers) - 1, -1, -1):
			if N_layer == 0:
				print(3 * " " + " " * (N_layer + N_layer - 1), end="")
			else:
				print(4 * " " + " " * (N_layer + N_layer - 1), end="")
			for card in self.pyramide_layers[N_layer]:
				if self.active_layer_index==N_layer:
					print(card, end="  ")
				else :
					print('++', end="  ")
			print()
		print(50 * "%")

	def start(self):
		while True:

			while True:
				try :
					self.outputGameSituation()
					action = self.choosingPlayAction()

					if action == "a":
						self.chooseCardsIndex()
					elif action == "b":
						self.chooseCardsIndex(use_deck_card=1)
					elif action == "c":
						self.deck.changeActiveCard()
					elif action == "d":
						if self.deck.activeCard.rank == "K":
							self.deck.using_card_from_the_deck()
							self.deck.changeActiveCard()
						active_layer=self.getActiveLayer()
						for cardIndex in range(len(active_layer)):
							if isinstance(active_layer[cardIndex], Card):
								if active_layer[cardIndex].rank == "K":
									active_layer[cardIndex] = " "
					else:
						print("--doAction--has uncorrected parameter ")
						raise ValueError

					if self.isLayerEmty():
						try :
							self.changeActiveLayerIndex()
						except IndexError:
							print("You won ! ")
							break
				except ValueError :
					pass
			break

	def choosingPlayAction(self):
		K_exist = 0

		for card in self.getActiveLayer() :
			if isinstance(card,Card):
				if card.rank == "K" :
					K_exist=1
		if self.deck.activeCard.rank == "K":
			K_exist = 1

		if not K_exist :
			question_1()
			actions=("a","b","c")
		else:
			question_2()
			actions=("a","b","c","d")
		while True:
			try:
				action = input()
				if action not in actions:
					raise ValueError
				break
			except ValueError:
				print("Write correct letter.")
				continue
		return action


	def chooseCardsIndex(self,use_deck_card=0):

		loops_number = 2 - use_deck_card
		cards = [self.deck.activeCard] if use_deck_card else []
		for i in range(loops_number):
			while True:
				try:
					index = int(input(f"Write Card{i+1} index :\n"))

					if index not in range(7 - self.active_layer_index):
						raise IndexError
					if isinstance(self.getActiveLayer()[index],str) :
						raise ValueError

					cards.append(index)
					break
				except IndexError:
					print("Write correct index")
					continue
				except ValueError :
					print("No card in this index")

		#self.isSumEqual13(cards)

		card1 = self.getActiveLayer()[cards[0]] if isinstance(cards[0],int) else cards[0]
		card2 = self.getActiveLayer()[cards[1]]

		if card1 + card2 == 13 :
			return self.removingCardsFromGameAfterChecking(cards)
		else :
			print("Sum of ranks is not equal 13 !!")

			raise ValueError

	def removingCardsFromGameAfterChecking(self,cards):
		for card in cards :
			if isinstance(card,int):
				self.getActiveLayer()[card]='  '
			else:
				self.deck.using_card_from_the_deck()
				self.deck.changeActiveCard()

	def isLayerEmty(self):
		layer= self.getActiveLayer()
		for element in layer :
			if isinstance(element,Card):
				return False
		return True

game = Game()
game.hello()




