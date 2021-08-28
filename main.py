import pygame
import os
pygame.font.init()
##variables##
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WINNER_FONT = pygame.font.SysFont("ariel", 100)
HELTH_FONT = pygame.font.SysFont("ariel", 40)
HIGHT, WIDTH = 500, 900
WIN = pygame.display.set_mode((WIDTH,HIGHT))
pygame.display.set_caption("Elhanan's game")
MAX_BULLETS = 3
FPS = 60
SPACESHIP_WIDTH = SPACESHIP_HIGHT = 50
VEL = 2
BORDER = pygame.Rect((WIDTH/2)-5, 0, 10, HIGHT)
yellowBullets = []
redBullets = []
BULLET_VEL = 7


#events
YELLOW_HIT=pygame.USEREVENT+1
RED_HIT=pygame.USEREVENT+2



###image define###
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HIGHT))
YELLOW_SPACESHIP = pygame.transform.rotate(YELLOW_SPACESHIP,90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HIGHT))
RED_SPACESHIP = pygame.transform.rotate(RED_SPACESHIP, 270)
BACKROUND = pygame.image.load(os.path.join('Assets', 'space.png'))
BACKROUND = pygame.transform.scale(BACKROUND,(WIDTH, HIGHT))

def draw_window(red,yellow,red_bullets,yellow_bullets,yellow_hp,red_hp):

    WIN.blit(BACKROUND, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    red_hp_text=HELTH_FONT.render("Health:"+str(red_hp), 1 , WHITE)
    yellow_hp_text=HELTH_FONT.render("Health:"+str(yellow_hp), 1, WHITE)
    WIN.blit(red_hp_text ,(WIDTH-red_hp_text.get_width()-10,red_hp_text.get_height()-10))
    WIN.blit(yellow_hp_text,(10, 10))
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x, red.y))

    for bulltes in red_bullets:
        pygame.draw.rect(WIN, RED, bulltes)
    for bulltes in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bulltes)
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


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellowBullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellowBullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            redBullets.remove(bullet)
        elif bullet.x < 0:
            redBullets.remove(bullet)
def winner_display(winner):
    winner_text = WINNER_FONT.render("The winner is "+winner, 1, WHITE)
    WIN.blit(winner_text,(WIDTH/2, HIGHT/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():

    red = pygame.Rect(700, 300, SPACESHIP_HIGHT, SPACESHIP_WIDTH)
    yellow = pygame.Rect(100, 300, SPACESHIP_HIGHT, SPACESHIP_WIDTH)
    red_hp = 5
    yellow_hp = 5

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run =False
                 pygame.quit()
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellowBullets)<MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y+yellow.height//2-2, 10, 5)
                    yellowBullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(redBullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x,  red.y + red.height // 2 - 2, 10, 5)
                    redBullets.append(bullet)

             if event == RED_HIT:
                  red_hp -= 1
             if event == YELLOW_HIT:
                  yellow_hp -= 1

        winner = ""
        if yellow_hp == 0:
            winner = "Yellow wins"
        if red_hp == 0:
            winner = "Red wins"
        if( winner != ""):
            winner_display(winner)
            break

        handle_bullets(yellowBullets, redBullets, yellow, red)
        key_preesed= pygame.key.get_pressed()
        move(key_preesed, red, yellow)
        draw_window(red, yellow, redBullets, yellowBullets, yellow_hp, red_hp)

    main()


if __name__=="__main__":
    main()