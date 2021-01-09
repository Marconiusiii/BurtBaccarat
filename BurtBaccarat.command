#!/usr/bin/env python3

import random
import math

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
		elif playerBet <= 0:
			print("Nice try, hot shot. You have to make a bet to play!")
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

sideBets = {
"Panda 8": 0,
"All Black": 0,
"All Red": 0,
"Dragon Bonus Banker": 0,
"Dragon Bonus Player": 0,
"Dragon 7": 0,
"Lucky Bonus": 0
}

def sideBetting():
	global sideBets
	while True:
		print("Choose your Side Bet!")
		choice = input("> ")
		if choice.lower() == 'ar':
			print("How Much on All Red?")
			sideBets["All Red"] = betPrompt()
			print("Ok, ${} on All Red.".format(sideBets["All Red"]))
			continue
		elif choice.lower() == 'ab':
			print("How much on All Black?")
			sideBets["All Black"] = betPrompt()
			print("Ok, ${} on All Black.".format(sideBets["All Black"]))
			continue
		elif choice.lower() == 'p':
			print("How much on the Panda 8?")
			sideBets["Panda 8"] = betPrompt()
			print("Ok, ${} on the Panda 8.".format(sideBets["Panda 8"]))
			continue
		elif choice.lower() == 'dbb':
			print("How much on the Dragon Bonus for the Banker?")
			sideBets["Dragon Bonus Banker"] = betPrompt()
			print("Ok, ${} on the Dragon Bonus for the Banker.".format(sideBets["Dragon Bonus Banker"]))
		elif choice.lower() ==  'dbp':
			print("How much on the Dragon Bonus for the Player?")
			sideBets["Dragon Bonus Player"] = betPrompt()
			print("Ok, ${} on the Dragon Bonus for the Player.".format(sideBets["Dragon Bonus Player"]))
			continue
		elif choice.lower() == 'd7':
			print("How much on the Dragon 7?")
			sideBets["Dragon 7"] = betPrompt()
			print("Ok, ${} on the Dragon 7.".format(sideBets["Dragon 7"]))
			continue
		elif choice.lower() == 'h':
			print("Side Bet Codes:\n\n\t'ab': All Black\n\tBet that all Player cards are Black\n\t'ar': All Red\n\tBet that all Player cards are Red\n\t'd7': Dragon 7\n\tBet that Banker wins with 7 after drawing 3rd card.\n\t'dbb': Dragon Bonus Banker\n\tBet that Banker wins with a point margin higher than 3 against the Player.\n\t'dbp': Dragon Bonus Player\n\tBet that Player wins with a point margin higher than 3.\n\t'l': Lucky Bonus\n\tBet that Banker wins with a hand totaling 6.\n\t'p': Panda 8\n\tBet that Player wins with a hand totaling 8 after drawing a third card.\n\t'h': Help/Show Bet Codes\n\t'x': Exit Side Betting and Return to Game.")
			continue
		elif choice.lower() == 'l':
			print("How much on the Lucky Bonus?")
			sideBets["Lucky Bonus"] = betPrompt()
			print("Ok, ${} on the Lucky Bonus.".format(sideBets["Lucky Bonus"]))
			continue
		elif choice.lower() == 'x':
			print("Returning to game....")
			break
		else:
			print("Invalid entry! Try again.")

def playerBet():
	global bets, decisions
	while True:
		for key in bets:
			if bets[key] > 0:
				print("You have ${amount} on the {bet} bet.".format(amount=bets[key], bet=key))
		for key in sideBets:
			if sideBets[key] > 0:
				print("You have ${amount} on the {bet} Side Bet.".format(amount=sideBets[key], bet=key))
		print("Player, Banker, Tie, or Side Bets? Type 'x' and hit Enter to finish betting.")
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
		elif choice.lower() == 's':
			sideBetting()
			continue
		elif choice == 'z':
			print("Zeroing out your bets.")
			for key in bets:
				bets[key] = 0
			continue
		elif choice == 'd':
			print("Decision Table for the current game:\n{table}".format(table=decisions))
			continue
		elif choice == 'x':
			if bets["Tie"] > 0 or bets["Player"] > 0 or bets["Banker"] > 0:
				print("Done Betting! Drawing cards...")
				break
			else:
				print("You didn't place any bets, genius! Try again or no cards for you!")
			continue
		else:
			print("That's not a choice! Try again!")
			continue

# Game Start
print("Burt Baccarat v.1.5\n\tBy: Marco Salsiccia")

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

def vig(bet):
	total = bet * 0.05
	if bet < 25:
		commission = math.ceil(total)
	else:
		commission = math.floor(total)
	print("${vig} paid to the House for the vig.".format(vig=commission))
	return commission


