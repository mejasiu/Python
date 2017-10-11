import pygame

class Rocket():
    """This will create a rocket object"""
    
    def __init__(self, screen):
        """Creating Rocket attributes"""
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_moving_up = False
        self.is_moving_down = False
        self.screen = screen
        
        #load ship image into its rectangle
        #I should look into how other progammers do this
        self.image = pygame.image.load('image/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (100, 200))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Location of the ship
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        """Draw the ship in its current location"""
        self.screen.blit(self.image, self.rect)
        
    def move_rocket_right(self):
        self.rect.centerx += 1
    def move_rocket_left(self):
        self.rect.centerx -= 1
    def move_rocket_up(self):
        self.rect.bottom -= 1
    def move_rocket_down(self):
        self.rect.bottom += 1
        
    def update_rocket(self):
        if self.is_moving_left and self.rect.left >= self.screen_rect.left:
            self.move_rocket_left()
        elif self.is_moving_right and self.rect.right <= self.screen_rect.right:
            self.move_rocket_right()
        elif self.is_moving_up and self.rect.top >= self.screen_rect.top:
            self.move_rocket_up()
        elif self.is_moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.move_rocket_down()