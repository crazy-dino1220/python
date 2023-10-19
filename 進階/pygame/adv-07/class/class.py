######################匯入模組######################
import pygame
import os
import sys
import random
import time


####################定義函式######################
def bg_update():
    global bg_roll_x

    bg_roll_x = (bg_roll_x - 10) % bg_x
    screen.blit(image, (bg_roll_x - bg_x, 0))
    screen.blit(image, (bg_roll_x, 0))


def move_dino():
    global ds_y, ds_index

    ds_index = (ds_index - 1) % len(image_dino)
    screen.blit(image_dino[ds_index], (ds_x, ds_y))


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
LIMIT_LOW = 140
clock = pygame.time.Clock()
####################載入圖片物件######################
image = pygame.image.load("bg_720.png")
image_dino = [
    pygame.image.load("_________1_360.png"),
    pygame.image.load("_________2_360.png")
]
bg_x = image.get_width()
bg_y = image.get_height()
bg_roll_x = 0
######################建立視窗######################
screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("dino")
######################分數物件######################

######################恐龍物件######################
ds_x = 50
ds_y = LIMIT_LOW
ds_index = 0
jumpStave = False
jumpValue = 0
jump_height = 13

######################仙人掌物件######################

######################循環偵測######################
while True:
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    bg_update()
    move_dino()
    pygame.display.update()
