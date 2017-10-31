'''
Created on Oct 27, 2017

@author: jaroszyn
'''
import sys
import pygame
import raining
from pygame.sprite import Sprite
from random import randint


class Drop(Sprite):
    """This class will create a rain droplet"""

    def __init__(self, settings, screen):
        """These are known variables of rain"""
        super().__init__()
        self.settings = settings
        self.screen = screen

    def draw_rain_drop(self, position_x, position_y):
        """Creating drop on the screen"""
        pygame.draw.rect(
            self.screen, self.settings.drop_color, (position_x, position_y, self.settings.drop_width, self.settings.drop_height), 0)

    def move_droplet(self):
        """Moving drop down the screen"""
        self.position_y += 1
        return self.position_y

    def make_it_rain(self, settings, screen, raining_drops):
        """This function will create rain that fall from the sky"""
        # This will have to be a function outside of Rain_drop because I would have to have a
        # Rain drop object to be able to make it rain, but since the make_it_rain object already
        # Creates droplets than it does not need to be here.

        for drops in range(settings.drop_count):
            # make the droplet
            droplet = Drop(settings, screen)
            # Set the position
            position_x = randint(0, settings.screen_width)
            position_y = 0
            droplet.draw_rain_drop(position_x, position_y)
            raining_drops.add(droplet)
