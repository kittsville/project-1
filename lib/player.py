import pygame

# Handles player position etc.
class Player(pygame.sprite.Sprite):
    # Set movement vector
    changeX = 0
    changeY = 0

    # Construct player robot at given location
    def __init__(self, xPos, yPos):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Load image and set width, height
        self.image = pygame.image.load("assets/robot.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Make our top-left corner the passed-in location
        self.rect.x = xPos
        self.rect.y = yPos

    # Change the location of the player. Assumed that xPos and yPos are postions in the 
    # matrix
    def moveBot(self, xPos, yPos):
        self.changeX = (xPos - self.rect.x)
        self.changeY = (yPos - self.rect.y)

    # Update the location of the player
    def update(self):
        self.rect.x += self.changeX
        self.rect.y += self.changeY
