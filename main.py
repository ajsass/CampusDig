# Import necessary modules
import pygame
from pygame.locals import *
import random
import math

from logic import logic

# Initialize pygame
pygame.init()

# Set screen width and height
width = 1000
height = 700

# Create the screen
screen = pygame.display.set_mode((width, height))

# Set the title and icon
pygame.display.set_caption("Campus Dig!")


#digg = Digscreen()
logi = logic()
down = False

#clock
clock = pygame.time.Clock()
# Game loop
while True:
    
    dig = False
    
    clock.tick(120)
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the user closes the window
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Get the pressed keys
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[K_UP]:
        dig = True
        
    mX,mY = pygame.mouse.get_pos()
    m1,m2,m3 = pygame.mouse.get_pressed(num_buttons=3)

    if m1 == True:
        down = True
    if down == True and m1 == False:
        dig = True
        down = False
    
    # Draw the background
    screen.fill((255, 255, 255))
    logi.draw(screen,pressed_keys,mX,mY,dig)
    #digg.tick(screen,pressed_keys,mX,mY,dig)

    
    
    # Update the display
    pygame.display.update()
    pygame.display.flip()