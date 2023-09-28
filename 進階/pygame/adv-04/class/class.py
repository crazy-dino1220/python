######################匯入模組######################
import pygame
import os
import sys
import random


####################定義函式######################
def gophers_update():
    global tick, pos, score
    if tick > max_tick:
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
        score += 1
    else:
        tick += 1
    pygame.draw.circle(screen, blue, pos, 50)


def score_update():
    score_sur = score_font.render(str(score, False, red))
    screen.blit(score_sur, (10, 10))


####################初始化######################
pygame.init()
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0
max_tick = 20
######################建立視窗######################
bg_x = 600
bg_y = 400
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("打地鼠")
######################背景物件######################
bg = pygame.Surface([bg_x, bg_y])
bg.fill(black)
######################地鼠物件######################
pos6 = [[200, 200], [300, 200], [400, 200], [200, 300], [300, 300], [400, 300]]
pos = pos6[0]
######################分數物件######################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
######################滑鼠物件######################

######################循環偵測######################
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(bg, (0, 0))
    gophers_update()
    score_update()
    pygame.display.update()