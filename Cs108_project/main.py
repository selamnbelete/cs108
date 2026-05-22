import pygame
import math
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
    pygame.draw.circle(screen, (245, 245, 245), (150, 100), 30)
    pygame.draw.circle(screen, (245, 245, 245), (180, 90), 35)
    pygame.draw.circle(screen, (245, 245, 245), (210, 100), 30)
    pygame.draw.circle(screen, (245, 245, 245), (500, 130), 25)
    pygame.draw.circle(screen, (245, 245, 245), (530, 120), 30)
    pygame.draw.circle(screen, (245, 245, 245), (560, 130), 25)

    # grass
    pygame.draw.rect(screen, (100, 190, 100), (0, 420, WIDTH, 180))

    # dirt shadow
    pygame.draw.ellipse(screen, (100, 60, 35), (255, 395, 290, 90))

    # dirt top
    pygame.draw.ellipse(screen, (135, 85, 45), (270, 390, 260, 80))

    # grass blades
    for x in range(0, WIDTH, 20):
        pygame.draw.line(screen, (90, 170, 90), (x, 420), (x + 5, 405), 2)
    
    # tiny flowers
    pygame.draw.circle(screen, (255, 255, 255), (120, 470), 5)
    pygame.draw.circle(screen, (255, 255, 255), (680, 520), 5)
    pygame.draw.circle(screen, (255, 255, 255), (740, 460), 5)

    pygame.draw.circle(screen, (255, 210, 80), (120, 470), 2)
    pygame.draw.circle(screen, (255, 210, 80), (680, 520), 2)
    pygame.draw.circle(screen, (255, 210, 80), (740, 460), 2)

def draw_plant(wave_offset, bounce_offset):
    # SEED
    if plant.stage == SEED:
        pygame.draw.circle(screen, (80, 50, 20), (400, 395), 10)

    # GROWING
    elif plant.stage == GROWING:

        stem_height = plant.size * 15

        # moving stem
        stem_x = 395 + wave_offset * 0.2

        pygame.draw.rect(
            screen,
            (60, 160, 70),
            (stem_x, 395 - stem_height, 10, stem_height),
            border_radius=5
        )

        # leaves
        pygame.draw.ellipse(
            screen,
            (70, 200, 90),
            (360 + wave_offset * 0.3, 360 - stem_height, 50, 28)
        )

        pygame.draw.ellipse(
            screen,
            (70, 200, 90),
            (392 + wave_offset * 0.3, 340 - stem_height, 50, 28)
        )

    # FULLY GROWN
    elif plant.stage == FULLY_GROWN:

        # moving stem
        stem_x = 395 + wave_offset * 0.2

        pygame.draw.rect(
            screen,
            (60, 160, 70),
            (stem_x, 250, 10, 150),
            border_radius=5
        )

        # leaves
        pygame.draw.ellipse(
            screen,
            (40, 170, 60),
            (350 + wave_offset * 0.2, 310, 60, 30)
        )

        pygame.draw.ellipse(
            screen,
            (40, 170, 60),
            (395 + wave_offset * 0.2, 290, 60, 30)
        )

        # animated flower position
        flower_x = 400 + wave_offset
        flower_y = 250 + bounce_offset

        # petals with outline
        pygame.draw.circle(screen, (220, 90, 140), (flower_x, flower_y - 20), 24)
        pygame.draw.circle(screen, (255, 120, 170), (flower_x, flower_y - 20), 20)

        pygame.draw.circle(screen, (220, 90, 140), (flower_x - 25, flower_y), 24)
        pygame.draw.circle(screen, (255, 120, 170), (flower_x - 25, flower_y), 20)

        pygame.draw.circle(screen, (220, 90, 140), (flower_x + 25, flower_y), 24)
        pygame.draw.circle(screen, (255, 120, 170), (flower_x + 25, flower_y), 20)

        pygame.draw.circle(screen, (220, 90, 140), (flower_x - 10, flower_y + 20), 24)
        pygame.draw.circle(screen, (255, 120, 170), (flower_x - 10, flower_y + 20), 20)

        pygame.draw.circle(screen, (220, 90, 140), (flower_x + 10, flower_y + 20), 24)
        pygame.draw.circle(screen, (255, 120, 170), (flower_x + 10, flower_y + 20), 20)

        # flower center
        pygame.draw.circle(screen, (240, 190, 50), (flower_x, flower_y), 20)
        pygame.draw.circle(screen, (255, 220, 100), (flower_x, flower_y), 15)

    # DEAD
    elif plant.stage == DEAD:

        pygame.draw.rect(screen, (90, 60, 30), (395, 310, 10, 90))

        pygame.draw.line(screen, (90, 60, 30), (400, 340), (360, 310), 5)
        pygame.draw.line(screen, (90, 60, 30), (400, 350), (440, 315), 5)

        draw_text("The plant died :(", 310, 180, font, (120, 0, 0))

def draw_bar(label, value, x, y, color):
    # label
    draw_text(label, x, y, small_font, (40, 40, 40))

    # bar background
    pygame.draw.rect(screen, (230, 230, 230), (x, y + 28, 160, 18), border_radius=8)

    # bar fill
    fill_width = int((value / 100) * 160)
    pygame.draw.rect(screen, color, (x, y + 28, fill_width, 18), border_radius=8)

    # outline
    pygame.draw.rect(screen, (80, 80, 80), (x, y + 28, 160, 18), 2, border_radius=8)

def draw_stats():
    draw_bar("Health", plant.health, 30, 30, (90, 200, 120))
    draw_bar("Water", plant.water, 30, 90, (80, 170, 240))
    draw_bar("Sunlight", plant.sunlight, 30, 150, (255, 210, 80))
    
    if plant.stage == SEED:
        stage_text = "Stage: Seed"
    elif plant.stage == GROWING:
        stage_text = "Stage: Growing"
    elif plant.stage == FULLY_GROWN:
        stage_text = "Stage: Fully Grown"
    else:
        stage_text = "Stage: Dead"

    draw_text(stage_text, 30, 215, small_font, (40, 40, 40))

def draw_game_page(wave_offset, bounce_offset):
    draw_background()
    draw_plant(wave_offset, bounce_offset)
    draw_stats()

    draw_text("Take care of your plant", 300, 20, small_font, (50, 80, 50))

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

        time = pygame.time.get_ticks()
        wave_offset = math.sin(time * 0.003) * 4
        bounce_offset = math.sin(time * 0.006) * 3

        draw_game_page(wave_offset, bounce_offset)

    pygame.display.flip()

pygame.quit()
