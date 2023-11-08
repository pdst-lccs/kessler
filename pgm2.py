# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm2.py
# Purpose: Display a single rectangle (square) in the pygame window

import pygame, sys, random, time
from pygame.locals import *

# start the pygame engine
pygame.init()

# create the display window
display_surface = pygame.display.set_mode((400, 300))

# Set the title of the display window
pygame.display.set_caption('A single white rectangle')

# create a rectangle to display
x = random.randint(0, 400)
y = random.randint(0, 300)
rectangle = pygame.Rect(x, y, 20, 20)
pygame.draw.rect(display_surface, (255, 255, 255), rectangle) # white

    
# run the game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # update the display surface with drawn object(s)
    pygame.display.update()
