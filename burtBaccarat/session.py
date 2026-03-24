from __future__ import annotations

from dataclasses import dataclass, field

from .payouts import mainBets, mainDelta, sideBets, sideDelta
from .rules import playRound
from .shoe import Shoe


@dataclass
class GameSession:
	bank: int
	startBank: int
	bets: dict[str, int] = field(default_factory=lambda: {name: 0 for name in mainBets})
	sideBets: dict[str, int] = field(default_factory=lambda: {name: 0 for name in sideBets})
	decisions: list[str] = field(default_factory=list)
	shoe: Shoe = field(default_factory=Shoe)

	def clearBets(self) -> None:
		for name in self.bets:
			self.bets[name] = 0
		for name in self.sideBets:
			self.sideBets[name] = 0

	def addCash(self, cash: int) -> None:
		self.bank += cash

	def setBet(self, betName: str, amount: int) -> None:
		self.bets[betName] = amount

	def setSideBet(self, betName: str, amount: int) -> None:
		self.sideBets[betName] = amount

	def quitText(self) -> str:
		diff = self.bank - self.startBank
		if diff > 0:
			return f"You leave ${diff} ahead. The casino files a tiny complaint and the cards glare at your back."
		if diff < 0:
			return f"You leave ${abs(diff)} down. The house thanks you for your donation and promises to spend it irresponsibly."
		return "You leave exactly even. Somehow you have achieved the spiritual middle seat of gambling."

	def needCash(self) -> bool:
		return self.bank <= 0

	def canShuffle(self) -> bool:
		return self.shoe.needsShuffle()

	def shuffleMsgs(self) -> list[str]:
		if not self.canShuffle():
			return []
		self.shoe.shuffle()
		self.shoe.burn()
		self.decisions.clear()
		return [
			"\nShuffling the shoe!\n",
			"\n\tBurning 10 Cards!\n",
		]

	def startMsgs(self) -> list[str]:
		self.shoe.burn()
		return [
			f"Great, starting off with ${self.bank}. Good luck!",
			"\n\tShuffling the shoe!\n",
			"\n\tBurning 10 Cards!\n",
		]

	def dealDone(self) -> bool:
		return any(self.bets.values()) or any(self.sideBets.values())

	def playHand(self) -> list[str]:
		roundData = playRound(self.shoe)
		msgs = list(roundData.events)

		self.decisions.append(roundData.outcome.upper())
		if len(self.decisions) > 10:
			self.decisions.pop(0)

		mainWin, mainMsgs = mainDelta(self.bets, roundData.outcome)
		sideWin, sideMsgs = sideDelta(self.sideBets, roundData)
		self.bank += mainWin + sideWin
		self.clearBets()

		msgs.extend(mainMsgs)
		msgs.extend(sideMsgs)
		msgs.append(f"You now have ${self.bank} in your bank.\n")
		return msgs
