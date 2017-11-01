'''
Created on Oct 27, 2017

@author: jaroszyn
'''
import sys
import pygame
from pygame.sprite import Sprite


class Drop(Sprite):
    """This class will create a rain droplet"""

    def __init__(self, settings, screen, drop_color, drop_speed):
        """These are known variables of rain"""
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.position_x = 0
        self.position_y = 0
        self.drop_color = drop_color
        self.drop_speed = drop_speed

    def draw_rain_drop(self):
        """Creating drop on the screen"""
        pygame.draw.rect(
            self.screen, self.drop_color, (self.position_x, self.position_y, self.settings.drop_width, self.settings.drop_height), 0)

    def move_droplet(self):
        """Moving drop down the screen"""
        self.position_y = (1 * self.drop_speed) + self.position_y
