import pygame

# GLOBAL VARIABLES
COLOR = (255, 100, 98)
SURFACE_COLOR = (167, 255, 100)
WIDTH = 500
HEIGHT = 500

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(SURFACE_COLOR)
        self.image.set_colorkey(COLOR)

        pygame.draw.rect(self.image,
        color,
        pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()

import pygame
import random

pygame.init()

SPRITE_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOUR_CHANGE_EVENT = pygame.USEREVENT + 2

BLUE = pygame.Colour('blue')
LIGHTBLUE = pygame.Colour('lightblue')
DARKBLUE = pygame.Colour('darkblue')

YELLOW = pygame.Colour('yellow')
MAGENTA = pygame.Colour('magenta')
ORANGE = pygame.Colour('orange')

class Sprite(pygame.sprite.Sprite):

    def __init__(self,colour,height,width):
        super().__init__()

        self.image = pygame.Surface([width,height])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1,1]), random.choice([-1,1])]
    def update(self):
        self.rect.move_ip(self.velocity)
        boundary_hit = True
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocityt[1] = self.velocity[1]
            boundary_hit = True
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOUR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOUR_CHANGE_EVENT))
    def change_colour(self):
        self.image.fill(random.choice([YELLOW ,MAGENTA , ORANGE ]))

    def change_backgorund_colour():
        global bg_colour
        bg_colour = random.choice([BLUE, LIGHTBLUE , DARKBLUE])

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(ORANGE,20,30)
sp1.rect.x = random.randint(0,480)
sp1.rect.y = random.randint(0,370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Boundary Sprite")
bg_color = BLUE
screen.fill(bg_color)

exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOUR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOUR_CHANGE_EVENT:
            change_background_coluor()