def payout(outcome):
	global bets, bank
	if outcome == 'p':
		if bets["Player"] > 0:
			print("You win ${}!".format(bets["Player"]))
			bank += bets["Player"]
			bets["Player"] = 0
		if bets["Banker"] > 0:
			print("You lose ${}.".format(bets["Banker"]))
			bank -= bets["Banker"]
			bets["Banker"] = 0
		if bets["Tie"] > 0:
			print("You lose ${} from the Tie Bet.".format(bets["Tie"]))
			bank -= bets["Tie"]
			bets["Tie"] = 0
	elif outcome == 'b':
		if bets["Player"] > 0:
			print("You lose ${}.".format(bets["Player"]))
			bank -= bets["Player"]
			bets["Player"] = 0
		if bets["Banker"] > 0:
			print("You won ${}!".format(bets["Banker"]))
			bank += bets["Banker"]
			bank -= vig(bets["Banker"])
			bets["Banker"] = 0
		if bets["Tie"] > 0:
			print("You lost ${} from the Tie Bet.".format(bets["Tie"]))
			bank -= bets["Tie"]
			bets["Tie"] = 0
	elif outcome == 't':
		print("Player and Banker bets Push!")
		if bets["Tie"] > 0:
			print("You won ${} on the Tie Bet! Woo!".format(bets["Tie"]*8))
			bank += bets["Tie"] * 8
		for key in bets:
			bets[key] = 0


def baccarat():
	global playerHand, bankerHand, decisions, bank
	outcome = ''
	pHand = []
	bHand = []
	p3card = b3card = ''
	p3val = b3val = 0
	p1card, p1val = draw()
	pHand.append(p1val)
	b1card, b1val = draw()
	bHand.append(b1val)
	p2card, p2val = draw()
	pHand.append(p2val)
	b2card, b2val = draw()
	bHand.append(b2val)
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

	if playerHand == 9 and bankerHand == 9 or playerHand == 8 and bankerHand == 8:
		print("We have a Natural Tie!")
		outcome = 't'
	elif playerHand in [8, 9] and bankerHand < playerHand:
		print("Player wins with a Natural {}!".format(playerHand))
		outcome = 'p'
	elif bankerHand in [8, 9] and playerHand < bankerHand:
		print("Banker Wins with a Natural {}!".format(bankerHand))
		outcome = 'b'
	elif playerHand in [6, 7]:
		print("Player stands on {}.".format(playerHand))
		if bankerHand == 7 and playerHand == 7:
			print("We have a Tie!")
			outcome = 't'
		elif bankerHand == 7 and playerHand == 6:
			print("Banker Wins!")
			outcome = 'b'
		elif bankerHand == 6 and playerHand == 7:
			print("Player Wins!")
			outcome = 'p'
		elif bankerHand > 7:
			print("Banker Wins!")
			outcome = 'b'
		else:
			b3card, b3val = draw()
			bHand.append(b3val)
			if bankerHand + b3val >= 10:
				bankerHand += b3val - 10
			else:
				bankerHand += b3val
			print("Banker draws {card} for a total of {amount}.".format(card=b3card, amount=bankerHand))
			if bankerHand == playerHand:
				print("We have a Tie!")
				outcome = 't'
			elif bankerHand < playerHand:
				print("Player Wins!")
				outcome = 'p'
			elif bankerHand > playerHand:
				print("Banker Wins!")
				outcome = 'b'
	else:
		p3card, p3val = draw()
		pHand.append(p3val)
		if playerHand + p3val >= 10:
			playerHand += p3val - 10
		else:
			playerHand += p3val
		print("Player draws {card} and now has {amount}.".format(card=p3card, amount=playerHand))
		if p3val in [2, 3] and bankerHand in range(5) or p3val in [4, 5] and bankerHand in range(6) or p3val in [6, 7] and bankerHand in range(7) or p3val == 8 and bankerHand in range(3) or p3val in [0, 1, 9] and bankerHand in range(4):
			b3card, b3val = draw()
			bHand.append(b3val)
			if bankerHand + b3val >= 10:
				bankerHand += b3val - 10
			else:
				bankerHand += b3val
			print("Banker draws {card} for a total of {amount}.".format(card=b3card, amount=bankerHand))
		else:
			print("Banker stands with {}.".format(bankerHand))
		if bankerHand == playerHand:
			print("We have a Tie!")
			outcome = 't'
		elif bankerHand < playerHand:
			print("Player Wins!")
			outcome = 'p'
		elif bankerHand > playerHand:
			print("Banker Wins!")
			outcome = 'b'
	if len(decisions) <= 10:
		decisions.append(outcome.upper())
	else:
		decisions.pop(0)
		decisions.append(outcome.upper())

