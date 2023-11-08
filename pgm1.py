# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm1.py
# Purpose: Getting started with pygame

# My first pygame program
import pygame, sys, random, time
from pygame.locals import *

# start the pygame engine
pygame.init()

# create the display window
display_surface = pygame.display.set_mode((400, 300))

# Set the title of the display window
pygame.display.set_caption('My first pygame program')


# run the game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
