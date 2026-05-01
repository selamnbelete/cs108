import pygame
from Plant_system import Plant, SEED, GROWING, FULLY_GROWN

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Garden Simulation")

# Create a plant instance
my_plant = Plant()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Example action: water plant (make this grow)
                my_plant.grow()
            elif event.key == pygame.K_s:  # Example action: give sunlight
                print("Provided sunlight to the plant.")

    dt = clock.tick(60) / 1000  # Get time since last frame

    # Update plant growth and aging
    #
    # my_plant.grow()
    #my_plant.age()

    # Clear screen with white
    screen.fill((255, 255, 255))

    # Draw the plant
    if my_plant.stage == SEED:
        pygame.draw.circle(screen, (0, 128, 0), (400, 300), 5)  # Seed stage
    elif my_plant.stage == GROWING:
        pygame.draw.rect(screen, (0, 255, 0), (400 - my_plant.size, 300, my_plant.size * 2, 10))  # Growing stage
    elif my_plant.stage == FULLY_GROWN:
        pygame.draw.rect(screen, (0, 180, 0), (395, 250, 10, 60))     # Stem
        pygame.draw.circle(screen, (255, 100, 150), (400, 240), 20)   # Flower

    pygame.display.flip()

pygame.quit()
