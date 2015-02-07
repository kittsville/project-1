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

gamePaused = True

#Whether or not the player has set a location for his robot

playerPlaced = False

# Creates all game menus (currently just start menu)
startMenu = menu.Menu(['Start','Options','Quit'], screen)

# Activates start menu, so it displays on game start up
startMenu.active = True

# Allows held keys to act as multiple key presses. After 200ms delay, every 69ms the held key will generate a new key press
pygame.key.set_repeat(199,69)

# create sprites list which the player will be in
active_sprites = pygame.sprite.Group()

pygame.display.update()

def drawInfo(output, outputLocation):
    currentFont = pygame.font.Font(startMenu.fontPath, startMenu.fontSize)
    outputText = currentFont.render(output,1, startMenu.textColour, BACKGROUND)
    screen.blit(outputText, outputLocation)

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
                    gamePaused = False
                    # Generates game grid
                    gameGrid = matrix.Matrix(8, 8, screen)
                
                # If options were selected, loads options menu
                elif selectedMenuItem is 1:
                    print 'Options selected'
                
                # If quit was selected, quits game
                elif selectedMenuItem is 2:
                    pygame.display.quit()
                    sys.exit()
            
            startMenu.draw()        
            pygame.display.update()
        elif(playerPlaced == True):
            # player movement
            if event.type == KEYDOWN and gamePaused == False:
                if event.key == K_UP:
                    player.moveUp()
                elif event.key == K_DOWN:
                    player.moveDown()
                elif event.key == K_LEFT:
                    player.moveLeft()
                elif event.key == K_RIGHT:
                    player.moveRight()

                # update player location
                player.update()

            # Clear screen
            screen.fill(BACKGROUND)

            # Draws current game grid to screen, necessary to keep it displayed to propagate updates to player position
            gameGrid.draw()

            # draw player
            active_sprites.draw(screen)

            # Flip screen
            pygame.display.flip()


        elif playerPlaced == False:
            # Clear screen
            screen.fill(BACKGROUND)

            # Draws current game grid to screen, necessary to keep it displayed to propagate updates to player position
            gameGrid.draw()
            drawInfo("Please place your robot!", (gameGrid.pixelWidth, gameGrid.pixelHeight))
                
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                
                pos = ( event.pos[0], event.pos[1])
        
                # Loops through grid squares, checking if click occurred in squares's area
                for x in xrange(gameGrid.):
                    for
                    if self.menuItemObjects[i].itemRect.collidepoint( pos ):
                         

    # Pause
    clock.tick(60)

pygame.quit()
