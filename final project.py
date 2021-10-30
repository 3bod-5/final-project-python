import pygame
import random

# intialzing
pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))
# game icon
pygame.display.set_caption("Island escape")
icon = pygame.image.load('island.png')
pygame.display.set_icon(icon)
#arena
Blue=(0 , 0 ,255)
Green=(0,255,0)


# player
player_img = pygame.image.load('rat.png')
playerX = 370
playerY = 440
playerX_change = 0

# Cat
Cat_img = pygame.image.load('black-cat.png')
CatX = random.randint(150 , 600)
CatY = random.randint(150 , 450)
CatX_change = 0.3
CatY_change = 40


def player(x,y):
    screen.blit(player_img, (x, y))


def Cat(x,y):
    screen.blit(Cat_img, (x, y))


# game windowe loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed chcek if right or left
        if event.type == pygame.KEYDOWN:
            print("Key stroke is preesed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking poundray of the space ship so it doesn't go out side of it
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    #Cat Movment
    CatX += CatX_change
    if CatX <= 100:
        CatX_change = 0.1
        CatY += CatY_change
    elif CatX >= 600:
        CatX_change = -0.1
        CatY += CatY_change


    screen.fill((128,128,128))
    player(playerX,playerY)
    Cat(CatX,CatY)
    pygame.draw.rect(screen, Blue, [0, 0, 100, 600])
    pygame.draw.rect(screen, Blue, [100, 0, 800, 100])
    '''"pygame.draw.rect(screen, Blue, [0,0, 100, 100])
    pygame.draw.rect(screen, Blue, [0, 100, 100, 100])
    pygame.draw.rect(screen, Blue, [0, 200, 100, 100])
    pygame.draw.rect(screen, Blue, [0, 300, 100, 100])
    pygame.draw.rect(screen, Blue, [0, 400, 100, 100])
    pygame.draw.rect(screen, Blue, [0, 500, 100, 100])
    pygame.draw.rect(screen, Blue, [0, 600, 100, 100])
    pygame.draw.rect(screen, Blue, [100, 0, 100, 100])
    pygame.draw.rect(screen, Blue, [200, 0, 100, 100])
    pygame.draw.rect(screen, Blue, [300, 0, 100, 100])
    pygame.draw.rect(screen, Blue, [400, 0, 100, 100])
    pygame.draw.rect(screen, Blue, [500, 0, 100, 100])
    pygame.draw.rect(screen, Blue, [600, 0, 100, 100])
    pygame.draw.rect(screen, Blue, [700, 0, 100, 100])
    pygame.draw.rect(screen, Blue, [800, 0, 100, 100])
    pygame.draw.rect(screen, Blue, [700, 100, 100, 100])
    pygame.draw.rect(screen, Green, [700, 200, 100, 100])
    pygame.draw.rect(screen, Blue, [700, 300, 100, 100])
    pygame.draw.rect(screen, Blue, [700, 400, 100, 100])
    pygame.draw.rect(screen, Blue, [700, 500, 100, 100])
    pygame.draw.rect(screen, Blue, [700, 600, 100, 100])
    pygame.draw.rect(screen, Blue, [100, 500, 100, 100])
    pygame.draw.rect(screen, Blue, [200, 500, 100, 100])
    pygame.draw.rect(screen, Blue, [300, 500, 100, 100])
    pygame.draw.rect(screen, Blue, [400, 500, 100, 100])
    pygame.draw.rect(screen, Blue, [500, 500, 100, 100])
    pygame.draw.rect(screen, Blue, [600, 500, 100, 100])'''''



    pygame.display.update()

