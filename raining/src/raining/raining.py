'''
Created on Oct 27, 2017
This code will make rain fall from the top to the bottom of the screen
@author: jaroszyn
'''
import pygame
import sys

from pygame.sprite import Group
from rain_settings import Settings
from rain_drop import Drop
from random import randint


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

        # Draw starts on the screen
        # stars.draw(screen)

        droplet.draw_rain_drop(position_x, position_y)
        position_y += 1

        pygame.display.update()
        pygame.display.flip()


run_project()
