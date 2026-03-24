from __future__ import annotations

import math

from .models import RoundData


mainBets = ("Player", "Banker", "Tie")
sideBets = (
	"Panda 8",
	"Ox 6",
	"All Black",
	"All Red",
	"Dragon Bonus Banker",
	"Dragon Bonus Player",
	"Dragon 7",
	"Lucky Bonus",
	"3 Card Player",
	"3 Card Banker",
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


def mainDelta(bets: dict[str, int], outcome: str) -> tuple[int, list[str]]:
	delta = 0
	msgs: list[str] = []

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


def sideDelta(bets: dict[str, int], roundData: RoundData) -> tuple[int, list[str]]:
	delta = 0
	msgs: list[str] = []
	playerTotal = roundData.playerTotal
	bankerTotal = roundData.bankerTotal
	playerWin = roundData.outcome == "p"
	bankerWin = roundData.outcome == "b"

	playerColors = {card.color for card in roundData.playerHand}

	if bets["3 Card Player"] > 0:
		amount = bets["3 Card Player"]
		if len(roundData.playerHand) == 3 and playerWin:
			win = amount * 4
			msgs.append(f"You won ${win} on the Three Card Player!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Three Card Player.")
			delta -= amount

	if bets["3 Card Banker"] > 0:
		amount = bets["3 Card Banker"]
		if len(roundData.bankerHand) == 3 and bankerWin:
			win = amount * 5
			msgs.append(f"You won ${win} on the Three Card Banker!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Three Card Banker.")
			delta -= amount

	if bets["All Black"] > 0:
		amount = bets["All Black"]
		if playerColors == {"black"}:
			win = amount * 24
			msgs.append(f"Wow, you won ${win} on All Black!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the All Black.")
			delta -= amount

	if bets["All Red"] > 0:
		amount = bets["All Red"]
		if playerColors == {"red"}:
			win = amount * 22
			msgs.append(f"Woo! You won ${win} on the All Red!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the All Red.")
			delta -= amount

	if bets["Dragon 7"] > 0:
		amount = bets["Dragon 7"]
		if len(roundData.bankerHand) == 3 and bankerTotal == 7 and bankerWin:
			win = amount * 40
			msgs.append(f"Boy howdy! You just won ${win} on the Dragon 7!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Dragon 7.")
			delta -= amount

	if bets["Dragon Bonus Banker"] > 0:
		amount = bets["Dragon Bonus Banker"]
		margin = bankerTotal - playerTotal
		odds = bonusOdds.get(margin, 0)
		if bankerWin and odds > 0:
			win = amount * odds
			msgs.append(f"You won ${win} on the Dragon Bonus for Banker!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Dragon Bonus for Banker.")
			delta -= amount

	if bets["Dragon Bonus Player"] > 0:
		amount = bets["Dragon Bonus Player"]
		margin = playerTotal - bankerTotal
		odds = bonusOdds.get(margin, 0)
		if playerWin and odds > 0:
			win = amount * odds
			msgs.append(f"You won ${win} from the Dragon Bonus for Player!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Dragon Bonus for Player.")
			delta -= amount

	if bets["Lucky Bonus"] > 0:
		amount = bets["Lucky Bonus"]
		if bankerTotal == 6 and bankerWin:
			win = amount * 18
			msgs.append(f"You won ${win} on the Lucky Bonus!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Lucky Bonus.")
			delta -= amount

	if bets["Ox 6"] > 0:
		amount = bets["Ox 6"]
		if len(roundData.playerHand) == 3 and playerTotal == 6 and playerWin:
			win = amount * 40
			msgs.append(f"Holy cows! You just won ${win} on the Ox 6!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Ox 6.")
			delta -= amount

	if bets["Panda 8"] > 0:
		amount = bets["Panda 8"]
		if len(roundData.playerHand) == 3 and playerTotal == 8 and playerWin:
			win = amount * 25
			msgs.append(f"Wow! You won ${win} on the Panda 8!")
			delta += win
		else:
			msgs.append(f"You lost ${amount} from the Panda 8.")
			delta -= amount

	return delta, msgs
