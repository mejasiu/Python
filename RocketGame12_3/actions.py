import sys
import pygame

def key_down(event, rocket):
    if event.key == pygame.K_LEFT:
        #Make the ship go to the left
        print("LEFT")
        rocket.is_moving_left = True
    elif event.key == pygame.K_RIGHT:
        #Make the ship go to the right
        print("RIGHT")
        rocket.is_moving_right = True
    elif event.key == pygame.K_UP:
        #Make the ship go fly up
        print("UP")
        rocket.is_moving_up = True
    elif event.key == pygame.K_DOWN:
        #Make the ship go down
        print("DOWN")
        rocket.is_moving_down = True
                
                    
def key_up(event, rocket):    
    if event.key == pygame.K_LEFT:
        # Make the ship go to the left
        print("LEFT")
        rocket.is_moving_left = False
    elif event.key == pygame.K_RIGHT:
        # Make the ship go to the right
        print("RIGHT")
        rocket.is_moving_right = False
    elif event.key == pygame.K_UP:
        # Make the ship go fly up
        print("UP")
        rocket.is_moving_up = False
    elif event.key == pygame.K_DOWN:
        # Make the ship go down
        print("DOWN")
        rocket.is_moving_down = False
        

def update(rocket):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
            
        if event.type == pygame.KEYDOWN:
            key_down(event, rocket)
        elif event.type == pygame.KEYUP:
            key_up(event, rocket)
            
    rocket.update_rocket()
                
            
    
    rocket.blitme()
    #this is to make the drawing visable
    pygame.display.flip()
