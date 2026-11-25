import pygame

import random

pygame.init()

# Create the game window

screen = pygame.display.set_mode((600, 400))

pygame.display.set_caption("Colorful Bounce Game")

# Rectangle position and size

x = 200

y = 150

width = 60

height = 60

# Random movement direction

speed_x = random.choice([-5, 5])

speed_y = random.choice([-5, 5])

# Starting color

color = (255, 0, 0)

# Control the game speed

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    x += speed_x
    y += speed_y

    if x <= 0 or x + width >= 600:
        speed_x = -speed_x
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
        
    if y <= 0 or y + height >= 400:
        speed_y = -speed_y
        color = (random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, (x, y, width, height))
    pygame.display.update()
    clock.tick(60)
pygame.quit()