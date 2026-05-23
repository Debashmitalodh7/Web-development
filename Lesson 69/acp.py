# Simple Pygame Program
# Creates a game window with a rectangle and text

import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font setup
font = pygame.font.SysFont("Arial", 40)

# Create text
text = font.render("Welcome to Pygame!", True, BLACK)

# Game loop
running = True
while running:

    # Fill background color
    screen.fill(WHITE)

    # Draw a rectangle
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))

    # Draw another rectangle
    pygame.draw.rect(screen, RED, (100, 400, 150, 80))

    # Display text
    screen.blit(text, (220, 100))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()