from burtBaccarat.models import Card
from burtBaccarat.rules import bankerDraws, playRound


class StubShoe:
	def __init__(self, cards):
		self.cards = list(reversed(cards))

	def draw(self):
		return self.cards.pop()


def testBankerStands() -> None:
	cards = [
		Card("4", "Spades"),
		Card("3", "Clubs"),
		Card("2", "Hearts"),
		Card("3", "Diamonds"),
	]
	roundData = playRound(StubShoe(cards))
	assert roundData.playerTotal == 6
	assert roundData.bankerTotal == 6
	assert len(roundData.bankerHand) == 2
	assert roundData.outcome == "t"


def testBankerDraws() -> None:
	assert bankerDraws(0, 8) is True
	assert bankerDraws(3, 8) is False
	assert bankerDraws(4, 2) is True
	assert bankerDraws(5, 3) is False
	assert bankerDraws(6, 7) is True
	assert bankerDraws(6, 5) is False
