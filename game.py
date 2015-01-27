import pygame               # Handles user input and game output
import sys                  # System specific parameters and functions
sys.path.insert(0, 'lib/')  # Adds class library as first directory searched when importing
import matrix               # Generates game grid
import player               # Manages player position and properties

# To call a class from the library call it from its parent file e.g. matrix.Matrix(5, 5)

# Allows you to access stuff like KEYDOWN directly rather than via pygame.KEYDOWN
from pygame.locals import *

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption("Wumpus World Simulation")

WHITE = (255, 255, 255)

clock = pygame.time.Clock()

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print 'here'
            pygame.display.quit()
            sys.exit()

    # Clear screen
    screen.fill(WHITE)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()
