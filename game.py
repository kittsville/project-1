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
screen = pygame.display.set_mode((600, 400))

# Set the title of the window
pygame.display.set_caption("Wumpus World Simulation")

# Sets game background colour, feel free to change!
global BACKGROUND
BACKGROUND = (42, 42, 42)

screen.fill(BACKGROUND)

clock = pygame.time.Clock()

gamePaused = True

# Whether or not the player has set a location for his robot
playerPlaced = False

# Creates all game menus (currently just start menu)
startMenu = menu.Menu(['Start','Quit'], screen)

# Activates start menu, so it displays on game start up
startMenu.active = True

# Allows held keys to act as multiple key presses.
# After 200ms delay, every 69ms the held key will generate a new key press
pygame.key.set_repeat(199,69)

# create sprites list which the player will be added to
active_sprites = pygame.sprite.Group()

pygame.display.update()

totalTime =  60

currentTime = totalTime

frames = 0

# Current grid size, incremented with each level
gridSize = 14

#draws the provided string to a given location on a surface by first getting the games font from the menu class
#then by creating another surface on which to write the text
#the new surface is then placed in the specified spot.
def drawInfo(output, outputLocation):
    currentFont = pygame.font.Font(startMenu.fontPath, startMenu.fontSize)
    outputText = currentFont.render(output,1, startMenu.textColour, BACKGROUND)
    screen.blit(outputText, outputLocation)

# Resizes window to accommodate new grid size
def resizeWindow(gameGrid):
    width   = gameGrid.pixelWidth
    height  = gameGrid.pixelHeight + 45 # Adds height to include 'Place robot/time left'
    
    pygame.display.set_mode((width, height))
    
    

# Main game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        
        # If user is currently in start menu
        if startMenu.active:
            if event.type == KEYDOWN:
                # Updates selected menu item based on key press
                startMenu.updateSelectedItem( event.key )

            # update selected menu item based on mouse position if there is any mouse movement
            if pygame.mouse.get_rel() != (0, 0):
                mousePos = pygame.mouse.get_pos()
                startMenu.updateSelectedItemMouse(mousePos)

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
                    gameGrid = matrix.Matrix(gridSize, gridSize, screen)
                    resizeWindow(gameGrid)
                    currentTime = totalTime
                
                # If quit was selected, quits game
                elif selectedMenuItem is 1:
                    pygame.display.quit()
                    sys.exit()

            # removes board after game finishes.
            screen.fill(BACKGROUND)
            startMenu.draw()        
            pygame.display.update()
        elif playerPlaced:
            # get player location
            playerX, playerY = thePlayer.getLocation()

            # if there is a star at players location collect it
            if gameGrid.isStar(playerX, playerY):
                gameGrid.grid[playerY][playerX] = 0
                gameGrid.starCount -= 1

            # if players location is the goal and all stars been collected. Level is completed and new must begin
            if gameGrid.isGoal(playerX, playerY) and gameGrid.starCount == 0:
                active_sprites.remove(thePlayer)
                playerPlaced = False
                
                # Deletes completed levels game grid
                del gameGrid
                
                # Reduces time available to complete game in and increases game grid size
                totalTime   -= 4
                gridSize    += 1
                
                # Generates game grid
                gameGrid = matrix.Matrix(gridSize, gridSize, screen)
                resizeWindow(gameGrid)
                currentTime = totalTime

            # player movement
            if event.type == KEYDOWN and not gamePaused:
                if event.key == K_UP:
                    thePlayer.changeY = -1
                elif event.key == K_DOWN:
                    thePlayer.changeY = 1
                elif event.key == K_LEFT:
                    thePlayer.changeX = -1
                elif event.key == K_RIGHT:
                    thePlayer.changeX = 1

                # update player location
                thePlayer.update()

            if event.type == MOUSEBUTTONDOWN:
                # position of mouse click
                pos = (event.pos[0], event.pos[1])
        
                # Loops through grid squares, checking if click occurred in squares's area
                for y in xrange(gameGrid.Height):
                    row = gameGrid.gridObjects[y]
                    for x in xrange(gameGrid.Width):
                        if row[x].collidepoint(pos):
                            thePlayer.changeX = y - playerX
                            thePlayer.changeY = x - playerY
                            if(-1 <= thePlayer.changeX <= 1) and (-1 <= thePlayer.changeY <= 1):
                                thePlayer.update()
                            else:
                                thePlayer.changeY = 0
                                thePlayer.changeX = 0

            # Clear screen
            screen.fill(BACKGROUND)

            # Draws current game grid to screen, necessary to keep it displayed to propagate updates to player position
            gameGrid.draw()

            # draw all active sprites
            active_sprites.draw(screen)

            # Flip screen
            pygame.display.flip()

        elif not playerPlaced:
            # Clear screen
            screen.fill(BACKGROUND)

            # Draws current game grid to screen, necessary to keep it displayed to propagate updates to player position
            gameGrid.draw()
            drawInfo("Please place your robot!", (90, gameGrid.pixelHeight))
            pygame.display.update()

            if event.type == MOUSEBUTTONDOWN:
                
                pos = (event.pos[0], event.pos[1])
        
                # Loops through grid squares, checking if click occurred in squares's area
                for y in xrange(gameGrid.Height):
                    row = gameGrid.gridObjects[y]
                    for x in xrange(gameGrid.Width):
                        if row[x].collidepoint(pos) and not gameGrid.isWall(y, x):
                            # Set to true so that regular game functions are now reachable
                            playerPlaced = True
                            # creates new instance of the class player.
                            thePlayer = player.Player(y, x, gameGrid)
                            # allows the player to be drawn to he GUI
                            active_sprites.add(thePlayer)
                            # set frames to 0 so that the timer will be reset if the user plays another game
                            frames = 0


    if(playerPlaced):
        currentTime = totalTime - (frames//60)
        stringTime = str(currentTime)               
        drawInfo(stringTime, (90, gameGrid.pixelHeight))
        pygame.display.update()
        frames += 1

    if(currentTime <= 0 and playerPlaced):
        active_sprites.remove(thePlayer)
        playerPlaced = False
        startMenu.active = True
    # Pause
    clock.tick(60)

pygame.quit()
