import sys
import pygame
from rocket import Rocket
from actions import update

def run_game():
    """This will start the game play"""
    pygame.init()
    screen = pygame.display.set_mode((600,800))
    pygame.display.set_caption("Rocket game")
    
    bg_color = (255, 255, 255)
    
    rocket = Rocket(screen)
    
    
    while True:
        #Creating the main loop of the game
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: sys.exit()
            
            #sending to the action function to do what i did below
        update(rocket)
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     #Make the ship go to the left
#                     print("LEFT")
#                 elif event.key == pygame.K_RIGHT:
#                     #Make the ship go to the right
#                     print("RIGHT")
#                 elif event.key == pygame.K_UP:
#                     #Make the ship go fly up
#                     print("UP")
#                 elif event.key == pygame.K_DOWN:
#                     #Make the ship go down
#                     print("DOWN")
#                     
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT:
#                     #Make the ship go to the left
#                     print("LEFT")
#                 elif event.key == pygame.K_RIGHT:
#                     #Make the ship go to the right
#                     print("RIGHT")
#                 elif event.key == pygame.K_UP:
#                     #Make the ship go fly up
#                     print("UP")
#                 elif event.key == pygame.K_DOWN:
#                     #Make the ship go down
#                     print("DOWN")
            
        #Color the screen
        screen.fill(bg_color)
#         rocket.blitme()
#     
#         #this is to make the drawing visable
#         pygame.display.flip()
#         
    
run_game()

