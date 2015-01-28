import pygame

# Handles player position etc.
class Player(pygame.sprite.Sprite):
    # Set movement vector
    changeX = 0
    changeY = 0

    # Construct player robot at given location
    def __init__(self, xPos, yPos, gridSize):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image and set width, height
        self.image = pygame.image.load("assets/robot.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Make our top-left corner the passed-in location
        self.rect.x = xPos
        self.rect.y = yPos

        self.gridSize = gridSize

    # Move the player to the grid above
    def moveUp(self):
        self.changeY = -self.gridSize

    # Move the player to the grid below
    def moveDown(self):
        self.changeY = +self.gridSize

    # Move the player to the grid to the left
    def moveLeft(self):
        self.changeX = -self.gridSize

    # Move the player to the grid to the right
    def moveRight(self):
        self.changeX = +self.gridSize

    # Update the location of the player if new location is in matrix
    def update(self):
        # TODO: check if self.rect.x + changeX would be in a valid grid. Same for y also.
        self.rect.x += self.changeX
        self.rect.y += self.changeY

        # Reset movement
        self.changeY = 0
        self.changeX = 0
