'''
Created on Oct 20, 2017

@author: jaroszyn
'''
import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from star import Star


def run_project():
    """This is the main loop for the Star Grid project"""
    pygame.init()
    env_settings = Settings()
    screen = pygame.display.set_mode(
        (env_settings.screen_width, env_settings.screen_height))
    pygame.display.set_caption("Star Map")

    # Make a new star object
    star = Star(env_settings, screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(env_settings.bg_color)

        # screen.fill(env_settings.bg_color)
        star.blitme()
        pygame.display.flip()


run_project()
