import pygame

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption("Wumpus World Simulation")

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Clear screen
    screen.fill(WHITE)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(60)

pygame.quit()