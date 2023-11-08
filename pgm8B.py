# Project: Educational resources to promote launch of EIRSAT-1 ...
# ... Ireland's first ever sattelite to  be launched into space.
# Date: September 2023
# Author: Joe English, Oide
# eMail: computerscience.pdst@oide.ie
# Program Name: pgm8B.py
# Purpose: A program to simulate the Kessler effect

import pygame, sys, random, time, math
from pygame.locals import *

# set up pygame
pygame.init()

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
pygame.display.set_caption('Eirsat-1: Kessler effect demo')
screen.fill(BLACK)
area = screen.get_rect()
#print(area)
WINDOWWIDTH =  area.width
WINDOWHEIGHT =  area.height

# centers of screen
X_center = WINDOWWIDTH//2
Y_center = WINDOWHEIGHT//2
earth_rad = 50

sats = [] # junk??
for count in range(100):
    satellite = {}
    satellite['sprite'] = pygame.Rect(0, 0, random.randint(1, 10), random.randint(1, 10)) # random sizes (maybe) and orientation
    satellite['colour'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    satellite['angle'] = random.randint(0, 360)
    satellite['X_ellipse'] = random.randint(100, 200) # X_ellipse is major radius of ellipsis
    satellite['Y_ellipse'] = random.randint(100, 200) # Y_ellipse is minor radius of ellipsis
    sats.append(satellite)
    # need to give each object a random direction and speed


# run the game loop
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_x:
            sys.exit(0)

    # draw the black background onto the surface
    screen.fill(BLACK)
    
    for satellite in sats:
        
        block = satellite['sprite']
        degree = satellite['angle']
        major_rad = satellite['X_ellipse']
        minor_rad = satellite['Y_ellipse']
        
        block.x = int(math.cos(degree * 2 * math.pi/360) * major_rad) + X_center 
        block.y = int(math.sin(degree * 2 * math.pi/360) * minor_rad) + Y_center 
    
        satellite['angle'] += 1
        
        # START KESSLER
        for sat in sats:
            if sat['sprite'] != block and block.colliderect(sat['sprite']): # COLLISION!!
                #print("HIT!")
                
                ## START - split the debris
                satellite['colour'] = (255,0,0)
                block.height = block.height//2
                block.width = block.width//2
                
                debris = {} # create a 
                debris['sprite'] = block.copy()
                debris['colour'] = RED
                debris['angle'] = satellite['angle'] #random.randint(0, 360)
                debris['X_ellipse'] = major_rad #random.randint(100, 200) # X_ellipse is major radius of ellipsis
                debris['Y_ellipse'] = minor_rad #random.randint(100, 200) # Y_ellipse is minor radius of ellipsis
                sats.append(debris)
        # END KESSLER

        # Now display
        pygame.draw.rect(screen, satellite['colour'], block) # 1 or 2 for fill/no fill
    
    # end for

    # draw circle in center of screen - Earth
    pygame.draw.circle(screen, BLUE, [X_center, Y_center], earth_rad)
    
    # render the screen object
    pygame.display.update()
        
    time.sleep(0.02)

