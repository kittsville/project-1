import pygame

# Handles player position etc.
class Player(pygame.sprite.Sprite):
    gridSquareSizePlusBorder = 33  # Height and width, in pixels, of each game grid square plus the one pixel border

    # Construct player robot at given location
    def __init__(self, gridX, gridY, matrix):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image and set width, height
        self.image = pygame.image.load("assets/robot.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Make our top-left corner the passed-in location
        self.rect.x = gridX*33
        self.rect.y = gridY*33

        # Set movement vector
        self.changeX = 0
        self.changeY = 0

        # get matrix and set current location
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

    # Update the location of the player if new location is in matrix
    def update(self):
        # temporary location to check if there is a wall before updating real location
        location = self.currentLocation

        if self.changeX != 0 or self.changeY != 0:
            location[0] += self.changeX
            location[1] += self.changeY

            # check if location is inside the game grid
            if (0 <= location[0] < self.gameGrid.Width) and (0 <= location[0] < self.gameGrid.Width):
                # check if place it would move to is a wall
                if not self.gameGrid.isWall(location[0], location[1]):
                    print("no wall at {}".format(location))
                    self.currentLocation = location
                    self.rect.x += self.changeX*Player.gridSquareSizePlusBorder
                    self.rect.y += self.changeY*Player.gridSquareSizePlusBorder
                else:
                    print("wall at {}".format(self.currentLocation)) # for debugging purposes
                    self.currentLocation[0] -= self.changeX
                    self.currentLocation[1] -= self.changeY

        # Reset movement
        self.changeX = 0
        self.changeY = 0
