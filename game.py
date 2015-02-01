import pygame               # Handles user input and game output
import sys                  # System specific parameters and functions
sys.path.insert(0, 'lib/')  # Adds class library as first directory searched when importing
import matrix               # Generates game grid
import player               # Manages player position and properties
import menu                 # Generates menu displayed at game launch and if game is paused

# To call a class from the library call it from its parent file e.g. matrix.Matrix(5, 5)

# Allows you to access stuff like KEYDOWN directly rather than via pygame.KEYDOWN
from pygame.locals import *

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption("Wumpus World Simulation")

# Sets game background colour, feel free to change!
global BACKGROUND
BACKGROUND = (42, 42, 42)

screen.fill(BACKGROUND)

clock = pygame.time.Clock()

# Creates all game menus (currently just start menu)
startMenu = menu.Menu(['Start','Options','Quit'], screen)

# Activates start menu, so it displays on game start up
startMenu.active = True

# Allows held keys to act as multiple key presses. After 200ms delay, every 69ms the held key will generate a new key press
pygame.key.set_repeat(199,69)

pygame.display.update()

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print 'Quiting Game'
            pygame.display.quit()
            sys.exit()
        
        # If user is currently in start menu
        if startMenu.active:
            if event.type == KEYDOWN:
                # Updates selected menu item based on key press
                startMenu.updateSelectedItem( event.key )
                
                # If Enter was pressed, performs action of currently selected menu item
                if event.key == K_RETURN:
                    # Gets currently selected menu item
                    selectedMenuItem = startMenu.getSelectedMenuItem()
                    
                    # If start was selected, launch game
                    if selectedMenuItem == 0:#here is the Menu class function
                        print 'Start selected'
                    
                    # If options were selected, loads options menu
                    elif selectedMenuItem == 1:
                        print 'Options selected'
                    
                    # If quit was selected, quits game
                    elif selectedMenuItem == 2:
                        pygame.display.quit()
                        sys.exit()
            
            startMenu.draw()        
            pygame.display.update()
        else:
            # Clear screen
            screen.fill(BACKGROUND)

            # Flip screen
            pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()
