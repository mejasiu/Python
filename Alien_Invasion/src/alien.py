import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet
    """
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting point
        """
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_settings
        
        #Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Store the alien's exact postion.
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the alien at the current location
        """
        self.screen.blit(self.image, self.rect)
    
    def check_edge(self):
        """Move the alien right or left.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """Move alien to the right
        """
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        # alien position
        self.rect.x = self.x
    
    