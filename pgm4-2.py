# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm4-2.py (program 4.2)
# Purpose: A program to simulate a single moving rectangle (diagonal and disappears off the edges)

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
pygame.display.set_caption('Moving square')

# define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# create a rectangle to display at (0,0)
rectangle = pygame.Rect(0, 0, 20, 20)
pygame.draw.rect(display_surface, WHITE, rectangle)

# declare movement variables
MOVESPEED = 1
move_down = True
move_left = False

# run the game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Perform the animation
    if move_down:
        rectangle.bottom = rectangle.bottom + MOVESPEED
    else:
        rectangle.bottom = rectangle.bottom - MOVESPEED

    if move_left:
        rectangle.left = rectangle.left - MOVESPEED
    else:
        rectangle.left = rectangle.left + MOVESPEED

    display_surface.fill(BLACK)
    pygame.draw.rect(display_surface, WHITE, rectangle) # white

    # update the display surface with drawn object(s)
    pygame.display.update()
    time.sleep(0.01)
