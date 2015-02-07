import pygame

# Handles player position etc.
class Player(pygame.sprite.Sprite):
    # Construct player robot at given location
    def __init__(self, gridX, gridY, matrix):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image and set width, height
        self.image = pygame.image.load("assets/robot.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Make our top-left corner the passed-in location
        self.rect.x = gridX*(matrix.gridSquareSize + 1)
        self.rect.y = gridY*(matrix.gridSquareSize + 1)

        # Set movement vector
        self.changeX = 0
        self.changeY = 0

        # get matrix and set current location on the grid
        self.gameGrid = matrix
        self.currentLocation = [gridX, gridY]

    # Move the player to the grid above
    def moveUp(self):
        self.changeY = -1

    # Move the player to the grid below
    def moveDown(self):
        self.changeY = 1

    # Move the player to the grid to the left
    def moveLeft(self):
        self.changeX = -1

    # Move the player to the grid to the right
    def moveRight(self):
        self.changeX = 1

    # Returns the location of the player
    def getLocation(self):
        return self.currentLocation[0], self.currentLocation[1]

    # Update the location of the player if new location is in matrix
    def update(self):
        # temporary location to check if there is a wall before updating real location
        location = list(self.currentLocation)

        # if there is any movement
        if self.changeX != 0 or self.changeY != 0:
            # update location
            location[0] += self.changeX
            location[1] += self.changeY
            # if location is inside the game grid
            if (0 <= location[0] < self.gameGrid.Width) and (0 <= location[1] < self.gameGrid.Height):
                # if location is not a wall
                if not self.gameGrid.isWall(location[0], location[1]):
                    print("no wall at {}".format(location))  # for debugging purposes
                    # update player location
                    self.currentLocation = list(location)
                    self.rect.x += self.changeX*(self.gameGrid.gridSquareSize + 1)
                    self.rect.y += self.changeY*(self.gameGrid.gridSquareSize + 1)
                else:
                    print("wall at {}".format(location))  # for debugging purposes

        # Reset movement
        self.changeX = 0
        self.changeY = 0
