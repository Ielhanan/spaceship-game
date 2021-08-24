import pygame
import os
##variables##
WHITE = (255,255,255)
BLACK = (0, 0, 0)
HIGHT, WIDTH = 500, 900
WIN = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Elhanan's game")
MAX_BULLETS=3
FPS = 60
SPACESHIP_WIDTH =SPACESHIP_HIGHT = 50
VEL=2
BORDER=pygame.Rect((WIDTH/2)-5,0,10,HIGHT)
yellowBullets=[]
redBullets=[]

###image define###
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP,90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP,270)


def draw_window(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x, red.y))

    pygame.display.update()



def move(key_preesed,red,yellow):

    if key_preesed[pygame.K_a] and  yellow.x- VEL > 0:  # LEFT
        yellow.x -= VEL
    if key_preesed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if key_preesed[pygame.K_s] and yellow.y+VEL+yellow.height < HIGHT:  # DOWN
        yellow.y += VEL
    if key_preesed[pygame.K_d] and yellow.x+VEL+yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if key_preesed[pygame.K_LEFT] and red.x - VEL-10 > BORDER.x:  # LEFT
        red.x -= VEL
    if key_preesed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if key_preesed[pygame.K_DOWN] and red.y+VEL+red.height < HIGHT:  # DOWN
        red.y += VEL
    if key_preesed[pygame.K_RIGHT] and red.x+VEL+red.width < WIDTH:  # RIGHT
        red.x += VEL


def main():
    red=pygame.Rect(700, 300, SPACESHIP_HIGHT, SPACESHIP_WIDTH)
    yellow=pygame.Rect(100, 300, SPACESHIP_HIGHT, SPACESHIP_WIDTH)


    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run =False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellowBullets)<MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x +yellow.width,yellow.y+yellow.height/2-2,10,5)
                    yellowBullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(redBullets)<MAX_BULLETS:
                    bullet = pygame.Rect(red.x ,  red.y + red.height / 2 - 2, 10, 5)
                    redBullets.append(bullet)


        key_preesed= pygame.key.get_pressed()
        move(key_preesed,red,yellow)
        draw_window(red,yellow)


    pygame.quit()




if __name__=="__main__":
    main()