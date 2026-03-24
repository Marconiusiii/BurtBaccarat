from __future__ import annotations

from .models import Hand, RoundData
from .shoe import Shoe


def bankerDraws(bankerTotal: int, playerThirdVal: int | None) -> bool:
	if playerThirdVal is None:
		return bankerTotal <= 5
	if bankerTotal <= 2:
		return True
	if bankerTotal == 3:
		return playerThirdVal != 8
	if bankerTotal == 4:
		return playerThirdVal in {2, 3, 4, 5, 6, 7}
	if bankerTotal == 5:
		return playerThirdVal in {4, 5, 6, 7}
	if bankerTotal == 6:
		return playerThirdVal in {6, 7}
	return False


def playRound(shoe: Shoe) -> RoundData:
	playerHand = Hand()
	bankerHand = Hand()
	events: list[str] = []

	playerHand.add(shoe.draw())
	bankerHand.add(shoe.draw())
	playerHand.add(shoe.draw())
	bankerHand.add(shoe.draw())

	events.append(
		f"Player draws {playerHand.cards[0]} and {playerHand.cards[1]} for a total of {playerHand.total}."
	)
	events.append(
		f"Banker draws {bankerHand.cards[0]} and {bankerHand.cards[1]} for a total of {bankerHand.total}."
	)

	playerTotal = playerHand.total
	bankerTotal = bankerHand.total

	if playerTotal in {8, 9} or bankerTotal in {8, 9}:
		if playerTotal == bankerTotal:
			events.append("We have a Natural Tie!")
			return RoundData(playerHand, bankerHand, "t", events)
		if playerTotal > bankerTotal:
			events.append(f"Player wins with a Natural {playerTotal}!")
			return RoundData(playerHand, bankerHand, "p", events)
		events.append(f"Banker wins with a Natural {bankerTotal}!")
		return RoundData(playerHand, bankerHand, "b", events)

	playerThirdVal: int | None = None

	if playerTotal <= 5:
		playerCard = shoe.draw()
		playerHand.add(playerCard)
		playerThirdVal = playerCard.value
		events.append(f"Player draws {playerCard} and now has {playerHand.total}.")
	else:
		events.append(f"Player stands on {playerTotal}.")

	if bankerDraws(bankerHand.total, playerThirdVal):
		bankerCard = shoe.draw()
		bankerHand.add(bankerCard)
		events.append(f"Banker draws {bankerCard} for a total of {bankerHand.total}.")
	else:
		events.append(f"Banker stands with {bankerHand.total}.")

	if playerHand.total == bankerHand.total:
		events.append("We have a Tie!")
		outcome = "t"
	elif playerHand.total > bankerHand.total:
		events.append("Player wins!")
		outcome = "p"
	else:
		events.append("Banker wins!")
		outcome = "b"

	return RoundData(playerHand, bankerHand, outcome, events)
