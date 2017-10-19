import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    #bg_color = (230, 230, 230)
    
    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    #alien = Alien(ai_settings, screen)
    
    # Make a group to store bullets in
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    #my test to see how many bullets on the screen
   # bullet_count = 0
    # Start the main loop for the game.
    while True:
        
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)
        
           
#         bullets.update()
#         
#         #Get rid of bullets that have disappeared
#         for bullet in bullets.copy():
#             #bullet_count += 1 
#             if bullet.rect.bottom <= 0:
#                 bullets.remove(bullet)
#                 #bullet_count -= 1
                
        #print(len(bullets))

run_game()