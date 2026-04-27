import pygame
import sys

pygame.init()

x, y   = 400, 300
vx, vy = 3, 2

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CS 108 Pygame")

clock = pygame.time.Clock()
FPS   = 60

while True:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Update state
    # (nothing yet)
    keys = pygame.key.get_pressed()
    SPEED = 4

    if keys[pygame.K_LEFT]:  x -= SPEED
    if keys[pygame.K_RIGHT]: x += SPEED
    if keys[pygame.K_UP]:    y -= SPEED
    if keys[pygame.K_DOWN]:  y += SPEED

    # clamp to window
    x = max(0, min(WIDTH,  x))
    y = max(0, min(HEIGHT, y))

    mx, my = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()


    # inside the loop, in Update state:
    x += vx
    y += vy

    # bounce off walls
    if x <= 0 or x >= WIDTH:
        vx = -vx
    if y <= 0 or y >= HEIGHT:
        vy = -vy

    # in Draw:
    screen.fill((30, 30, 46))
    pygame.draw.circle(screen, (137, 180, 250), (int(x), int(y)), 30)

    # 3. Draw
    screen.fill((30, 30, 46))
    pygame.draw.circle(screen, (137, 180, 250), (int(x), int(y)), 30)
    pygame.draw.circle(screen, (166, 227, 161), (mx, my), 15)

    pygame.display.flip()           # push frame to screen
    clock.tick(FPS)                 # cap at 60 FPS

    if pressed[0]:
        print(f"clicking at {mx}, {my}")
        