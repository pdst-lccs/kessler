# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm2A-red+green+blue.py
# Purpose: Solution to Programming Exercises Q3
# Display a red, green and blue square on a black background

import pygame, sys, random, time
from pygame.locals import *

# start the pygame engine
pygame.init()

# create the display window
display_surface = pygame.display.set_mode((400, 300))

# Set the title of the display window
pygame.display.set_caption('Coloured rectangles')

# create a rectangle to display
rectangle = pygame.Rect(0, 0, 50, 50)
pygame.draw.rect(display_surface, (255,0,0), rectangle) #red
rectangle = pygame.Rect(50, 0, 50, 50)
pygame.draw.rect(display_surface, (0,255,0), rectangle) #green
rectangle = pygame.Rect(100, 0, 50, 50)
pygame.draw.rect(display_surface, (0,0,255), rectangle) #blue

# run the game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # update the display surface with drawn object(s)
    pygame.display.update()



