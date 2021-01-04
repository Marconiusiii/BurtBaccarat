#!/usr/bin/env python3

import random
# Burt Baccarat 

deck = {}
discard = []

suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']

cardValues = {
'Ace': 1,
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 0,
'Jack': 0,
'Queen': 0,
'King': 0
}

# Deck Generation

def deckGenerator():
	d = {}
	for suit in suits:
		for card, val in cardValues.items():
			d ['{} of {}'.format(card, suit)] = val
	return d

# Draw function
def draw():
	global deck, discard
	while True:
		card, cardVal = random.choice(list(deck.items()))
		if discard.count(card) == 8:
			del deck[card]
			continue
		else:
			discard.append(card)
			break
	return card, cardVal


# Initial deck creation
deck = deckGenerator()

bets = {
"Player": 0,
"Banker": 0,
"Tie": 0
}

def betPrompt():
	global bank
	while True:
		try:
			playerBet =  int(input("\t$> "))
		except ValueError:
			print("\tThat wasn't a number!")
			continue
		if playerBet > bank:
			print("\tYou simply don't have enough money to do that! DO you want to add more to your bankroll?")
			addMore = input(">")
			if addMore.lower() in ['y', 'yes', 'atm', 'help', 'more money']:
				outOfMoney()
			continue
		else:
			return playerBet

def outOfMoney():
	global bank
	if bank <= 0:
		print("\tYou are totally out of money. Let's hit the ATM again and get you more cash. How much do you want?")
	else:
		print("\tYour chips are getting really low. How much would you like to add to your bankroll?")
	while True:
		try:
			cash = int(input("\t$>"))
		except ValueError:
			print("\tYou forgot what numbers were and the ATM beeps at you in annoyance. Try again.")
			continue
		if cash <= 0:
			print("\tWhat am I, a bank? This is for withdrawals only! Try again.")
			continue
		else:
			bank += cash
			break
	print("\tAlright, starting you off again with ${}. Don't lose it all this time!".format(bank))

def playerBet():
	global bets
	while True:
		for key in bets:
			if bets[key] > 0:
				print("You have ${amount} on the {bet} bet.".format(amount=bets[key], bet=key))
		print("Player, Banker, or Tie?")
		choice = input("> ")
		if choice == 'p':
			print("How much on the Player Bet?")
			bets["Player"] = betPrompt()
			print("Ok, ${} on the Player Bet.".format(bets["Player"]))
			continue
		elif choice == 'b':
			print("How much on the Banker Bet?")
			bets["Banker"] = betPrompt()
			print("Ok, ${} on the Banker Bet.".format(bets["Banker"]))
			continue
		elif choice == 't':
			print("How much for the Tie Bet?")
			bets["Tie"] = betPrompt()
			print("Ok, ${} on the Tie.".format(bets["Tie"]))
			continue
		elif choice == 'z':
			print("Zeroing out your bets.")
			for key in bets:
				bets[key] = 0
			continue
		elif choice == 'x':
			print("Done Betting! Drawing cards...")
			break
		else:
			print("That's not a choice! Try again!")
			continue

# Game Start
print("Burt Baccarat v.1.0\n\tBy: Marco Salsiccia")

print("How much would you like to cash in for your bank?")
while True:
	try:
		bank = int(input("$"))
		break
	except ValueError:
		print("That wasn't a number, doofus.")
		continue
print("Great, starting off with ${bank}. Good luck!".format(bank=bank))

playerHand = 0
bankerHand = 0

def baccarat():
	global playerHand, bankerHand, bets, bank
	p1card, p1val = draw()
	p2card, p2val = draw()
	b1card, b1val = draw()
	b2card, b2val = draw()
	if p1val + p2val >= 10:
		playerHand = p1val + p2val - 10
	else:
		playerHand = p1val + p2val
	if b1val + b2val >= 10:
		bankerHand = b1val + b2val - 10
	else:
		bankerHand = b1val + b2val

	print("Player draws {p1} and {p2} for a total of {amount}.".format(p1=p1card, p2=p2card, amount=playerHand))
	print("Banker draws {b1} and {b2} for a total of {amount}.".format(b1=b1card, b2=b2card, amount=bankerHand))


	if playerHand == 9 and bankerHand == 9 or playerHand == 8 and dealerHand == 8:
		print("We have a Tie!")

	elif playerHand == 9 and dealerHand == 8:
		print("Player wins!")

	elif bankerHand == 9 and playerHand == 8:
		print("Banker Wins!")

	elif playerHand in [6, 7]:
		print("Player stands on {}.".format(playerHand))
		if bankerHand == 7 and playerHand == 7:
			print("We have a Tie!")
		elif bankerHand == 7 and playerHand == 6:
			print("Banker Wins!")

		elif bankerHand == 6 and playerHand == 7:
			print("Player Wins!")
		else:
			b3card, b3val = draw()
			if bankerHand + b3val >= 10:
				bankerHand += b3Val - 10
			else:
				bankerHand += b3val
			print("Banker draws {card} for a total of {amount}.".format(card=b3card, amount=b3val))
			if bankerHand == playerHand:
				print("We have a Tie!")
			elif bankerHand < playerHand:
				print("Player Wins!")
			elif bankerHand > playerHand:
				print("Banker Wins!")

	else:
		p3card, p3val = draw()
		if playerHand + p3val >= 10:
			playerHand += p3val - 10
		else:
			playerHand += p3val
		print("Player draws {card} and now has {amount}.".format(card=p3card, amount=playerHand))
		if p3val in [2, 3] and bankerHand in range(5) or p3val in [4, 5] and bankerHand in range(6) or p3val in [6, 7] and bankerHand in range(7) or p3val == 8 and bankerHand in range(3) or p3val in [0, 1, 9] and bankerHand in range(4):
			b3card, b3val = draw()
			if bankerHand + b3val >= 10:
				bankerHand += b3val - 10
			else:
				bankerHand += b3val
			print("Banker draws {card} for a total of {amount}.".format(card=b3card, amount=bankerHand))
		else:
			print("Banker stands with {}.".format(bankerHand))
		if bankerHand == playerHand:
			print("We have a Tie!")
		elif bankerHand < playerHand:
			print("Player Wins!")
		elif bankerHand > playerHand:
			print("Banker Wins!")



# Begin Game Loop
while True:

	if bank <= 0:
		outOfMoney()

	if len(deck) < 8:
		deck = deckGenerator()
		del discard[:]
		print("\nShuffling!\n")

# Betting
	print("You have ${}. Place your bets!".format(bank))
	playerBet()

# Drawing hands
	baccarat()