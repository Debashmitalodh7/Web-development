import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)
BLACK = (0, 0, 0)

# Font
font = pygame.font.SysFont("Arial", 35)

# Clock
clock = pygame.time.Clock()

background = pygame.image.load("Lesson 71/download (1).jfif")

# Resize image to fit screen
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

player_size = 50
player_speed = 5

player = pygame.Rect(
    WIDTH // 2,
    HEIGHT // 2,
    player_size,
    player_size
)


enemy_size = 40
enemies = []

for i in range(7):

    enemy = pygame.Rect(
        random.randint(0, WIDTH - enemy_size),
        random.randint(0, HEIGHT - enemy_size),
        enemy_size,
        enemy_size
    )

    enemies.append(enemy)


score = 0
collided_enemies = []


running = True

while running:

    # Draw background image
    screen.blit(background, (0, 0))

    # Event handling
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed

    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    if keys[pygame.K_UP]:
        player.y -= player_speed

    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Keep player inside screen
    player.x = max(0, min(player.x, WIDTH - player_size))
    player.y = max(0, min(player.y, HEIGHT - player_size))

    # Draw player
    pygame.draw.rect(screen, BLUE, player)

    # Draw enemies and check collisions
    for enemy in enemies:

        pygame.draw.rect(screen, RED, enemy)

        # Collision detection
        if player.colliderect(enemy):

            if enemy not in collided_enemies:
                score += 1
                collided_enemies.append(enemy)

        else:

            if enemy in collided_enemies:
                collided_enemies.remove(enemy)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (20, 20))

    # Update screen
    pygame.display.update()

    # Frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()