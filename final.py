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
Grey=(128 , 128 ,128)
Green=(0,255,0)
Black=(0,0,0)


# player
player_img = pygame.image.load('rat.png')
playerX = 300
playerY = 200
playerX_change = 0
playerY_change = 0
step=0.1


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


# game window loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check if right or left
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            playerY_change -= step

        if key[pygame.K_DOWN]:
            playerY_change += step

        if key[pygame.K_RIGHT]:
            playerX_change += step


        if key[pygame.K_LEFT]:
            playerX_change -= step

        '''if event.type == pygame.KEYDOWN:
            print("Key stroke is preesed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if event.type == pygame.K_UP:
            playerY_change = 0.3
        if event.type == pygame.K_DOWN:
            playerY_change = -0.3'''

    # Checking poundray of the space ship so it doesn't go out side of it
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerY >= 736:
        playerY = 736
    playerY += playerY_change
    #Cat Movment
    CatX += CatX_change
    CatY += CatY_change
    if CatX <= 100:
        CatX_change = 0.1
        CatY += CatY_change
    elif CatX >= 600:
        CatX_change = -0.1
        CatY += CatY_change

    if CatY <= 100:
        CatY_change = 0.1
        CatY += CatY_change
    elif CatY >= 400 :
        CatY_change = -0.1
        CatY += CatY_change


    screen.fill((0,0,255))
    pygame.draw.rect(screen,Grey,[100,100,600,400])
    pygame.draw.rect(screen, Green, [700, 250, 100, 100])
    pygame.draw.line(screen, Black, (100, 100), (700, 100), 2)
    pygame.draw.line(screen, Black, (100, 200), (700, 200), 2)
    pygame.draw.line(screen, Black, (100, 300), (700, 300), 2)
    pygame.draw.line(screen, Black, (100, 400), (700, 400), 2)
    pygame.draw.line(screen, Black, (100, 500), (700, 500), 2)
    pygame.draw.line(screen, Black, (100, 200), (700, 200), 2)
    pygame.draw.line(screen, Black, (100, 100), (100, 500), 2)
    pygame.draw.line(screen, Black, (200, 100), (200, 500), 2)
    pygame.draw.line(screen, Black, (300, 100), (300, 500), 2)
    pygame.draw.line(screen, Black, (400, 100), (400, 500), 2)
    pygame.draw.line(screen, Black, (500, 100), (500, 500), 2)
    pygame.draw.line(screen, Black, (600, 100), (600, 500), 2)
    pygame.draw.line(screen, Black, (700, 100), (700, 500), 2)
    player(playerX,playerY)
    Cat(CatX,CatY)


    pygame.display.update()

