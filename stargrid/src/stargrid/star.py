'''
Created on Oct 20, 2017

@author: jaroszyn
'''
import pygame
#from pygame.sprite import Sprite


class Star():
    """A class to represent a single alien in the fleet
    """

    def __init__(self, env_settings, screen):
        """Initialize the alien and set its starting point
        """
        # super().__init__()
        self.screen = screen
        self.ai_setting = env_settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact postion.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at the current location
        """
        self.screen.blit(self.image, self.rect)
