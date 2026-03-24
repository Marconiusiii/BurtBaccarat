from burtBaccarat.models import Card, Hand, RoundData
from burtBaccarat.payouts import sideDelta


def makeRound(playerCards, bankerCards, outcome: str) -> RoundData:
	return RoundData(
		playerHand=Hand(list(playerCards)),
		bankerHand=Hand(list(bankerCards)),
		outcome=outcome,
		events=[],
	)


def zeroBets() -> dict[str, int]:
	return {
		"Panda 8": 0,
		"Ox 6": 0,
		"All Black": 0,
		"All Red": 0,
		"Dragon Bonus Banker": 0,
		"Dragon Bonus Player": 0,
		"Dragon 7": 0,
		"Lucky Bonus": 0,
		"3 Card Player": 0,
		"3 Card Banker": 0,
	}


def testDragonSeven() -> None:
	roundData = makeRound(
		playerCards=[Card("8", "Spades"), Card("10", "Clubs")],
		bankerCards=[Card("3", "Hearts"), Card("2", "Diamonds"), Card("2", "Spades")],
		outcome="p",
	)
	bets = zeroBets()
	bets["Dragon 7"] = 10
	delta, _ = sideDelta(bets, roundData)
	assert delta == -10


def testAllRed() -> None:
	roundData = makeRound(
		playerCards=[Card("2", "Hearts"), Card("3", "Diamonds"), Card("3", "Spades")],
		bankerCards=[Card("10", "Clubs"), Card("10", "Spades")],
		outcome="p",
	)
	bets = zeroBets()
	bets["All Red"] = 5
	delta, _ = sideDelta(bets, roundData)
	assert delta == -5


def testPandaNeedsWin() -> None:
	roundData = makeRound(
		playerCards=[Card("3", "Hearts"), Card("2", "Diamonds"), Card("3", "Clubs")],
		bankerCards=[Card("10", "Clubs"), Card("9", "Spades")],
		outcome="b",
	)
	bets = zeroBets()
	bets["Panda 8"] = 10
	delta, _ = sideDelta(bets, roundData)
	assert delta == -10
