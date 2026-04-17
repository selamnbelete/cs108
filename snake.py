import pygame
import random
import sys

# ----------------------------
# Settings
# ----------------------------
CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20

WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT

FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (220, 0, 0)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)


def random_food(snake):
    """Return a random position not occupied by the snake."""
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake:
            return pos


def draw_cell(screen, color, position):
    x, y = position
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, BLACK, rect, 1)


def draw_grid(screen):
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))


def show_text(screen, text, size, color, center):
    font = pygame.font.SysFont("arial", size, bold=True)
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=center)
    screen.blit(surface, rect)


def reset_game():
    snake = [(10, 10), (9, 10), (8, 10)]
    direction = (1, 0)  # moving right
    food = random_food(snake)
    score = 0
    game_over = False
    return snake, direction, food, score, game_over


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()

    snake, direction, food, score, game_over = reset_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if not game_over:
                    if event.key == pygame.K_UP and direction != (0, 1):
                        direction = (0, -1)
                    elif event.key == pygame.K_DOWN and direction != (0, -1):
                        direction = (0, 1)
                    elif event.key == pygame.K_LEFT and direction != (1, 0):
                        direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                        direction = (1, 0)
                else:
                    if event.key == pygame.K_r:
                        snake, direction, food, score, game_over = reset_game()

        if not game_over:
            head_x, head_y = snake[0]
            dx, dy = direction
            new_head = (head_x + dx, head_y + dy)

            # Wall collision
            if (
                new_head[0] < 0
                or new_head[0] >= GRID_WIDTH
                or new_head[1] < 0
                or new_head[1] >= GRID_HEIGHT
            ):
                game_over = True

            # Self collision
            elif new_head in snake:
                game_over = True

            else:
                snake.insert(0, new_head)

                if new_head == food:
                    score += 1
                    food = random_food(snake)
                else:
                    snake.pop()

        # Draw
        screen.fill(BLACK)
        draw_grid(screen)

        # Draw snake
        for i, segment in enumerate(snake):
            if i == 0:
                draw_cell(screen, DARK_GREEN, segment)  # head
            else:
                draw_cell(screen, GREEN, segment)

        # Draw food
        draw_cell(screen, RED, food)

        # Score
        show_text(screen, f"Score: {score}", 24, WHITE, (80, 20))

        if game_over:
            show_text(screen, "GAME OVER", 40, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30))
            show_text(screen, "Press R to Restart", 28, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 15))
            show_text(screen, "Close the window to Quit", 24, WHITE, (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    