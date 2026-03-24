# Burt Baccarat v.2.0.0

Terminal-based accessible Baccarat game built in Python 3.

## About

Baccarat is one of the easiest casino games to learn. You pick whether the Player hand will win, the Banker hand will win, or the round will end in a Tie. After that, the dealer does all the work and the cards decide whether you were a genius or just donating to the casino for fun.

This version of Burt Baccarat lets you choose between Standard Baccarat and Easy Baccarat before you even cash in, so you can pick the table style you want right from the start.

## How to Play

Run the game with:

```bash
python3 BurtBaccarat.command
```

When the game starts, pick your table:

- `s` for Standard Baccarat
- `e` for Easy Baccarat

After that, enter your opening bankroll and start betting.

At any prompt during the game, type `q` to quit. The game will send you off with a parting message depending on whether you are walking away in profit, leaving a little lighter in the wallet, or somehow landing exactly even like a proper gambling wizard.

## The Basics

All cards count at face value except 10s and face cards, which are worth 0. Aces are worth 1.

Hands are scored by dropping the first digit of any total over 9:

- 7 + 8 = 5
- 9 + Ace = 0
- 4 + 3 = 7

If either side gets an 8 or 9 in the first two cards, that is a Natural and no more cards are drawn.

The Player hand draws a third card on 0 through 5 and stands on 6 or 7. The Banker hand follows the standard Baccarat drawing rules automatically, so you do not have to memorize the whole decision chart unless you really want to impress somebody at a dinner party.

## Main Betting

The main betting prompt only handles the regular game wagers:

- `p` for Player
- `b` for Banker
- `t` for Tie
- `s` to go into the Side Bets menu
- `d` to view the decision table
- `z` to clear your current bets
- `x` to finish betting and deal the hand

All side bets are placed from inside the Side Bets menu only. They do not appear in the main betting prompt.

## Standard Baccarat

Standard Baccarat uses the usual Banker commission. Banker wins pay even money minus a 5% commission.

### Standard Main Bet Payouts

- Player: `1:1`
- Banker: `1:1` minus 5% commission
- Tie: `8:1`

### Standard Side Bets

Type `s` at the main betting prompt, then use these codes:

- `dbp` for Dragon Bonus Player
- `dbb` for Dragon Bonus Banker
- `pp` for Player Pair
- `bp` for Banker Pair
- `ep` for Either Pair
- `ppp` for Perfect Pair Player
- `ppb` for Perfect Pair Banker

### Standard Side Bet Payouts

- Dragon Bonus Player: natural win pays `1:1`; win by 4 pays `1:1`; 5 pays `2:1`; 6 pays `4:1`; 7 pays `6:1`; 8 pays `10:1`; 9 pays `30:1`
- Dragon Bonus Banker: natural win pays `1:1`; win by 4 pays `1:1`; 5 pays `2:1`; 6 pays `4:1`; 7 pays `6:1`; 8 pays `10:1`; 9 pays `30:1`
- Player Pair: `11:1`
- Banker Pair: `11:1`
- Either Pair: `5:1`
- Perfect Pair Player: `25:1`
- Perfect Pair Banker: `25:1`

### Standard Side Bet Notes

Dragon Bonus pushes on a natural tie.

Player Pair and Banker Pair win if the first two cards on that side are the same rank.

Either Pair wins if either the Player or Banker starts with a pair.

Perfect Pair wins only if the first two cards on that side match rank and suit, which is a lot rarer and a lot prettier when it lands.

## Easy Baccarat

Easy Baccarat removes the usual Banker commission, but there is one catch. If the Banker wins with a three-card total of 7, the Banker main bet pushes instead of paying.

### Easy Main Bet Payouts

- Player: `1:1`
- Banker: `1:1`
- Tie: `8:1`
- Banker win with a three-card 7: push on the Banker main bet

### Easy Side Bets

Type `s` at the main betting prompt, then use these codes:

- `dbp` for Dragon Bonus Player
- `dbb` for Dragon Bonus Banker
- `d7` for Dragon 7
- `p8` for Panda 8

### Easy Side Bet Payouts

- Dragon Bonus Player: natural win pays `1:1`; win by 4 pays `1:1`; 5 pays `2:1`; 6 pays `4:1`; 7 pays `6:1`; 8 pays `10:1`; 9 pays `30:1`
- Dragon Bonus Banker: natural win pays `1:1`; win by 4 pays `1:1`; 5 pays `2:1`; 6 pays `4:1`; 7 pays `6:1`; 8 pays `10:1`; 9 pays `30:1`
- Dragon 7: Banker wins with a three-card 7 and pays `40:1`
- Panda 8: Player wins with a three-card 8 and pays `25:1`

## Decision Table

The game tracks recent results in a simple decision table:

- `P` means Player win
- `B` means Banker win
- `T` means Tie

The table stores up to the 10 most recent hands and clears when the shoe is shuffled.

## Final Notes

This game uses an eight-deck shoe. When the shoe is shuffled, 10 cards are burned before play continues.

Play smart, have fun, and if the cards go bad on you for a while, just remember that Baccarat is basically a very classy coin flip wearing a tuxedo.
