'''
Created on Oct 20, 2017

@author: jaroszyn
'''


class Settings():
    """This class will keep all settings for the stargrid"""

    def __init__(self):
        # Screen
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Star
        self.star_size_factor = 5
