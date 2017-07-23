Blackjack simulator
antai.ted@gmail.com

GAME SPEC:

	2-deck, 104 cards. Bellagio has 2-deck and 6-deck games. (Will do 6-deck simulation later.)
	Based on hard 17, dealer has to draw cards if her hand is less than 17. Soft 17 will slightly improve dealer’s advantage. 
	FACE-UP, players are able to see each other’s card
	Not considering splitting Ace (too complicated)
	No surrender or insurance

GOAL:
	The goal is NOT to win Blackjack or 21 (There is a difference between blackjack and 21, blackjack means only two cards, an Ace and a 10 valued card, the payout for blackjack is more than the bet, VS payout for 21 is even)

	The goal is to BUST the dealer!
	

STRATEGY:  

	Let’s say players Antai, Bob, Chris, and Dan are sitting on the table clockwise, which means every time dealer deals the card starts from AnTai, and ends at Dan.

	Because Dan sits at the end of the table, he has more clues to figure out the situation. (Except for cases where a player got 21 or busted, the chip is paid or taken away immediately by the dealer)

BET:
AnTai bet 10 dollar,
Bob bet 20 dollar,
Chris bet 30 dollar,
and Dan bet 50 dollar each time,

The strategy is to SACRIFICE AnTai, Bob, even Chris, and make Dan win. Play as a team!

As for AnTai, he keeps asking for more cards if his hand is less than 20 (thres),
for Bob, the thres is 19
for Chirs, the thres is 18
for Dan, the thres is 17

Each player keeps track of the highest hand in current game, if he sees others have higher hand than his own thres, he stops draw cards unless his card value is less than his lower_thres

COUNTING:
	It also needs players to count cards, especially for 2-deck game



HOW TO USE:

python BlackjackGame.py numberOfSimulatedGame
