import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Color Change with Custom Event")

# Define custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # trigger every 2 seconds

# Sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((80, 80))
        self.color = self.random_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def random_color(self):
        return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    def change_color(self):
        self.color = self.random_color()
        self.image.fill(self.color)

# Create sprites
sprite1 = MySprite(100, 150)
sprite2 = MySprite(300, 150)

# Sprite group
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Custom event triggers color change
        if event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

        # Optional: press SPACE to manually trigger event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.event.post(pygame.event.Event(CHANGE_COLOR_EVENT))

    # Draw
    screen.fill((30, 30, 30))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()