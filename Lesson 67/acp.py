import pygame
import sys
import os

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Game Window with Image")

# Correct path (ONLY filename here)
folder = os.path.dirname(__file__)
img_path = os.path.join(folder, "image.png")

print(img_path)  # debug

img = pygame.image.load(img_path)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(img, (100, 100))
    pygame.display.update()

pygame.quit()
sys.exit()