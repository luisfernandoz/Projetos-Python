import pygame
from pygame.locals import *
import math
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Move the Green, Red, Blue, and White Squares")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

square_size = 50
green_square_x = (SCREEN_WIDTH - square_size) // 2
green_square_y = (SCREEN_HEIGHT - square_size) // 2

red_square_x = SCREEN_WIDTH - green_square_x - square_size
red_square_y = SCREEN_HEIGHT - green_square_y - square_size

blue_square_size = 30
blue_square_x = SCREEN_WIDTH // 2
blue_square_y = SCREEN_HEIGHT // 2
blue_square_penalty = 0  # Points reduction per second when blue square touches the green square

white_square_size = 20
white_square_x = random.randint(0, SCREEN_WIDTH - white_square_size)
white_square_y = random.randint(0, SCREEN_HEIGHT - white_square_size)
white_square_speed = 2

clock = pygame.time.Clock()

attraction_factor = 0.1
repulsion_factor = 0.1

score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[K_LEFT] and green_square_x > 0:
        green_square_x -= 5
    if keys[K_RIGHT] and green_square_x < SCREEN_WIDTH - square_size:
        green_square_x += 5
    if keys[K_UP] and green_square_y > 0:
        green_square_y -= 5
    if keys[K_DOWN] and green_square_y < SCREEN_HEIGHT - square_size:
        green_square_y += 5

    red_square_x = SCREEN_WIDTH - green_square_x - square_size
    red_square_y = SCREEN_HEIGHT - green_square_y - square_size

    dx_green = green_square_x - blue_square_x
    dy_green = green_square_y - blue_square_y
    distance_green = math.sqrt(dx_green**2 + dy_green**2)

    dx_red = red_square_x - white_square_x
    dy_red = red_square_y - white_square_y
    distance_red = math.sqrt(dx_red**2 + dy_red**2)

    if distance_green > 0:
        attraction_force_green = attraction_factor / distance_green
        blue_square_x += attraction_force_green * dx_green
        blue_square_y += attraction_force_green * dy_green

        # Check for collision between blue and green squares
        if (
            green_square_x < blue_square_x + blue_square_size
            and green_square_x + square_size > blue_square_x
            and green_square_y < blue_square_y + blue_square_size
            and green_square_y + square_size > blue_square_y and score > 0
        ):
            # Custom pop-up with the game score
            pop_up_font = pygame.font.Font(None, 48)
            pop_up_text = pop_up_font.render("Game Over   Your Score: " + str(score), True, WHITE)

            # Center the pop-up on the screen
            pop_up_rect = pop_up_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

            screen.blit(pop_up_text, pop_up_rect.topleft)
            pygame.display.update()

            pygame.time.delay(2000)  # Display the pop-up for 2000 milliseconds (2 seconds)

            running = False  # End the game

    if distance_red > 0:
        repulsion_force_red = repulsion_factor / distance_red
        white_square_x -= repulsion_force_red * dx_red
        white_square_y -= repulsion_force_red * dy_red

    white_square_x += random.uniform(-white_square_speed, white_square_speed)
    white_square_y += random.uniform(-white_square_speed, white_square_speed)

    # Check for collision between red and white squares
    if (
        red_square_x < white_square_x + white_square_size
        and red_square_x + square_size > white_square_x
        and red_square_y < white_square_y + white_square_size
        and red_square_y + square_size > white_square_y
    ):
        # Increment score
        score += 1
        repulsion_factor += 0.05
        attraction_factor += 0.1

        # Respawn white square in a new location
        white_square_x = random.randint(0, SCREEN_WIDTH - white_square_size)
        white_square_y = random.randint(0, SCREEN_HEIGHT - white_square_size)

    white_square_x = max(0, min(white_square_x, SCREEN_WIDTH - white_square_size))
    white_square_y = max(0, min(white_square_y, SCREEN_HEIGHT - white_square_size))

    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, (green_square_x, green_square_y, square_size, square_size))
    pygame.draw.rect(screen, RED, (red_square_x, red_square_y, square_size, square_size))
    pygame.draw.rect(screen, BLUE, (int(blue_square_x), int(blue_square_y), blue_square_size, blue_square_size))
    pygame.draw.rect(screen, WHITE, (int(white_square_x), int(white_square_y), white_square_size, white_square_size))

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
