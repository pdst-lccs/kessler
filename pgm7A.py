# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm7A.py
# Purpose: Solution to programming task 7A
# This program simulates a disintegration effect ...
# ... when two squares collide one of them diminishes in size

# Program 7A - collision detection - bounce and diminish in size by half
import pygame, sys, random, time
from pygame.locals import *

# start the pygame engine
pygame.init()

# create the display window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
display_surface = pygame.display.set_mode((WINDOWWIDTH,
                                           WINDOWHEIGHT))

# Set the title of the display window
pygame.display.set_caption('Collision detection - bounce and disintegrate')

# define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# create a list of dictionaries
satellites = []
for count in range(5):
    x = random.randint(0, WINDOWWIDTH)
    y = random.randint(0, WINDOWHEIGHT)
    
    satellite = {}
    satellite['sprite'] = pygame.Rect(x, y, 20, 20)
    satellite['h_speed'] = random.randint(1, 2)
    satellite['v_speed'] = random.randint(1, 2)
    satellite['move_down'] = random.choice([True,False])
    satellite['move_left'] = random.choice([True,False])
    
    satellites.append(satellite)

# run the game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill(BLACK)

    for satellite in satellites:
        
        rectangle = satellite['sprite']

        # Perform the vertical animation
        if satellite['move_down']:
            if rectangle.bottom >= WINDOWHEIGHT:
                satellite['move_down'] = False
            else:
                rectangle.bottom = rectangle.bottom + satellite['v_speed']
        else:
            if rectangle.top <= 0:
                satellite['move_down'] = True
            else:
                rectangle.top = rectangle.top - satellite['v_speed']
                
        # Perform the horizontal animation
        if satellite['move_left']:
            if rectangle.left <= 0:
                satellite['move_left'] = False
            else:
                rectangle.left = rectangle.left - satellite['h_speed']
        else: 
            if rectangle.right >= WINDOWWIDTH:
                satellite['move_left'] = True
            else:
                rectangle.right = rectangle.right + satellite['h_speed']

        # Collision detection ...
        for sat in satellites:
            # If the objects are not the same and there is overlap ...
            if sat['sprite'] != rectangle and rectangle.colliderect(sat['sprite']):
                
                # ... simulate a bounce effect
                satellite['move_left'] = not satellite['move_left'] #random.choice([True,False])
                satellite['move_down'] = not satellite['move_down'] #random.choice([True,False])
                
                # ... simulate disintegration
                rectangle.height = rectangle.height//2
                rectangle.width = rectangle.width//2

        pygame.draw.rect(display_surface, WHITE, rectangle)

    # update the display surface with drawn object(s)
    pygame.display.update()
    time.sleep(0.01)



