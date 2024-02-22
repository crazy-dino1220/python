######################匯入模組######################
import pygame
import sys
import os
from pygame.locals import *
import random
from collections import deque

######################匯入圖片######################


######################初始化設定######################
os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
bg = pygame.image.load("BACKGROUND.png")
bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################

screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("RubbishMan")
#####################主程式#########################
screen.blit(bg, (0, 0))
# 讓視窗維持在螢幕上
pygame.display.update()
# 開始運行
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # 讓視窗維持在
pygame.display.update()
