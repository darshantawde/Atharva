f = open('score.json', 'r')

for line in f:
    print(line)

#import os
#import random
#import pygame
#
## Class for the orange dude
#class Player(object):
#
#    def __init__(self, pos):
#        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
#
#    def move(self, dx, dy):
#
#        # Move each axis separately. Note that this checks for collisions both times.
#        if dx != 0:
#            self.move_single_axis(dx, 0)
#        if dy != 0:
#            self.move_single_axis(0, dy)
#
#    def move_single_axis(self, dx, dy):
#
#    # Move the rect
#        self.rect.x += dx
#        self.rect.y += dy
#
#    # If you collide with a wall, move out based on velocity
#        for wall in walls:
#            if self.rect.colliderect(wall.rect):
#                if dx > 0: # Moving right; Hit the left side of the wall
#                    self.rect.right = wall.rect.left
#                if dx < 0: # Moving left; Hit the right side of the wall
#                    self.rect.left = wall.rect.right
#                if dy > 0: # Moving down; Hit the top side of the wall
#                    self.rect.bottom = wall.rect.top
#                if dy < 0: # Moving up; Hit the bottom side of the wall
#                    self.rect.top = wall.rect.bottom
#
## Nice class to hold a wall rect
#class Wall(object):
#
#    def __init__(self, pos):
#        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
#
#class Finish(object):
#
#    def __init__(self, pos):
#        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
#
## Variables
#currentLevel = 0
#
## Initialise pygame
#pygame.init()
#
## Set up the display
#pygame.display.set_caption("Change level")
#screen = pygame.display.set_mode((320, 240))
#
#clock = pygame.time.Clock()
#
#levels = [[
#    "WWWWWWWWWWWWWWWWWWWW",
#    "W                  W",
#    "W  P      WWWWWW   W",
#    "W   WWWW       W   W",
#    "W   W        WWWW  W",
#    "W WWW  WWWW        W",
#    "W   W     W W      W",
#    "W   W     W   WWW WW",
#    "W   WWW WWW   W W  W",
#    "W     W   W   W W  W",
#    "WWW   W   WWWWW W  W",
#    "W W      WW        W",
#    "W W   WWWW   WWW   W",
#    "W     W   F    W   W",
#    "WWWWWWWWWWWWWWWWWWWW",
#    ],
#    [
#    "WWWWWWWWWWWWWWWWWWWW",
#    "W                  W",
#    "W                  W",
#    "W   WWWWWWWWWWWWW  W",
#    "W                  W",
#    "W         P        W",
#    "W                  W",
#    "W   WWWWWWWWWWWWW  W",
#    "W                  W",
#    "W   WWWWWWWWWWWWW  W",
#    "W                  W",
#    "W         F        W",
#    "W                  W",
#    "W                  W",
#    "WWWWWWWWWWWWWWWWWWWW",
#    ],
#    [
#    "WWWWWWWWWWWWWWWWWWWW",
#    "W        P         W",
#    "W                  W",
#    "W   WWWWWWWWWWWWW  W",
#    "W                  W",
#    "WWWWWWWWWWWWWWW    W",
#    "W                  W",
#    "W   WWWWWWWWWWWWWWWW",
#    "W                  W",
#    "WWWWWWWWWWWWWW     W",
#    "W                  W",
#    "W                  W",
#    "W        F         W",
#    "W                  W",
#    "WWWWWWWWWWWWWWWWWWWW",
#    ]]
#
#def load_level(level):
#    walls = []
#    players = []
#    finishes = []
#
#    # Parse the level string above
#    x = y = 0
#    for row in levels[level]:
#        for col in row:
#            if col == "W":
#                walls.append(Wall((x, y)))
#            if col == "P":
#                players.append(Player((x, y)))
#            if col == "F":
#                finishes.append(Finish((x, y)))
#            x += 16
#        y += 16
#        x = 0
#    return walls, players, finishes
#
#walls, players, finishes = load_level(currentLevel)
#running = True
#while running:
#
#    clock.tick(60)
#
#    for e in pygame.event.get():
#        if e.type == pygame.QUIT:
#            running = False
#        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
#            running = False
#
#    # Move the player if an arrow key is pressed
#    key = pygame.key.get_pressed()
#    if key[pygame.K_LEFT]:
#        player.move(-2, 0)
#    if key[pygame.K_RIGHT]:
#        player.move(2, 0)
#    if key[pygame.K_UP]:
#        player.move(0, -2)
#    if key[pygame.K_DOWN]:
#        player.move(0, 2)
#
#    # Just added this to make it slightly fun ;)
#    for player in players:
#        for finish in finishes:
#            if player.rect.colliderect(finish.rect): 
#                currentLevel += 1
#                walls, players, finishes = load_level(currentLevel)
#
#    # Draw the scene
#    screen.fill((0, 0, 0))
#    for wall in walls:
#        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
#    for player in players:
#        pygame.draw.rect(screen, (255, 200, 0), player.rect)
#    for finish in finishes:
#        pygame.draw.rect(screen, (0, 200, 0), finish.rect)
#    pygame.display.flip() 