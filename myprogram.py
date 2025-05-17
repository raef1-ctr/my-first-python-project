import pygame
import random

# Initialize Pygame
pygame.init()
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Paddle settings
paddle_width, paddle_height = 100, 10
paddle_x = width // 2 - paddle_width // 2
paddle_y = height - 30
paddle_speed = 7

# Ball settings
ball_radius = 10
ball_x = width // 2
ball_y = height // 2
ball_speed_x = random.choice([-4, 4])
ball_speed_y = -4

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Paddle control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < width - paddle_width:
        paddle_x += paddle_speed

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Wall collision
    if ball_x <= 0 or ball_x >= width:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # Paddle collision
    if paddle_y < ball_y + ball_radius < paddle_y + 10 and paddle_x < ball_x < paddle_x + paddle_width:
        ball_speed_y *= -1

    # Game over
    if ball_y > height:
        font = pygame.font.SysFont(None, 48)
        text = font.render("Game Over!", True, RED)
        win.blit(text, (width//2 - 100, height//2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)
        running = False

    # Draw paddle and ball
    pygame.draw.rect(win, BLUE, (paddle_x, paddle_y, paddle_width, paddle_height))
    pygame.draw.circle(win, RED, (ball_x, ball_y), ball_radius)

    pygame.display.update()

pygame.quit()
