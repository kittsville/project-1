import pygame

# Handles player position etc.
class Player:
    # Set speed vector
    change_x = 0
    change_y = 0

    # Construct player robot at given location
    def __init__(self, xPos, yPos):
        pygame.sprite.Sprite.__init__(self)

        # Set height, width
        self.image, self.rect = pygame.image.load("assests/robot.png").convert_alpha()

        # Make our top-left corner the passed-in location.
        self.rect.x = xPos
        self.rect.y = yPos

    # Change the speed of the player
    def change_speed(self, xPos, yPos):
        self.change_x += xPos
        self.change_y += yPos

    # Update the location
    def update(self):
        """ Update position of the player """
        self.rect.x += self.change_x
        self.rect.y += self.change_y
