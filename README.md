# Burt Baccarat v.1.8.6
Terminal-based Accessible Baccarat game built in Python 3.

## About

Baccarat is one of the easiest games to play in a casino, and I wanted to try my hand at building an accessible version that anyone could play in Terminal. This will be refactoring some of the code and functions from my HitTheDeck Blackjack game to repurpose them here.
## ## How to Install

Download the .command file and run it in Terminal by double-clicking it from the Desktop. You can also use Terminal commands to change directory to the one where you have the files downloaded and then running:

$ python3 BurtBaccarat.command

If you have git installed, run the pull command to grab the repository documents:

$ git pull https://www.github.com/Marconiusiii/BurtBaccarat

## What is Baccarat?

Baccarat is a very simple game to play. All you have to do is guess whether the Player or Banker will win, or if they will tie. Baccarat is based entirely on luck and the players don't gave to do anything other than make their bet and wait for the outcome of the cards. The game is played automatically by the dealer and the cards are drawn out of an 8 deck shoe. When the shoe is shuffled, the first 10 cards are burned before play starts.

Players do not receive individual hands against the dealer like Blackjack. Rather the dealer only deals out one set of cards for the collective Player spot and another set of cards for the Banker spot.

The goal of the game is to get a hand that adds up as close to 9 as possible. All of the cards in the game are worth their face value, with the Ace equaling 1, the 5 equaling 5, and so on. However, the 10, Jack, Queen, and King cards are all worth 0.

Two cards are dealt to the Player and to the Banker. If the two cards add up to a value higher than or equal to 10, 10 is subtracted from the hand total. For example, a hand of an 8 and 6 = 4, since 14 - 10 = 4. A hand containing a 9 and an Ace is worth 0 points, etc.

### The Outcomes

If a dealer or player receives a hand totaling 8 or 9, that's called a Natural and the game is decided on whose hand total is higher than the other. A player hand will always stand on 6 or 7, and if the player total is 0-5, a third card is drawn.

If the player hand has not drawn a card, the banker hand follows the same rules, drawing if the value is 0-5, and standing on 6-9.

### The Banker Drawing Rules

If the player hand draws a card, the banker hand follows these rules on determining how to draw and stand. Don't worry, all of this is done automatically by the dealer both in this game and in the actual casino!

* If Player draws 2 or 3, Banker draws if hand = 0-4 and stands if 5-7.
* If Player draws 4 or 5, Banker draws if hand value = 0-5 and stands on 6-7.
* If Player draws 6 or 7, Banker draws if hand value = 0-6 and stands on 7.
* If Player draws 8, Banker draws if hand value = 0-2 and stands on 3-7.
* If Player draws 1, 9, or Face Card/10, Banker draws if hand value = 0-3 and stands on 4-7.

## Playing the Game

After launching the game, you'll be prompted to set up your initial bankroll. Type in a number and hit Enter to get going.

You'll be prompted to make a bet with the "Player, Banker, Tie, or Side Bet?" prompt. You can bet on any or all of the bets and you are not restricted to just one. You may also just type 'x' and hit Enter without entering any bets to burn through a hand. Here are the betting commands you can use at this prompt:
* Player Bet - type 'p' and hit Enter
* Banker Bet - type 'b' and hit Enter
* Tie Bet - type 't' and hit Enter
* Side Bets - type 's' and hit Enter
* Decisions Table - type 'd' and hit Enter
* Zero out Bets - type 'z' and hit Enter
* Finish Betting - type 'x' and hit Enter

### Side Bets

There are a variety of Side Bets that have appeared over the years to make the game more interesting. The most common Baccarat Side Bets are available after you've typed 's' to enter the Side Betting mode. You'll be prompted to enter your side bet. Use the following codes at this prompt to make a bet:

* 3 Card Player: 'p3' - Bet that the Player wins with 3 cards.
* 3 Card Banker: 'b3' - Bet the the Banker wins with 3 cards.
* All Red: 'ar' - Bets that all the Player cards will be REd/Hearts and Diamonds.
* All Black: 'ab' - Bets that all Player cards are all Black/Clubs and Spades.
* Dragon 7: 'd7' - Betting that the Banker will win with a hand totaling 7 after drawing a 3rd card.
* Dragon Bonus Banker: 'dbb' - Betting that the Banker wins by at least 4 points over the player hand total.
* Dragon Bonus Player: 'dbp' - Betting that the Player wins by at least 4 points over the Banker total.
* Lucky Bonus: 'l' - Betting that the Banker wins with a hand totaling 6.
* Ox 6: 'o' - Betting that the Player hand totals 6 and wins with 3 cards.
* Panda 8: 'p' - Betting that the Player wins with a hand totaling 8 after drawing a third card.

Check out the Pay Table to see the odds for these bets.

### Decisions Table
Baccarat tables usually keep track of the winning outcomes over the course of the game. Some players use this to plan their bets, although every outcome is always totally random with no effect on the future hands. This is presented as a list of letters, with 'P' signifying a Player win, 'B' as a Banker win, and 'T' as a Tie. The game keeps track of a maximum of 10 hands at a time. Once you play more than 10 hands, the decision table will update accordingly. When the shoe is shuffled, the Decision Table will clear.

## Pay Table

<table>
<caption>Baccarat Pay Table</caption>
<thead>
<tr>
<th scope="col">Bet</th>
<th scope="col">Payout</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row">Player Bet</th><td>1:1</td>
</tr>
<tr>
<th scope="row">Banker Bet</th><td>1:1 -5% vig</td>
</tr>
<tr>
<th scope="row">Tie Bet</th><td>8:1</td>
</tr>
<tr>
<th scope="row">3 Card Player</th><td>4:1</td>
</tr>
<tr>
<th scope="row">3 Card Banker</th><td>5:1</td>
</tr>
<tr>
<th scope="row">All Red</th><td>22:1</td>
</tr>
<tr>
<th scope="row">All Black</th><td>24:1</td>
</tr>
<tr>
<th scope="row">Dragon 7</th><td>40:1</td>
</tr>
<tr>
<th scope="row">Lucky Bonus</th><td>18:1</td>
</tr>
<tr>
<th scope="row">Ox 6</th><td>40:1</td>
</tr>
<tr>
<th scope="row">Panda 8</th><td>25:1</td>
</tr>
</tbody>
</table>
<table>
<summary>Dragon Bonus Payouts</summary>
<thead>
<tr>
<th scope="col">Win Margin</th>
<th scope=:col">Payout</th>
</tr>
</thead>
<tbody>
<tr>
<th scope="row">9 points</th><td>30:1</td>
</tr>
<tr>
<th scope="row">8 points</th><td>10:1</td>
</tr>
<tr>
<th scope="row">7 points</th><td>6:1</td>
</tr>
<tr>
<th scope="row">6 points</th><td>4:1</td>
</tr>
<tr>
<th scope="row">5 points</th><td>2:1</td>
</tr>
<tr>
<th scope="row">4 points</th><td>1:1</td>
</tr>
<tr>
<th scope="row">3 or less</th><td>Loss</td>
</tr>
</tbody>
</table>

Enjoy! Thanks for Playing!