from __future__ import annotations

import random

from .models import Card, cardVals


suits = ["Spades", "Clubs", "Hearts", "Diamonds"]


class Shoe:
	def __init__(self, decks: int = 8, rng: random.Random | None = None) -> None:
		self.decks = decks
		self.rng = rng or random.Random()
		self.cards: list[Card] = []
		self.shuffle()

	def shuffle(self) -> None:
		self.cards = [
			Card(rank=rank, suit=suit)
			for _ in range(self.decks)
			for suit in suits
			for rank in cardVals
		]
		self.rng.shuffle(self.cards)

	def burn(self, count: int = 10) -> None:
		for _ in range(min(count, len(self.cards))):
			self.draw()

	def draw(self) -> Card:
		if not self.cards:
			raise RuntimeError("Cannot draw from an empty shoe.")
		return self.cards.pop()

	def needsShuffle(self, cutSize: int = 10) -> bool:
		return len(self.cards) <= cutSize

	def __len__(self) -> int:
		return len(self.cards)
