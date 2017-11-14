'''
Created on Oct 19, 2017

@author: jaroszyn
'''


class GameStats():
    '''
    Track statistics for Alien Invasion.
    '''

    def __init__(self, ai_settings):
        '''
        Initialize statistics.
        '''
        self.ai_settings = ai_settings
        self.reset_status()

        # Start alien invasion in an active state
        self.game_active = False

    def reset_status(self):
        """Initialize stats that can change during the game.
        """
        self.ship_left = self.ai_settings.ship_limit
