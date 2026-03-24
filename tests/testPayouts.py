from burtBaccarat.models import Card, Hand, RoundData
from burtBaccarat.payouts import mainDelta, sideDelta


def makeRound(playerCards, bankerCards, outcome: str) -> RoundData:
	return RoundData(
		playerHand=Hand(list(playerCards)),
		bankerHand=Hand(list(bankerCards)),
		outcome=outcome,
		events=[],
	)


def zeroBets() -> dict[str, int]:
	return {
		"Dragon Bonus Banker": 0,
		"Dragon Bonus Player": 0,
		"Dragon 7": 0,
		"Panda 8": 0,
		"Player Pair": 0,
		"Banker Pair": 0,
		"Either Pair": 0,
		"Perfect Pair Player": 0,
		"Perfect Pair Banker": 0,
	}


def testDragonSeven() -> None:
	roundData = makeRound(
		playerCards=[Card("8", "Spades"), Card("10", "Clubs")],
		bankerCards=[Card("3", "Hearts"), Card("2", "Diamonds"), Card("2", "Spades")],
		outcome="p",
	)
	bets = zeroBets()
	bets["Dragon 7"] = 10
	delta, _ = sideDelta(bets, roundData, "easy")
	assert delta == -10


def testDragonNatWin() -> None:
	roundData = makeRound(
		playerCards=[Card("9", "Hearts"), Card("10", "Diamonds")],
		bankerCards=[Card("7", "Clubs"), Card("10", "Spades")],
		outcome="p",
	)
	bets = zeroBets()
	bets["Dragon Bonus Player"] = 5
	delta, _ = sideDelta(bets, roundData, "standard")
	assert delta == 5


def testPandaNeedsWin() -> None:
	roundData = makeRound(
		playerCards=[Card("3", "Hearts"), Card("2", "Diamonds"), Card("3", "Clubs")],
		bankerCards=[Card("10", "Clubs"), Card("9", "Spades")],
		outcome="b",
	)
	bets = zeroBets()
	bets["Panda 8"] = 10
	delta, _ = sideDelta(bets, roundData, "easy")
	assert delta == -10


def testEzBankPush() -> None:
	roundData = makeRound(
		playerCards=[Card("4", "Hearts"), Card("2", "Diamonds"), Card("Ace", "Clubs")],
		bankerCards=[Card("2", "Clubs"), Card("3", "Spades"), Card("2", "Hearts")],
		outcome="b",
	)
	bets = {"Player": 0, "Banker": 10, "Tie": 0}
	delta, msgs = mainDelta(bets, roundData, "easy")
	assert delta == 0
	assert "pushes" in msgs[0]


def testEitherPair() -> None:
	roundData = makeRound(
		playerCards=[Card("8", "Hearts"), Card("8", "Diamonds")],
		bankerCards=[Card("2", "Clubs"), Card("9", "Spades")],
		outcome="p",
	)
	bets = zeroBets()
	bets["Either Pair"] = 10
	delta, _ = sideDelta(bets, roundData, "standard")
	assert delta == 50
