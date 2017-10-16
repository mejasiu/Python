"""
In this program I will be adding the functionality of 12-5.  At this point I do not see a point
 to re-write the whole code since I did it already in 12-3.  I will add the functionality here to
 show that i understand the concept of what we did.
"""

import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    #bg_color = (230, 230, 230)
    
    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()
    #my test to see how many bullets on the screen
   # bullet_count = 0
    # Start the main loop for the game.
    while True: 
        
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets,screen)
#         bullets.update()
#         
#          #Get rid of bullets that have disappeared
#         for bullet in bullets.copy():
#             #bullet_count += 1 
#             if bullet.rect.left >= ai_settings.screen_width:
#                 bullets.remove(bullet)
#                 #bullet_count -= 1
#                 
#         print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()