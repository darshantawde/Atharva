import math
import random

import pygame

# Run in Python 3.7.0 on PyCharm!
# Initialize PyGame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((626, 327))

# Background
bg = pygame.image.load('bg.jpg')

# Title and Icon
pygame.display.set_caption("Joe and the Strange Case of the Flying Rabbits")
icon = pygame.image.load('man.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('hunter.png')
playerX = 313
playerY = 263
playerX_change = 0

# Enemy
rabbitImg = pygame.image.load('bunny.png')
rabbitX = random.randint(0, 562)
rabbitY = random.randint(15, 50)
rabbitX_change = 0.5
rabbitY_change = 0.5

# Bullet
# Ready (Bullet == Invisible), Fire (Bullet == Moving)
bulletImg = pygame.image.load('bullet.png')
bulletX = 313
bulletY = 263
bulletX_change = 0
bulletY_change = 3.5
bullet_state = 'ready'

score = 0


# Draw Player
def player(x, y):
    screen.blit(playerImg, (x, y))


# Draw Rabbit
def rabbit(x, y):
    screen.blit(rabbitImg, (x, y))


# Fire Bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


# Collision Checker (<27 PX between Rabbit and Bullet)
def is_collision(rx, ry, bx, by):
    distance = math.sqrt((math.pow(rx - bx, 2)) + (math.pow(ry - by, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop Setup
running = True
while running:

    # Set Background RGB - Red, Green, Blue
    screen.fill((0, 191, 255))

    # Set Background
    screen.blit(bg, (0, 0))

    # Stop Running When X Button is Pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    # Get Current X Coord of Spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    # Setting Up Boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 562:
        playerX = 562

    rabbitX += rabbitX_change

    if rabbitX <= 0:
        rabbitX_change = 0.9
        rabbitY += rabbitY_change
    elif rabbitX >= 562:
        rabbitX_change = -0.9
        rabbitY += rabbitY_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 263
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = is_collision(rabbitX, rabbitY, bulletX, bulletY)
    if collision:
        bulletY = 263
        bullet_state = 'ready'
        score += 1
        rabbitX = random.randint(0, 562)
        rabbitY = random.randint(15, 50)

    player(playerX, playerY)
    rabbit(rabbitX, rabbitY)

    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score: ' + str(score), True, (0, 255, 0), (0, 0, 128))
    textRect = text.get_rect()
    textRect.center = (560, 10)
    screen.blit(text, textRect)

    pygame.display.update()
