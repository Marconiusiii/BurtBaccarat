from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable


cardVals = {
	"Ace": 1,
	"2": 2,
	"3": 3,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 7,
	"8": 8,
	"9": 9,
	"10": 0,
	"Jack": 0,
	"Queen": 0,
	"King": 0,
}


@dataclass(frozen=True)
class Card:
	rank: str
	suit: str

	@property
	def value(self) -> int:
		return cardVals[self.rank]

	@property
	def color(self) -> str:
		if self.suit in {"Hearts", "Diamonds"}:
			return "red"
		return "black"

	def __str__(self) -> str:
		return f"{self.rank} of {self.suit}"


@dataclass
class Hand:
	cards: list[Card] = field(default_factory=list)

	def add(self, card: Card) -> None:
		self.cards.append(card)

	@property
	def total(self) -> int:
		return sum(card.value for card in self.cards) % 10

	def __len__(self) -> int:
		return len(self.cards)

	def __iter__(self) -> Iterable[Card]:
		return iter(self.cards)


@dataclass
class RoundData:
	playerHand: Hand
	bankerHand: Hand
	outcome: str
	events: list[str]

	@property
	def playerTotal(self) -> int:
		return self.playerHand.total

	@property
	def bankerTotal(self) -> int:
		return self.bankerHand.total

	@property
	def playerNat(self) -> bool:
		return len(self.playerHand) == 2 and self.playerTotal in {8, 9}

	@property
	def bankerNat(self) -> bool:
		return len(self.bankerHand) == 2 and self.bankerTotal in {8, 9}
