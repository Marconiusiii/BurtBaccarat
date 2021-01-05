# Burt Baccarat v.1.0
Terminal-based Accessible Baccarat game built in Python 3.

## About

Baccarat is one of the easiest games to play in a casino, and I wanted to try my hand at building an accessible version that anyone could play in Terminal. This will be refactoring some of the code and functions from my HitTheDeck Blackjack game to repurpose them here.
## ## How to Install

Download the .command file and run it in Terminal by double-clicking it from the Desktop. You can also use Terminal commands to change directory to the one where you have the files downloaded and then running:

$ python3 BurtBaccarat.command

If you have git installed, run the pull command to grab the repository documents:

$ git pull https://www.github.com/Marconiusiii/BurtBaccarat

## What is Baccarat?

Baccarat is a very simple game to play. All you have to do is guess whether the Player or Banker will win, or if they will tie. Baccarat is based entirely on luck and the players don't gave to do anything other than make their bet and wait for the outcome of the cards. The game is played automatically by the dealer and the cards are drawn out of an 8 deck shoe.

Players do not receive individual hands against the dealer like Blackjack. Rather the dealer only deals out one set of cards for the collective Player spot and another set of cards for the Banker spot.

The goal of the game is to get a hand that adds up as close to 9 as possible. All of the cards in the game are worth their face value, with the Ace equaling 1, the 5 equaling 5, and so on. However, the 10, Jack, Queen, and King cards are all worth 0.

Two cards are dealt to the Player and to the Banker. If the two cards add up to a value higher than or equal to 10, 10 is subtracted from the hand total. For example, a hand of an 8 and 6 = 4, since 14 - 10 = 4. A hand containing a 9 and an Ace is worth 0 points, etc.

### The Outcomes

If a dealer or player receives a hand totaling 8 or 9, that's called a Natural and the game is decided on whose hand total is higher than the other. A player hand will always stand on 6 or 7, and if the player total is 0-5, a third card is drawn.

If the player hand has not drawn a card, the banker hand follows the same rules, drawing if the value is 0-5, and standing on 6-9.

### The Banker Drawing Rules

If the player hand draws a card, the banker hand follows these rules on determining how to draw and stand. Don't worry, all of this is done automatically by the dealer both in this game and in the actual casino!

*If Player draws 2 or 3, Banker draws if hand = 0-4 and stands if 5-7.
*If Player draws 4 or 5, Banker draws if hand value = 0-5 and stands on 6-7.
*If Player draws 6 or 7, Banker draws if hand value = 0-6 and stands on 7.
*If Player draws 8, Banker draws if hand value = 0-2 and stands on 3-7.
*If Player draws 1, 9, or Face Card/10, Banker draws if hand value = 0-3 and stands on 4-7.

## Playing the Game

After launching the game, you'll be prompted to set up your initial bankroll. Type in a number and hit Enter to get going.

You'll be prompted to make a bet with the "Player, Banker, Tie?" prompt. You can bet on any or all of the bets and you are not restricted to just one. Here are the betting commands you can use at this prompt:
*Player Bet - type 'p' and hit Enter
*Banker Bet - type 'b' and hit Enter
*Tie Bet - type 't' and hit Enter
*Decisions Table - type 'd' and hit Enter
*Zero out Bets - type 'z' and hit Enter
*Finish Betting - type 'x' and hit Enter

### Decisions Table

Baccarat tables usually keep track of the winning outcomes over the course of the game. Some players use this to plan their bets, although every outcome is always totally random with no effect on the future hands. This is presented as a list of letters, with 'P' signifying a Player win, 'B' as a Banker win, and 'T' as a Tie. The game keeps track of a maximum of 10 hands at a time. Once you play more than 10 hands, the decision table will update accordingly. When the shoe is shuffled, the Decision Table will clear.

## Pay Table

*Player Bets win 1:1
*Banker Bets win 1:1 minus a 5% vig
*Tie Bets win 8:1

Enjoy! Thanks for Playing!