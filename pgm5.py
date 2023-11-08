# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm5.py
# Purpose: A program to simulate a single moving rectangle that bounces off the edges

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
pygame.display.set_caption('Moving square (bounces)')

# define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# create a rectangle to display at (0,0)
x = random.randint(0, WINDOWWIDTH)
y = random.randint(0, WINDOWHEIGHT)
rectangle = pygame.Rect(x, y, 20, 20)
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

    display_surface.fill(BLACK)

    # Perform the vertical animation
    if move_down:
        if rectangle.bottom >= WINDOWHEIGHT:
            move_down = False
        else:
            rectangle.bottom = rectangle.bottom + MOVESPEED
    else:
        if rectangle.top <= 0:
            move_down = True
        else:
            rectangle.top = rectangle.top - MOVESPEED

    # Perform the horizontal animation
    if move_left:
        if rectangle.left <= 0:
            move_left = False
        else:
            rectangle.left = rectangle.left - MOVESPEED
    else:
        if rectangle.right >= WINDOWWIDTH:
            move_left = True
        else:
            rectangle.right = rectangle.right + MOVESPEED

    pygame.draw.rect(display_surface, WHITE, rectangle)

    # update the display surface with drawn object(s)
    pygame.display.update()
    time.sleep(0.01)

