import pygame                               # Handles user input and game output
from random import randint                  # Used to spread obstacles and stars evenly across the game grid

# Generates the game grid and handles interactions with it
class Matrix:
    obstacleDensity     = 0.3                                           # Amount of obstacle blocks to place in the grid to 1 d.p. 1 = All obstacles, 0 = No obstacles
    starDensity         = 0.2                                           # Amount of stars to place in the grid to 1 d.p. 1 = All stars, 0 = No stars

    # Holds spatial data of each game grid square
    class gridSquare:
        squareRect  = pygame.Rect       # Holds square's coordinates
    
    # Generates game grid on matrix initialisation
    def __init__(self, mWidth, mHeight, gameSurface):
        self.gridObjects    = []                                            # Physical implementation of grid. Used to render self.grid
        self.goalLocation   = []                                            # Location of player goal, where the player must go having collected all the stars
        self.pixelMargin    = 1                                             # The number of pixels to separate grid squares vertically and horizontally
        self.gridSquareSize = 32                                            # Height and width, in pixels, of each game grid square
        self.Width          = mWidth
        self.Height         = mHeight
        self.pixelWidth     = (mWidth * ( self.gridSquareSize + 1 )) + 1    # Calculates total width of grid in pixels
        self.pixelHeight    = (mHeight * ( self.gridSquareSize + 1 )) + 1   # Calculates total height of grid in pixels
        self.gameSurface    = gameSurface                                   # Instance of game's Pygame surface, for drawing the grid on
        maxObstacles        = mWidth * mHeight * self.obstacleDensity       # Maximum number of obstacle blocks allowed on the grid
        maxStars            = mWidth * mHeight * self.starDensity           # Maximum number of stars allowed on the grid
        
        self.obstacleCount  = 0                                             # Number of obstacle blocks placed in the grid so far
        self.starCount      = 0                                             # Number of stars placed in the grid so far
        obstacleThreshold   = self.obstacleDensity * 10                     # Modifies density for use by the random obstacle placer
        starThreshold       = self.starDensity * 10                         # Modifies density for use by the random star placer
        self.grid           = []                                            # Reset grid

        
        for y in range(0, mHeight):
            row = []
            for x in range(0, mWidth):
                if self.obstacleCount < maxObstacles and randint(1, 11) < obstacleThreshold:
                    row.append(1)
                    self.obstacleCount += 1
                elif self.starCount < maxStars and randint(1, 11) < starThreshold:
                    row.append(2)
                    self.starCount += 1
                else:
                    row.append(0)

            self.grid.append(row)

        # Adds the goal, the square the player must travel to on level completion
        self.addGoal(mWidth, mHeight)
    
    # Returns if a wall exists at the given position
    def isWall(self,xPos, yPos):
        if self.grid[yPos][xPos] == 1:
            return True
        else:
            return False

    # Returns if a star exists at the given position
    def isStar(self, xPos, yPos):
        if self.grid[yPos][xPos] == 2:
            return True
        else:
            return False

    # Returns if a goal is at the given position
    def isGoal(self, xPos, yPos):
        if self.grid[yPos][xPos] == 3:
            return True
        else:
            return False

    #Checks if the space it is attempting to occupy is a blank spot
    #if it isn't then it recursively calls itself till it finds a empty spot
    def addGoal(self, mWidth, mHeight):
        print mWidth, " ", mHeight
        x = mWidth - 1
        y = mHeight - 1
        x = randint(0, x)
        y = randint(0, y)
        check_row = self.grid[y]
        if check_row[x] == 0:
            check_row[x] = 3
            self.grid[y] = check_row
            self.goalLocation = [x, y]
        else:
            self.addGoal(mWidth, mHeight)

    # Renders game grid to display
    def draw(self):
        # Creates surface to render game grid to
        gridSurface = pygame.Surface((self.pixelWidth, self.pixelHeight))
        
        # Sets vertical starting point (in pixels)
        vStart = self.pixelMargin
        
        # Renders all rows of game grid
        for y in xrange(self.Height):
            # Initialises row output
            gridRow = []
            
            # Sets horizontal starting point (in pixels)
            hStart = self.pixelMargin
            
            # Renders each grid square of a single row
            for x in xrange(self.Width):
                gridRow.append(pygame.Rect( vStart, hStart, self.gridSquareSize, self.gridSquareSize ))
                
                # Fetches whatever is at current position in grid
                gridSquare = self.grid[x][y]
                
                # If grid square is the goal, colour green
                if gridSquare == 3:
                    squareColour = (0, 76, 16)
                # If grid square is a star, colour yellow
                elif gridSquare == 2:
                    squareColour = (246, 225, 81)
                # If grid square if a wall, colour grey
                elif gridSquare == 1:
                    squareColour = (225, 225, 225)
                else:
                    squareColour = (142, 142, 142)
                
                
                pygame.draw.rect(self.gameSurface, squareColour, gridRow[x])
                
                hStart += self.gridSquareSize + 1
            
            self.gridObjects.append(gridRow)
            
            # Increases vertical starting point
            vStart += self.gridSquareSize + 1
