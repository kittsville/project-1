import pygame       # Handles user input and game output
import sys          # Used to quit game
import lib.matrix   # Generates game grid
import lib.player   # Manages player position and properties

''''To create an instance of a class from the library call it from its parent file and directory
e.g. to call the Matrix class you need to do do myInstance = lib.matrix.Matrix
I'm liking Python less by the minute'''



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
