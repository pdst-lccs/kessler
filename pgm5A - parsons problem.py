# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm5A-parsons problem.py
# Purpose: Solution to programming task 5 (Parson's problem)
# This program create multiple moving rectangles all bouncing off the edges in sync.

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
pygame.display.set_caption('Moving squares that bounce')

# define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# create multiple rectangles to display
rectangles = []
for _ in range(10):
    x = random.randint(0, WINDOWWIDTH)
    y = random.randint(0, WINDOWHEIGHT)
    rectangle = pygame.Rect(x, y, 20, 20)
    pygame.draw.rect(display_surface, WHITE, rectangle)
    rectangles.append(rectangle)

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

    # Perform the animation on each rectangle
    for rectangle in rectangles:
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


