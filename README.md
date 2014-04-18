Black jack simulator
antai.ted@gmail.com

GAME SPEC:
	2-deck, 104 cards. Total, Bellagio has 2-deck and 6-deck games. Will do 6-deck simulation later.
	based on hard 17, dealer has to draw cards if deal’s hand is less than 17. Soft 17 will slightly slightly improve dealer’s advantage. 
	FACE-UP, players are able to see each other’s card
	Not considering splitting Ace (too complicated)
	No surrender or insurance

GOAL:
	The goal is NOT to win Blackjack or 21 ( there is a difference between blackjack and 21, blackjack means only two cards, an Ace and a 10 valued card, the payout for blackjack is more than the bet, VS payout for 21 is even)

	The goal is to BUST the dealer!!!!
	

STRATEGY:  

	Let’s say players Antai, Bob, Chris, and Dan are sitting on the table clockwise, which means every time dealer deals the card starts from AnTai, and ends at Dan.

	Because Dan sits at the end of the table, he has more clues to figure out the situation. (Except for cases where a player got 21 or busted, the chip is paid or taken away immediately by the dealer)

BET:
AnTai bet 10 dollar,
Bob bet 20 dollar,
Chris bet 30 dollar,
and Dan bet 50 dollar each time,

the strategy is to SACRIFICE AnTai, Bob, even Chris, and make Dan win. Play as a team!!!! (We split our prize after we get back to hotel)

As for AnTai, he keeps asking for more cards if his card total is less than 20,
for Bob, the three is 19
for Chirs, the three is 18
for Dan, the three is 17

Each player keep track of the highest hand in current game,
when they see others have a hand higher than his own thres, he stops draw cards unless his card value is less than his lower_thres( different for everyone,  around 15,16)

COUNTING:
	It also needs players to count cards a little bit, as for Bellagio they have 2-deck and 6-deck game,
		As for 2-deck games counting is important especially when there are many players
		As for 6-deck cuz the cards in play is way less than total_cards, counting doesn’t really make a difference in terms of odds

	
