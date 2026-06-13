import pygame
import random
import string

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Password Generator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (173, 216, 230)

# Font
font = pygame.font.Font(None, 36)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

password = "Click SPACE to Generate"

running = True
while running:
    screen.fill(LIGHT_BLUE)

    title = font.render("Random Password Generator", True, BLACK)
    screen.blit(title, (140, 50))

    text = font.render(password, True, BLACK)
    screen.blit(text, (50, 150))

    instruction = font.render("Press SPACE", True, BLACK)
    screen.blit(instruction, (220, 230))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                password = generate_password(12)

pygame.quit()