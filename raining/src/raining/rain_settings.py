'''
Created on Oct 27, 2017

@author: jaroszyn
'''


class Settings():
    """This class will keep all settings for the rain"""

    def __init__(self):
        # Screen
        self.screen_width = 600
        self.screen_height = 900
        self.bg_color = (255, 255, 255)

        # Droplet
        self.drop_width = 2
        self.drop_height = 11
        # default speed
        self.drop_speed = 1
        # slower speed
        self.slower_drop_speed = 0.75
        # black
        self.drop_color = (0, 0, 0)
        # gray color
        self.gray_drop_color = (200, 200, 200)

        # Rain
        self.drop_count = 800
