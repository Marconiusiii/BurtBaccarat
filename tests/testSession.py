from burtBaccarat.session import GameSession


class StubShoe:
	def __init__(self) -> None:
		self.shuffled = False
		self.burned = False

	def needsShuffle(self) -> bool:
		return True

	def shuffle(self) -> None:
		self.shuffled = True

	def burn(self) -> None:
		self.burned = True


def testQuitTextWin() -> None:
	session = GameSession(bank=150, startBank=100)
	assert "ahead" in session.quitText()


def testQuitTextLoss() -> None:
	session = GameSession(bank=40, startBank=100)
	assert "down" in session.quitText()


def testShuffleMsgs() -> None:
	session = GameSession(bank=100, startBank=100, shoe=StubShoe())
	session.decisions = ["P", "B"]
	msgs = session.shuffleMsgs()
	assert len(msgs) == 2
	assert session.decisions == []
	assert session.shoe.shuffled is True
	assert session.shoe.burned is True
