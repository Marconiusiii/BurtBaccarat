# Burt Baccarat v.2.0.0

Terminal-based accessible Baccarat game built in Python 3.

## About

Burt Baccarat is an accessible Baccarat game with an eight-deck shoe, automated dealing, and support for Player, Banker, Tie, and common side bets.

This project now separates the reusable game engine from the terminal interface so the Baccarat rules and payout logic can be shared by future front ends such as a web client or an iOS app.

## Project Structure

- `BurtBaccarat.command`: thin terminal launcher
- `burtBaccarat/models.py`: cards, hands, and round result data models
- `burtBaccarat/shoe.py`: eight-deck shoe and burn handling
- `burtBaccarat/rules.py`: core Baccarat dealing and third-card rules
- `burtBaccarat/payouts.py`: main and side-bet settlement
- `burtBaccarat/session.py`: bankroll, bets, shoe state, and round flow
- `burtBaccarat/cli.py`: interactive terminal flow
- `tests/`: regression coverage for rules and payouts

## Running the Game

Run the terminal game with:

```bash
python3 BurtBaccarat.command
```

Type `q` at any prompt during gameplay to quit cleanly.

## Running Tests

If `pytest` is installed, run:

```bash
PYTHONPATH=. pytest
```

## Baccarat Rules

Baccarat is a comparing card game where you bet on whether the Player hand wins, the Banker hand wins, or the round ends in a Tie.

- Card values are face value for Ace through 9.
- 10, Jack, Queen, and King are worth 0.
- Hand totals use modulo 10 scoring.
- Naturals of 8 or 9 stand automatically.
- Player draws on totals 0-5 and stands on 6-7.
- Banker follows the standard third-card drawing matrix.

## Side Bets

The terminal game supports these side bets:

- `3 Card Player`
- `3 Card Banker`
- `All Red`
- `All Black`
- `Dragon 7`
- `Dragon Bonus Banker`
- `Dragon Bonus Player`
- `Lucky Bonus`
- `Ox 6`
- `Panda 8`

## Notes for Porting

The intended integration point for future ports is the pure engine layer:

- `playRound()` in `burtBaccarat/rules.py`
- `mainDelta()` in `burtBaccarat/payouts.py`
- `sideDelta()` in `burtBaccarat/payouts.py`
- `GameSession` in `burtBaccarat/session.py`
- `Shoe` in `burtBaccarat/shoe.py`

That keeps UI code separate from rule enforcement and makes automated testing much easier.
