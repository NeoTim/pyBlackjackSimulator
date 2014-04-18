from Player import Player
from Dealer import Dealer

  
class BlackjackGame(object):
    
    def __init__(self):
        self.dealer = None
        self.players = []
          
    
    def create_players(self):
        '''hardcoded for now'''    
        dealer = Dealer("X-Man", 0, 6) # 6 decks
        self.dealer = dealer
        
        player1 = Player("Antai", 1)
        player2 = Player("Bob", 2)
        player3 = Player("Chris", 3)
        player4 = Player("Dan", 4)
        
        self.players.append(player1)
        self.players.append(player2)
        self.players.append(player3)
        self.players.append(player4)

    #------------------------------
    '''COUNT CARDS'''
    def safe_odd(self, player):
        
        if player.cal_value() > 21: #busted already
            # print "busted"
            return 0
        
        if player.cal_value() == 21:    # winner!
            return 1
        
        higest_card_value = self.dealer.highest_player_card_value
        
        diff = 21 - player.cal_value()
        
        if diff >= 10:
            return 1
        
        cnt_sum = 0
        for i in range(diff-1): # Because the counter is from 2,3,4
            cnt_sum += self.dealer.card_count[i]
            
            #face = Dealer.get_card_face(i)
            # print face, self.dealer.card_count[i]
            
        ace_index = 12 # here check ace, which will be used as 1
        cnt_sum += self.dealer.card_count[ace_index] # Ace Counter
        #face = Dealer.get_card_face(ace_index)
        # print face, self.dealer.card_count[ace_index]
        
        
        odd = float(cnt_sum)/self.dealer.total_card_left
        print ("safe odd = %i/%i = %f" %(cnt_sum, self.dealer.total_card_left, odd))
    
        return odd
    
    #------------------------------
    
    def init_new_game(self):
        self.dealer.reset()
        self._clear_players()
        
    def _clear_players(self):
        '''clear all player stuff'''
        self.dealer.player.clear_cards()
        
        for player in self.players:
            player.clear_cards()
           
    def game_update(self, gid=1):
        print ("\n--------------------------------GAME ID: %i-------------------------------" %(gid))
        
        for player in self.players:
            while player.want_more_card(self.dealer.highest_player_card_value, self.safe_odd(player)) is True:
                new_card = self.dealer.draw_next_card()
                player.cards.append(new_card)
                print player.name + " draw new card " + Dealer.get_card_face(new_card)
                
            self.dealer.check_player(player)
            print "-------------------"
        
        self.dealer.check_self(self.players) # NOW: dealer move
        
        return self.accounting()

    def accounting(self):
        print "$$$$$$$$$$$$$$$$$$ Accounting Book $$$$$$$$$$$$$$$$$$"
        
        casino_delta = 0
        dealer_card_value = self.dealer.player.cal_value()
        
        '''check order matters, in reality, player bust/21 will be processed immediately'''
        for player in self.players:
            
            player_delta = 0
            
            if player.is_busted:
                print player.name + " lose " , -player.bet
                player_delta = -player.bet
            elif player.win_21:
                '''DEF: A Blackjack is a total of 21 in your first two cards.
                    It may also be called a Natural.
                    A Blackjack pays you odds of 3 to 2,
                    while any other winning hand, including a 21, pays EVEN money'''
                card_count = len(player.cards)
                if card_count == 2: # TODO: split aces????
                    print player.name + " win blackjack Ace+v10, 1.5 X" , player.bet, "=", 1.5*player.bet
                    player_delta = 1.5*player.bet
                else:
                    print player.name + " got twenty-one win " , player.bet
                    player_delta = player.bet
            else: # player stands check value with dealer
                if self.dealer.player.is_busted:
                    print "Dealer busted " + player.name + " win " , player.bet
                    player_delta = player.bet
                else: # need to compare value
                    player_card_value = player.cal_value()
                    if dealer_card_value < player_card_value:
                        print "Dealer lose " + player.name + " win " , player.bet
                        player_delta = player.bet
                    elif dealer_card_value == player_card_value:
                        print player.name + " and dealer are even: Push"
                    else: #dealer has higher value or dealer win 21 or blackjack
                        print "Dealer win " + player.name + " lose " , -player.bet
                        player_delta = -player.bet
            
            casino_delta += -player_delta # player gain is casino lose. vice versa
        
        print ("$$$$$$$$$$$ Current Game Player Money Pool Delta: $%i $$$$$$$$$$$ " %(-casino_delta))
        return -casino_delta
                    
                    
                    
                    
                    
                    
    def simulate_game(self, game_count = 1):
        
        total_player_pool = 0
        
        for i in range(game_count):
            self.init_new_game()
            total_player_pool += self.game_update(i)
            
            
        print ("\n\n\n------------>TOTAL_GAME_COUNT = %i, Final PLAYER MONEY POOL DELTA = %i <------------- " %(game_count, total_player_pool))
        
        avg_gain = float(total_player_pool) / game_count
        
        bet_sum = 0
        for player in self.players:
            bet_sum += player.bet
            
        win_percent = avg_gain/bet_sum
        print ("------------>Avg_gain_per_game = %f, win_percent = %f" %(avg_gain, win_percent))
#------------------TESTING CODE-----------------------

blackjack_game = BlackjackGame()
blackjack_game.create_players()

blackjack_game.simulate_game(10)
    