# Payout and Side Bets
	payout(outcome)
	black = ['es', 'bs']
	red = ['ts', 'ds']
	if sideBets["All Black"] > 0:
	#	print("{c1} {c2}".format(c1=p1card, c2=p2card))
		if p1card[-2:] in black and p2card[-2:] in black:
			print("Wow, you won ${} on All Black!".format(sideBets["All Black"] * 24))
			bank += sideBets["All Black"] * 24
			sideBets["All Black"] = 0
		else:
			print("You lost ${} from the All Black.".format(sideBets["All Black"]))
			bank -= sideBets["All Black"]
			sideBets["All Black"] = 0
	if sideBets["All Red"] > 0:
		if p1card[-2:] in red and p2card[-2:] in red:
			print("Woo! You won ${} on the All Red!".format(sideBets["All Red"] * 22))
			bank += sideBets["All Red"] * 22
			sideBets["All Red"] = 0
		else:
			print("You lost ${} from the All Red.".format(sideBets["All Red"]))
			bank -= sideBets["All Red"]
			sideBets["All Red"] = 0
	if sideBets["Dragon 7"] > 0:
		if len(bHand) == 3 and bankerHand == 7:
			print("Boy Howdy! You just won ${} on the Dragon 7!".format(sideBets["Dragon 7"] * 40))
			bank += sideBets["Dragon 7"] * 40
			sideBets["Dragon 7"] = 0
		else:
			print("You lost ${} from the Dragon 7.".format(sideBets["Dragon 7"]))
			bank -= sideBets["Dragon 7"]
			sideBets["Dragon 7"] = 0
	if sideBets["Dragon Bonus Banker"] > 0 or sideBets["Dragon Bonus Player"] > 0:
		odds = 0
		if sideBets["Dragon Bonus Banker"] > 0:
			margin = bankerHand - playerHand
		elif sideBets["Dragon Bonus Player"] > 0:
			margin = playerHand - bankerHand
		if margin == 9:
			odds = 30
		elif margin == 8:
			odds = 10
		elif margin == 7:
			odds = 6
		elif margin == 6:
			odds = 4
		elif margin == 5:
			odds = 2
		elif margin == 4:
			odds = 1
		elif margin <= 3:
			odds = 0	

		if sideBets["Dragon Bonus Banker"] > 0 and bankerHand in [8, 9] and bankerHand > playerHand:
			bankerWin = sideBets["Dragon Bonus Banker"] * odds
			if bankerWin > 0:
				print("You won ${} on the Dragon Bonus for Banker!".format(bankerWin))
				bank += bankerWin
			else:
				print("You lost ${} from the Dragon Bonus for Banker.".format(sideBets["Dragon Bonus Banker"]))
				bank -= sideBets["Dragon Bonus Banker"]
				sideBets["Dragon Bonus Banker"] = 0
		else:
			if sideBets["Dragon Bonus Banker"] > 0:
				print("You lost ${} from the Dragon Bonus for Banker.".format(sideBets["Dragon Bonus Banker"]))
				bank -= sideBets["Dragon Bonus Banker"]
				sideBets["Dragon Bonus Banker"] = 0

		if sideBets["Dragon Bonus Player"] > 0 and playerHand in [8, 9] and playerHand > bankerHand:
			playerWin = sideBets["Dragon Bonus Player"] * odds
			if playerWin > 0:
				print("You won ${} from the Dragon Bonus for Player!".format(playerWin))
				bank += playerWin
			else:
				print("You lost ${} from the Dragon Bonus Player.".format(sideBets["Dragon Bonus Player"]))
				bank -= sideBets["Dragon Bonus Player"]
				sideBets["Dragon Bonus Player"] = 0
		else:
			if sideBets["Dragon Bonus Player"] > 0:
				print("You lost ${} from the Dragon Bonus for Player.".format(sideBets["Dragon Bonus Player"]))
				bank -= sideBets["Dragon Bonus Player"]
				sideBets["Dragon Bonus Player"] = 0
	if sideBets["Lucky Bonus"] > 0:
		if bankerHand == 6:
			print("You won ${} on the Lucky Bonus!".format(sideBets["Lucky Bonus"] * 18))
			bank += sideBets["Lucky Bonus"] * 18
			sideBets["Lucky Bonus"] = 0
		else:
			print("You lost ${} from the Lucky Bonus.".format(sideBets["Lucky Bonus"]))
			bank -= sideBets["Lucky Bonus"]
			sideBets["Lucky Bonus"] = 0
	if sideBets["Panda 8"] > 0:
		if len(pHand) == 3 and playerHand == 8:
			print("Wow! You won ${} on the Panda 8!".format(sideBets["Panda 8"] * 25))
			bank += sideBets["Panda 8"] * 25
			sideBets["Panda 8"] = 0
		else:
			print("You lost ${} from the Panda 8.".format(sideBets["Panda 8"]))
			bank -= sideBets["Panda 8"]
			sideBets["Panda 8"] = 0

decisions = []

# Begin Game Loop
while True:

	if bank <= 0:
		outOfMoney()

	if len(deck) < 8:
		deck = deckGenerator()
		del discard[:]
		print("\nShuffling!\n")
		decisions = []

# Betting
	print("Place your bets!")
	playerBet()

# Drawing hands
	baccarat()
	print("You now have ${} in your bank.".format(bank))
	input("Hit Enter for the next hand...")
	continue