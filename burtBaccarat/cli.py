from __future__ import annotations

from .session import GameSession


version = "2.0.0"


class QuitGame(Exception):
	pass


def quitNow(state: GameSession) -> None:
	print(state.quitText())
	raise QuitGame()


def readInput(prompt: str, state: GameSession | None = None) -> str:
	value = input(prompt).strip()
	if value.lower() == "q":
		if state is None:
			print("Quitting the game. The dealer shrugs and sweeps the cards back into the shoe.")
			raise QuitGame()
		quitNow(state)
	return value


def getBank() -> int:
	print("How much would you like to cash in for your bank?")
	while True:
		try:
			bank = int(readInput("$"))
		except ValueError:
			print("That wasn't a number. Try again.")
			continue
		if bank <= 0:
			print("You need a positive bankroll to start.")
			continue
		return bank


def getAmount(bank: int, state: GameSession | None = None) -> int:
	while True:
		try:
			amount = int(readInput("\t$> ", state))
		except ValueError:
			print("\tThat wasn't a number!")
			continue
		if amount <= 0:
			print("\tYou have to make a positive bet to play.")
			continue
		if amount > bank:
			print("\tYou don't have enough money for that bet.")
			continue
		return amount


def getCash(state: GameSession) -> None:
	if state.bank <= 0:
		print("\tYou are out of money. How much would you like to add?")
	else:
		print("\tYour chips are getting low. How much would you like to add?")
	while True:
		try:
			cash = int(readInput("\t$> ", state))
		except ValueError:
			print("\tThat wasn't a number. Try again.")
			continue
		if cash <= 0:
			print("\tPlease enter a positive amount.")
			continue
		state.addCash(cash)
		print(f"\tAlright, your bankroll is now ${state.bank}.")
		return


def showBets(state: GameSession) -> None:
	for betName, amount in state.bets.items():
		if amount > 0:
			print(f"You have ${amount} on the {betName} bet.")
	for betName, amount in state.sideBets.items():
		if amount > 0:
			print(f"You have ${amount} on the {betName} side bet.")


def setSideBets(state: GameSession) -> None:
	codeMap = {
		"p3": "3 Card Player",
		"b3": "3 Card Banker",
		"ar": "All Red",
		"ab": "All Black",
		"o": "Ox 6",
		"p": "Panda 8",
		"dbb": "Dragon Bonus Banker",
		"dbp": "Dragon Bonus Player",
		"d7": "Dragon 7",
		"l": "Lucky Bonus",
	}
	while True:
		print("Choose your Side Bet! Type 'h' for help, 'x' to return, or 'q' to quit.")
		choice = readInput("> ", state).lower()
		if choice == "x":
			print("Returning to game....")
			return
		if choice == "h":
			print(
				"Side Bet Codes:\n"
				"\t'ab': All Black\n"
				"\t'ar': All Red\n"
				"\t'b3': 3 Card Banker\n"
				"\t'd7': Dragon 7\n"
				"\t'dbb': Dragon Bonus Banker\n"
				"\t'dbp': Dragon Bonus Player\n"
				"\t'l': Lucky Bonus\n"
				"\t'o': Ox 6\n"
				"\t'p': Panda 8\n"
				"\t'p3': 3 Card Player\n"
				"\t'x': Exit Side Betting\n"
				"\t'q': Quit Game"
			)
			continue
		betName = codeMap.get(choice)
		if not betName:
			print("Invalid entry! Try again.")
			continue
		print(f"How much on the {betName}?")
		state.setSideBet(betName, getAmount(state.bank, state))
		print(f"Ok, ${state.sideBets[betName]} on the {betName}.")


def takeBets(state: GameSession) -> None:
	while True:
		showBets(state)
		print("Player, Banker, Tie, or Side Bets? Type 'x' to deal or 'q' to quit.")
		choice = readInput("> ", state).lower()
		if choice == "p":
			print("How much on the Player Bet?")
			state.setBet("Player", getAmount(state.bank, state))
			print(f"Ok, ${state.bets['Player']} on the Player Bet.")
			continue
		if choice == "b":
			print("How much on the Banker Bet?")
			state.setBet("Banker", getAmount(state.bank, state))
			print(f"Ok, ${state.bets['Banker']} on the Banker Bet.")
			continue
		if choice == "t":
			print("How much for the Tie Bet?")
			state.setBet("Tie", getAmount(state.bank, state))
			print(f"Ok, ${state.bets['Tie']} on the Tie.")
			continue
		if choice == "s":
			setSideBets(state)
			continue
		if choice == "d":
			print(f"Decision Table for the current game:\n{state.decisions}")
			continue
		if choice == "z":
			print("Zeroing out your bets.")
			state.clearBets()
			continue
		if choice == "x":
			if state.dealDone():
				print("Done betting! Drawing cards...")
			else:
				print("Burning a hand with no bets. What fun!")
			return
		print("That's not a choice! Try again!")


def checkShuffle(state: GameSession) -> None:
	for msg in state.shuffleMsgs():
		print(msg)


def doRound(state: GameSession) -> None:
	for msg in state.playHand():
		print(msg)


def runCli() -> None:
	print(f"Burt Baccarat v.{version}\n\tBy: Marco Salsiccia")
	startBank = getBank()
	state = GameSession(bank=startBank, startBank=startBank)
	for msg in state.startMsgs():
		print(msg)

	try:
		while True:
			if state.needCash():
				getCash(state)
			checkShuffle(state)
			print("Place your bets!")
			takeBets(state)
			doRound(state)
	except QuitGame:
		return
