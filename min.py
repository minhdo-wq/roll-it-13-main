import pygame
import random

# init
pygame.init()

# window
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner Game")

# colors     
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)

# player
player = pygame.Rect(100,300,40,40)
velocity = 0
gravity = 1
jump_power = -15
slow_power = 10000000000

# obstacle
obstacle = pygame.Rect(800,300,30,40)
speed = 6

clock = pygame.time.Clock()
running = True

while running:

    clock.tick(60)
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
             

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.y == 300:
                velocity = jump_power

    # gravity
    velocity += gravity
    player.y += velocity

    if player.y > 300:     
        player.y = 300

    # obstacle movement
    obstacle.x -= speed
    if obstacle.x < -50:
        obstacle.x = 8000
        speed += 30

    # collision
    if player.colliderect(obstacle):
        print("Game Over")
        running = False

    pygame.draw.rect(screen, green, player)
    pygame.draw.rect(screen, red, obstacle)

    pygame.display.update()

pygame.quit()