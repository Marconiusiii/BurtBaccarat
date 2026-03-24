from __future__ import annotations

import math

from .models import RoundData


mainBets = ("Player", "Banker", "Tie")
stdBets = (
	"Dragon Bonus Banker",
	"Dragon Bonus Player",
	"Player Pair",
	"Banker Pair",
	"Either Pair",
	"Perfect Pair Player",
	"Perfect Pair Banker",
)
easyBets = (
	"Dragon Bonus Banker",
	"Dragon Bonus Player",
	"Dragon 7",
	"Panda 8",
)

bonusOdds = {
	4: 1,
	5: 2,
	6: 4,
	7: 6,
	8: 10,
	9: 30,
}


def vig(bet: int) -> int:
	total = bet * 0.05
	if bet < 25:
		return math.ceil(total)
	return math.floor(total)


def pairWin(hand) -> bool:
	return hand.cards[0].rank == hand.cards[1].rank


def perfPair(hand) -> bool:
	return hand.cards[0] == hand.cards[1]


def ezPush(roundData: RoundData, gameType: str) -> bool:
	if gameType != "easy":
		return False
	return roundData.outcome == "b" and len(roundData.bankerHand) == 3 and roundData.bankerTotal == 7


def mainDelta(bets: dict[str, int], roundData: RoundData, gameType: str) -> tuple[int, list[str]]:
	delta = 0
	msgs: list[str] = []
	outcome = roundData.outcome

	if outcome == "p":
		if bets["Player"] > 0:
			msgs.append(f"You win ${bets['Player']}!")
			delta += bets["Player"]
		if bets["Banker"] > 0:
			msgs.append(f"You lose ${bets['Banker']}.")
			delta -= bets["Banker"]
		if bets["Tie"] > 0:
			msgs.append(f"You lose ${bets['Tie']} from the Tie Bet.")
			delta -= bets["Tie"]
	elif outcome == "b":
		if bets["Player"] > 0:
			msgs.append(f"You lose ${bets['Player']}.")
			delta -= bets["Player"]
		if bets["Banker"] > 0:
			if ezPush(roundData, gameType):
				msgs.append("Easy Baccarat push rule! Banker wins with a 3-card 7, so the Banker bet pushes.")
			elif gameType == "easy":
				msgs.append(f"You won ${bets['Banker']}!")
				delta += bets["Banker"]
			else:
				fee = vig(bets["Banker"])
				msgs.append(f"You won ${bets['Banker']}!")
				msgs.append(f"${fee} paid to the House for the vig.")
				delta += bets["Banker"] - fee
		if bets["Tie"] > 0:
			msgs.append(f"You lost ${bets['Tie']} from the Tie Bet.")
			delta -= bets["Tie"]
	else:
		msgs.append("Player and Banker bets push!")
		if bets["Tie"] > 0:
			msgs.append(f"You won ${bets['Tie'] * 8} on the Tie Bet! Woo!")
			delta += bets["Tie"] * 8

	return delta, msgs


def sideDelta(bets: dict[str, int], roundData: RoundData, gameType: str) -> tuple[int, list[str]]:
	delta = 0
	msgs: list[str] = []
	playerTotal = roundData.playerTotal
	bankerTotal = roundData.bankerTotal
	playerWin = roundData.outcome == "p"
	bankerWin = roundData.outcome == "b"
	natTie = roundData.playerNat and roundData.bankerNat and playerTotal == bankerTotal

	if bets.get("Dragon 7", 0) > 0:
		amount = bets["Dragon 7"]
		if len(roundData.bankerHand) == 3 and bankerTotal == 7 and bankerWin:
			win = amount * 40
			msgs.append(f"Boy howdy! You just won ${win} on the Dragon 7!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Dragon 7.")
			delta -= amount

	if bets.get("Dragon Bonus Banker", 0) > 0:
		amount = bets["Dragon Bonus Banker"]
		margin = bankerTotal - playerTotal
		odds = bonusOdds.get(margin, 0)
		if natTie:
			msgs.append("Dragon Bonus Banker pushes on a natural tie.")
		elif roundData.bankerNat and bankerWin:
			win = amount
			msgs.append(f"You won ${win} on the Dragon Bonus for Banker!")
			delta += win
		elif bankerWin and odds > 0:
			win = amount * odds
			msgs.append(f"You won ${win} on the Dragon Bonus for Banker!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Dragon Bonus for Banker.")
			delta -= amount

	if bets.get("Dragon Bonus Player", 0) > 0:
		amount = bets["Dragon Bonus Player"]
		margin = playerTotal - bankerTotal
		odds = bonusOdds.get(margin, 0)
		if natTie:
			msgs.append("Dragon Bonus Player pushes on a natural tie.")
		elif roundData.playerNat and playerWin:
			win = amount
			msgs.append(f"You won ${win} from the Dragon Bonus for Player!")
			delta += win
		elif playerWin and odds > 0:
			win = amount * odds
			msgs.append(f"You won ${win} from the Dragon Bonus for Player!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Dragon Bonus for Player.")
			delta -= amount

	if bets.get("Panda 8", 0) > 0:
		amount = bets["Panda 8"]
		if len(roundData.playerHand) == 3 and playerTotal == 8 and playerWin:
			win = amount * 25
			msgs.append(f"Wow! You won ${win} on the Panda 8!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Panda 8.")
			delta -= amount

	if gameType == "standard" and bets.get("Player Pair", 0) > 0:
		amount = bets["Player Pair"]
		if pairWin(roundData.playerHand):
			win = amount * 11
			msgs.append(f"You won ${win} on the Player Pair!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Player Pair.")
			delta -= amount

	if gameType == "standard" and bets.get("Banker Pair", 0) > 0:
		amount = bets["Banker Pair"]
		if pairWin(roundData.bankerHand):
			win = amount * 11
			msgs.append(f"You won ${win} on the Banker Pair!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Banker Pair.")
			delta -= amount

	if gameType == "standard" and bets.get("Either Pair", 0) > 0:
		amount = bets["Either Pair"]
		if pairWin(roundData.playerHand) or pairWin(roundData.bankerHand):
			win = amount * 5
			msgs.append(f"You won ${win} on Either Pair!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from Either Pair.")
			delta -= amount

	if gameType == "standard" and bets.get("Perfect Pair Player", 0) > 0:
		amount = bets["Perfect Pair Player"]
		if perfPair(roundData.playerHand):
			win = amount * 25
			msgs.append(f"You won ${win} on the Perfect Player Pair!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Perfect Player Pair.")
			delta -= amount

	if gameType == "standard" and bets.get("Perfect Pair Banker", 0) > 0:
		amount = bets["Perfect Pair Banker"]
		if perfPair(roundData.bankerHand):
			win = amount * 25
			msgs.append(f"You won ${win} on the Perfect Banker Pair!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Perfect Banker Pair.")
			delta -= amount

	return delta, msgs
