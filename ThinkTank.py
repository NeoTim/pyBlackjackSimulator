

class ThinkTank(object):
    
    '''need to test/improve this value'''
    
    @classmethod
    def cal_bet_low_by_position(cls, x, min_bet=10):
        return {
            # 0: 17, # NO dealer
            1: min_bet,
            2: 2*min_bet,
            3: 3*min_bet,
            4: 5*min_bet,
            5: 5*min_bet,
            6: 5*min_bet,
            7: 5*min_bet, # 7 seats total
        }.get(x, -1) # Default: Error
    
    
    @classmethod
    def cal_safe_zone_by_position(cls, x):
        return {
            # 0: 17, # NO dealer
            1: 0.19, # A
            2: 0.24, # B
            3: 0.29, # C
            4: 0.33, # D
            5: 0.33,
            6: 0.33,
            7: 0.33, # 7 seats total
        }.get(x, -1) # Default: Error
    
    @classmethod
    def cal_draw_thres_high_by_position(cls, x):
        return {
            0: 17, # DEALER.player shall not use this value anyway
            1: 20,
            2: 19,
            3: 18,
            4: 17,
            5: 16,
            6: 15,
            7: 15, # 7 seats total
        }.get(x, 21) # Default, 21, keep drawing...
    
    
    @classmethod
    def cal_draw_thres_low_by_position(cls, x):
        return {
            0: 17, # dealer, will keep on drawing card less than this number
            1: 17, # Antai
            2: 16, # Bob
            3: 15, # Chris
            4: 15, # Dan
            5: 15,
            6: 15,
            7: 15, # 7 seats total
        }.get(x, 21) # Default, 21, keep drawing...
    
    

    