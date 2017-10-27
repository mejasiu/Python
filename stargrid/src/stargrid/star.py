'''
Created on Oct 20, 2017

@author: jaroszyn
'''
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class to represent a single star in the grid
    """

    def __init__(self, env_settings, screen):
        """Initialize the star onto the screen
        """
        super().__init__()
        self.screen = screen
        self.ai_setting = env_settings

        # Load the star image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.image_size = self.image.get_rect()
        # Creates a smaller star
        self.image = pygame.transform.scale(
            self.image, (int(self.image_size.width / env_settings.star_size_factor), int(self.image_size.height / env_settings.star_size_factor)))
        self.rect = self.image.get_rect()

        # start each new star near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the star's exact postion.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the stars at the current location
        """
        self.screen.blit(self.image, self.rect)
