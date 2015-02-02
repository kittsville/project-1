from random import randint

# Generates the game grid and handles interactions with it
class Matrix:
    grid            = []    # Game grid
    obstacleDensity = 0.4   # Amount of obstacle blocks to place in the grid to 1 d.p. 1 = All obstacles, 0 = No obstacles
    starDensity     = 0.2   # Amount of stars to place in the grid to 1 d.p. 1 = All stars, 0 = No stars

    # Generates game grid on matrix initialisation
    def __init__(self, mWidth, mHeight):
        maxObstacles        = mWidth * mHeight * self.obstacleDensity   # Maximum number of obstacle blocks allowed on the grid
        maxStars            = mWidth * mHeight * self.starDensity       # Maximum number of stars allowed on the grid
        
        obstacleCount       = 0                                         # Number of obstacle blocks placed in the grid so far
        starCount           = 0                                         # Number of stars placed in the grid so far
        
        obstacleThreshold   = self.obstacleDensity * 10                 # Modifies density for use by the random obstacle placer
        starThreshold       = self.starDensity * 10                     # Modifies density for use by the random star placer
        
        print 'Generating Grid' # Debugging code, leave for now
        
        for y in range(0, mHeight):
            row = []

            for x in range(0, mWidth):
                if obstacleCount < maxObstacles and randint(1, 11) < obstacleThreshold:
                    row.append(1)
                elif starCount < maxStars and randint(1, 11) < starThreshold:
                    row.append(2)
                else:
                    row.append(0)

            self.grid.append(row)
            print row # Debugging, leave for now
        

    # Returns if a wall exists at the given position
    def isWall(self,xPos, yPos):
        if self.grid[yPos][xPos] == 1:
            return True
        else:
            return False
        