import pygame
from Plant_system import Plant, SEED, GROWING, FULLY_GROWN, DEAD
from Button import Button

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Garden Simulation")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arialrounded", 42, bold=True)
small_font = pygame.font.SysFont("arial", 26)

plant = Plant()

# Buttons
start_button = Button(300, 350, 200, 60, "Start")
water_button = Button(50, 500, 150, 50, "Water")
sun_button = Button(230, 500, 150, 50, "Sunlight")
reset_button = Button(590, 500, 150, 50, "Reset")

game_state = "home"

# Optional sounds
# Put sound files in the same folder if you have them
water_sound = None
grow_sound = None

def draw_text(text, x, y, font_used, color=(0, 0, 0)):
    img = font_used.render(text, True, color)
    screen.blit(img, (x, y))

def draw_home_page():
    screen.fill((190, 230, 190))

    draw_text("Garden Simulation", 260, 150, font)
    draw_text("Take care of your plant by giving it water and sunlight.", 155, 220, small_font)
    draw_text("Try to grow it from a seed to a full flower.", 210, 255, small_font)

    start_button.draw(screen, font)

def draw_background():

    # sky gradient look
    screen.fill((180, 225, 250))

    # sun glow
    pygame.draw.circle(screen, (255, 230, 120), (700, 90), 55)
    pygame.draw.circle(screen, (255, 245, 180), (700, 90), 35)

    # clouds
    pygame.draw.circle(screen, (255, 255, 255), (150, 100), 30)
    pygame.draw.circle(screen, (255, 255, 255), (180, 90), 35)
    pygame.draw.circle(screen, (255, 255, 255), (210, 100), 30)

    pygame.draw.circle(screen, (255, 255, 255), (500, 130), 25)
    pygame.draw.circle(screen, (255, 255, 255), (530, 120), 30)
    pygame.draw.circle(screen, (255, 255, 255), (560, 130), 25)

    # grass
    pygame.draw.rect(screen, (100, 190, 100), (0, 420, WIDTH, 180))

    # dirt shadow
    pygame.draw.ellipse(screen, (90, 55, 30), (255, 395, 290, 90))

    # dirt top
    pygame.draw.ellipse(screen, (120, 75, 40), (270, 390, 260, 80))

def draw_plant():
    if plant.stage == SEED:
        pygame.draw.circle(screen, (80, 50, 20), (400, 395), 10)

    elif plant.stage == GROWING:
        stem_height = plant.size * 15

        # stem
        pygame.draw.rect(screen, (60, 160, 70), (395, 395 - stem_height, 10, stem_height), border_radius=5)

        # leaves
        pygame.draw.ellipse(screen, (70, 200, 90), (360, 360 - stem_height, 50, 28))
        pygame.draw.ellipse(screen, (70, 200, 90), (392, 340 - stem_height, 50, 28))

    elif plant.stage == FULLY_GROWN:
        pygame.draw.rect(screen, (60, 160, 70), (395, 250, 10, 150), border_radius=5)

        # leaves
        pygame.draw.ellipse(screen, (40, 170, 60), (350, 310, 60, 30))
        pygame.draw.ellipse(screen, (40, 170, 60), (395, 290, 60, 30))

        # flower petals
        pygame.draw.circle(screen, (255, 120, 170), (400, 230), 22)
        pygame.draw.circle(screen, (255, 120, 170), (375, 250), 22)
        pygame.draw.circle(screen, (255, 120, 170), (425, 250), 22)
        pygame.draw.circle(screen, (255, 120, 170), (390, 270), 22)
        pygame.draw.circle(screen, (255, 120, 170), (410, 270), 22)

        # flower center
        pygame.draw.circle(screen, (255, 220, 80), (400, 250), 18)

    elif plant.stage == DEAD:
        pygame.draw.rect(screen, (90, 60, 30), (395, 310, 10, 90))
        pygame.draw.line(screen, (90, 60, 30), (400, 340), (360, 310), 5)
        pygame.draw.line(screen, (90, 60, 30), (400, 350), (440, 315), 5)
        draw_text("The plant died :(", 310, 180, font, (120, 0, 0))

def draw_stats():
    draw_text(f"Health: {int(plant.health)}", 30, 30, small_font)
    draw_text(f"Water: {int(plant.water)}", 30, 60, small_font)
    draw_text(f"Sunlight: {int(plant.sunlight)}", 30, 90, small_font)

    if plant.stage == SEED:
        stage_text = "Stage: Seed"
    elif plant.stage == GROWING:
        stage_text = "Stage: Growing"
    elif plant.stage == FULLY_GROWN:
        stage_text = "Stage: Fully Grown"
    else:
        stage_text = "Stage: Dead"

    draw_text(stage_text, 30, 120, small_font)

def draw_game_page():
    draw_background()
    draw_plant()
    draw_stats()

    water_button.draw(screen, small_font)
    sun_button.draw(screen, small_font)
    reset_button.draw(screen, small_font)

def reset_game():
    global plant
    plant = Plant()

running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_state == "home":
            if start_button.is_clicked(event):
                game_state = "game"

        elif game_state == "game":
            if water_button.is_clicked(event):
                plant.water_plant()

            if sun_button.is_clicked(event):
                plant.give_sunlight()

            if reset_button.is_clicked(event):
                reset_game()

    if game_state == "home":
        draw_home_page()

    elif game_state == "game":
        plant.update()
        draw_game_page()

    pygame.display.flip()

pygame.quit()
