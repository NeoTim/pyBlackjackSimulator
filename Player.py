from ThinkTank import ThinkTank


class Player(object):
    
    @classmethod
    def cal_single_card_value(cls, x):
        '''Convet card id to value'''
        return {
            0: 2,
            1: 3,
            2: 4,
            3: 5,
            4: 6,
            5: 7,
            6: 8,
            7: 9,
            8: 10,
            9: 10, # J
            10: 10, # Q
            11: 10, # K
            12: 11, # A, magic number 1 or 11
        }.get(x, -1) # Default, -1, error
        
        
    @classmethod  
    def _cal_value(cls, obj_cards):
        
        #if len(obj_cards) == 0:
        #   return 0
        
        cards = sorted(obj_cards) # the KEY is to SORT in ascending order, and determine Ace value last
            
        total_value = 0
        size = len(cards)
        for i in range(size):
            card_val = cls.cal_single_card_value(cards[i]) # look up value
            total_value += card_val
            
            if total_value == 21:
                if card_val == 11 and i < (size - 1): # not the last card, have to use 1 not 11
                    total_value -= 10
                    # print "-10 First"
            
            elif total_value > 21: # busted
                if card_val == 11: # use a 1 anyway
                    total_value -= 10
                    # print "-10 Second"
                        
        return total_value
    
    #------------------------object methods starts here--------------
    
    def __init__(self, name, position):
       
        # Those var don't change
        self.name = name
        self.position = position
        
        self.bet = ThinkTank.cal_bet_low_by_position(self.position) # NOT FOR DEALER
        self.safe_zone = ThinkTank.cal_safe_zone_by_position(self.position) # NOT FOR DEALER
        
        self.thres = ThinkTank.cal_draw_thres_high_by_position(self.position) # NOT FOR DEALER
        self.thres_low = ThinkTank.cal_draw_thres_low_by_position(self.position)
                
        # These vars will be reset per game
        self.is_busted = False
        self.win_21 = False
        self.cards = []
       
    def cal_value(self):
        '''calculate cards value'''        
        if len(self.cards) == 0:
            return 0
        
        return self.__class__._cal_value(self.cards)
    
    '''For Player only . Dealer.player shouldn't call this func'''
    def want_more_card(self, higest_card_value_so_far, safe_odd):
         
        card_val = self.cal_value()
        
        # Condition A
        me_think_other_has_high_cards = False
        if self.thres <= higest_card_value_so_far:
            me_think_other_has_high_cards = True
                
        
        # Condition B
        me_need_to_draw_more = False
        if card_val < self.thres:
            me_need_to_draw_more = True
            
       
        # condition C
        me_meet_my_lower_thres = False
        if self.thres_low <= card_val:
            me_meet_my_lower_thres = True
        
        
        rule1 = me_think_other_has_high_cards and (not me_meet_my_lower_thres)
        rule2 = (not me_think_other_has_high_cards) and me_need_to_draw_more
        
         
        is_mathematically_safe = False
        if safe_odd > self.safe_zone:
            is_mathematically_safe = True
            
            
        conclusion = (rule1 or rule2) and is_mathematically_safe
        
        return conclusion
        

    def clear_cards(self):
        
        self.is_busted = False
        self.win_21 = False
        del self.cards[:]
        
