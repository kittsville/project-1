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

# create sprites list which the player will be added to
active_sprites = pygame.sprite.Group()

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
            
            # If user has pressed Enter, perform action of whichever menu item was selected
            if (event.type == KEYDOWN and event.key == K_RETURN) or event.type == MOUSEBUTTONDOWN:
                # Fetches menu item selected when enter was pressed, or menu item that was clicked
                selectedMenuItem = startMenu.getSelectedMenuItem( event )
                
                # If start was selected, launch game
                if selectedMenuItem is 0:
                    # Turns off start menu
                    startMenu.active = False
                    
                    # Generates game grid
                    gameGrid = matrix.Matrix(8, 8, screen)
                    
                    # From here on, grid is ready for player
                    # Need to add ability to set player location using mouse

                    # Create player at the x, y location on the grid
                    thePlayer = player.Player(0, 0, gameGrid)
                    # Add player to active spirtes list
                    active_sprites.add(thePlayer)
                
                # If options were selected, loads options menu
                elif selectedMenuItem is 1:
                    print 'Options selected'
                
                # If quit was selected, quits game
                elif selectedMenuItem is 2:
                    pygame.display.quit()
                    sys.exit()
            
            startMenu.draw()        
            pygame.display.update()
        else:
            # player movement
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    thePlayer.moveUp()
                elif event.key == K_DOWN:
                    thePlayer.moveDown()
                elif event.key == K_LEFT:
                    thePlayer.moveLeft()
                elif event.key == K_RIGHT:
                    thePlayer.moveRight()

                # update player location
                thePlayer.update()

            # Clear screen
            screen.fill(BACKGROUND)

            # Draws current game grid to screen, necessary to keep it displayed to propagate updates to player position
            gameGrid.draw()

            # draw all active sprites
            active_sprites.draw(screen)

            # Flip screen
            pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()
