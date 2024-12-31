import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pinball Game")

# Sliders properties
slider_width, slider_height = 10, 100
slider_speed = 10

# Create left and right sliders
left_slider = pygame.Rect(30, (HEIGHT - slider_height) // 2, slider_width, slider_height)
right_slider = pygame.Rect(WIDTH - 30 - slider_width, (HEIGHT - slider_height) // 2, slider_width, slider_height)

# Ball properties
ball_radius = 10
ball_speed = [random.choice([-5, 5]), random.choice([-5, 5])]  # Random initial speed in x and y directions
ball = pygame.Rect((WIDTH - ball_radius) // 2, (HEIGHT - ball_radius) // 2, ball_radius, ball_radius)

# Additional variables for speed increase
speed_increase_percentage = 2
collisions = 0

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the sliders
    if ball_speed[0] > 0:
        if ball.centery < right_slider.centery and right_slider.top > 0:
            right_slider.y -= slider_speed
        elif ball.centery > right_slider.centery and right_slider.bottom < HEIGHT:
            right_slider.y += slider_speed
    else:
        if ball.centery < left_slider.centery and left_slider.top > 0:
            left_slider.y -= slider_speed
        elif ball.centery > left_slider.centery and left_slider.bottom < HEIGHT:
            left_slider.y += slider_speed

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with sliders
    if ball.colliderect(left_slider) or ball.colliderect(right_slider):
        ball_speed[0] = -ball_speed[0]
        ball_speed[0] += ball_speed[0] * (speed_increase_percentage / 100)
        collisions += 1

    # Ball collision with top and bottom boundaries
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball out of bounds
    if ball.left < 0 or ball.right > WIDTH:
        # Reset the ball
        ball = pygame.Rect((WIDTH - ball_radius) // 2, (HEIGHT - ball_radius) // 2, ball_radius, ball_radius)
        ball_speed = [random.choice([-5, 5]), random.choice([-5, 5])]  # Random initial speed

    # Clear the screen
    screen.fill(BLACK)

    # Draw the sliders
    pygame.draw.rect(screen, WHITE, left_slider)
    pygame.draw.rect(screen, WHITE, right_slider)

    # Draw the ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
