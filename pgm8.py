# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm8.py
# Purpose: A program to simulate a rectangle in an elliptical orbit around a centre point

import pygame, sys, random, time, math
from pygame.locals import *

# start the pygame engine
pygame.init()

# create the display window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
display_surface = pygame.display.set_mode((WINDOWWIDTH,
                                           WINDOWHEIGHT))
# screen centre - added
X_center = WINDOWWIDTH//2
Y_center = WINDOWHEIGHT//2
earth_rad = 50 # added

# Set the title of the display window
pygame.display.set_caption('Eliptical orbit around a centre point')

# define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0, 0, 255) # added

# create a single rectangle (satellite) to display
satellite = {}
satellite['sprite'] = pygame.Rect(0, 0, random.randint(1, 10), random.randint(1, 10))
satellite['colour'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
satellite['angle'] = random.randint(0, 360)
satellite['X_ellipse'] = random.randint(100, 200) # X_ellipse is major radius of ellipsis
satellite['Y_ellipse'] = random.randint(100, 200) # Y_ellipse is minor radius of ellipsis

# run the game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill(BLACK)

    rectangle = satellite['sprite']
    degree = satellite['angle']
    major_rad = satellite['X_ellipse']
    minor_rad = satellite['Y_ellipse']
    
    rectangle.x = int(math.cos(degree * 2 * math.pi/360) * major_rad) + X_center 
    rectangle.y = int(math.sin(degree * 2 * math.pi/360) * minor_rad) + Y_center 

    satellite['angle'] += 1

    # Now display the satellite
    pygame.draw.rect(display_surface, satellite['colour'], rectangle)
    
    # draw circle in center of screen - Earth
    pygame.draw.circle(display_surface, BLUE, [WINDOWWIDTH//2, WINDOWHEIGHT//2], 50)

    # update the display surface with drawn object(s)
    pygame.display.update()
    time.sleep(0.01)



