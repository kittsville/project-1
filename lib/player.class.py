import pygame

# Handles player position etc.
class Player:
    # Set movement vector
    change_x = 0
    change_y = 0

    # Construct player robot at given location
    def __init__(self, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)

        # Load image and set width, height
        self.image, self.rect = pygame.image.load("assests/robot.png").convert_alpha()

        # Make our top-left corner the passed-in location
        self.rect.x = xPos
        self.rect.y = yPos

    # Change the location of the player. Assumed that xPos and yPos are postions in the 
    # matrix
    def move_bot(self, xPos, yPos):
        self.change_x = (xPos - self.rect.x)
        self.change_y = (yPos - self.rect.y)

    # Update the location of the player
    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
