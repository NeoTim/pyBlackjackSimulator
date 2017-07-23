from Player import Player
from ThinkTank import ThinkTank
import random

class Dealer(object):

    @classmethod
    def get_card_face(cls, x):
        '''convet id to actual card face, for display purposes only'''
        return {
            0: "2",
            1: "3",
            2: "4",
            3: "5",
            4: "6",
            5: "7",
            6: "8",
            7: "9",
            8: "10",
            9: "J", 
            10: "Q", 
            11: "K", 
            12: "A", 
        }.get(x, "Unknown") # Default: error
    
    @classmethod   
    def _draw_card(cls): # private, RNG
        '''gen card id 0-12 -> 2-A'''
        '''ID:   0 1 2 3 4 5 6 7 8  9 10 11 12'''
        '''face: 2 3 4 5 6 7 8 9 10 J Q  K  A'''
        
        card_id = random.randint(0, 12)
        
        # Might need to use a link list for better modeling the odds
        
        return card_id
    
    
    def __init__(self, name, position, deck_count=6):
        '''dealer composites the deal player object, dealer also control
        all decks/cards'''
        
        self.name = "Dealer " + name
        self.player = Player(name, position) # composite
        
        # variables need to be reset every game
        self.highest_player_card_value = 0 # keep track
    
        self.deck_count = deck_count
        cnt = deck_count * 4
        self.card_count = [cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt]
        
        # Hmm counting this way might not be exactly the same
        # Once a card is drawn the odd for randomization should change
        
        self.total_card_left = 52*deck_count
        
    def reset(self):
        '''reset decks/cards'''
        cnt = self.deck_count * 4
        self.card_count = [cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt,cnt]
        
        self.total_card_left = 52*self.deck_count
        self.highest_player_card_value = 0
        
    def draw_next_card(self):
        '''Use class random draw card, as well as COUNT card numbers'''
        next_card = self.__class__._draw_card() # get random card
        if self.card_count[next_card] == 0: # all used? this is very unlikely for 4 decks
            print "REALLY INTERESTING, what an odd!", self.card_count
            next_card = self.draw_next_card() # recusive
        else:
            self.card_count[next_card] -= 1
             
        return next_card
        
    def check_player(self, player, is_dealer=False):
        player_val = player.cal_value()
       
        if player_val < 21:
            if is_dealer is True:
                print "Let's see: , " + self.name + " got " + str(player_val)
                if self.highest_player_card_value < player_val: # tie??? don't pay or take money?
                    print self.name + "got higher cards and wins"
                
            else:
                print player.name + " has " + str(player_val)
                if self.highest_player_card_value < player_val:
                    self.highest_player_card_value = player_val
                    print "Current game got new higest value " + str(player_val)
        
        elif player_val == 21:
            player.win_21 = True
            if is_dealer is True:
                print "wow! " + self.name + " got 21 huh~ Everybody give money to Dealer"
            else:
                print "wow! " + player.name + " got 21, DEALER WILL PAY RIGHT NOW"
               
        else: # busted
            player.is_busted = True
            if is_dealer is True:
                print ("wow! " + self.name + " got busted, val = %i, whoever is still on the table wins!" %(player_val))
            else:
                print ("wow! " + player.name + " got busted, val = %i, dealer take your money NOW!" %(player_val))

        
    def check_self(self, players):
        '''Dealer move last'''
        stand_player_count = 0
        for player in players:
            if player.is_busted or player.win_21:
                continue
            else:
                stand_player_count += 1
        
        if stand_player_count == 0:
            return
        
        # Now at least one stand player, dealer needs to draw cards
        '''notes:  If the player and dealer have the same point total(TIE),
        this is called a "PUSH", and the player typically does not win or
        lose money on that hand.'''
        thres = ThinkTank.cal_draw_thres_low_by_position(self.player.position)
        while self.player.cal_value() < self.highest_player_card_value or \
                self.player.cal_value() < thres:
            new_card = self.draw_next_card()
            print self.name + " draw new card " + self.__class__.get_card_face(new_card)
            self.player.cards.append(new_card)
            
        self.check_player(self.player, True)
        
        
        