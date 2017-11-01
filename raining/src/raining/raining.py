'''
Created on Oct 27, 2017
This code will make rain fall from the top to the bottom of the screen
@author: jaroszyn
'''
import pygame
import sys

from pygame.sprite import Group
from rain_settings import Settings
#from rain_drop import Drop
#from random import randint
import rain_functions as rf


def run_project():
    """This is the main loop for the Star Grid project"""
    pygame.init()
    rain_settings = Settings()
    screen = pygame.display.set_mode(
        (rain_settings.screen_width, rain_settings.screen_height))
    pygame.display.set_caption("Raining")

    # Make a rain droplet
    # droplet = Drop(rain_settings, screen)

    raining_drops = Group()

    # We will make this a more gray color
    background_drops = Group()
    # gray
    gray_drop_color = (200, 200, 200)

    # Create star map
    #strfunc.createStarfeild(stars, screen, env_settings)
    position_x = 0
    position_y = 0

    # Random position of the rain drop falling
    # position_x = randint(0, rain_settings.screen_width)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(rain_settings.bg_color)

        rf.makeItRain(rain_settings, screen,
                      raining_drops, rain_settings.drop_color, rain_settings.drop_speed)
        rf.makeItRain(rain_settings, screen, background_drops,
                      gray_drop_color, 0.75)
        rf.drawDroppetMoveDownScreen(raining_drops)
        rf.drawDroppetMoveDownScreen(background_drops)
        rf.removeDroppletsFromMemory(raining_drops, rain_settings)
        rf.removeDroppletsFromMemory(background_drops, rain_settings)

        pygame.display.update()
        pygame.display.flip()


run_project()
