######################匯入模組######################
import sys
import os
import pygame
import math
####################定義函式######################

####################初始化######################
pygame.init()
os.chdir(sys.path[0])
bg_img = "snow.jpg"
bg = pygame.image.load(bg_img)

bg_X = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################
screen = pygame.display.set_mode((bg_X, bg_y))
pygame.display.set_caption("my game")
####################撥放音樂######################
mp3_path = "snow-dream.mp3"
pygame.mixer.music.load(mp3_path)
pygame.mixer.music.play()
pygame.mixer.music.fadeout(6000000)
####################設定文字######################
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("START", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()
####################設定雪花基本參數######################

####################新增fps######################
clock = pygame.time.Clock()
while True:
    clock.tick(20)

    mouse_pos = pygame.mouse.get_pos()
    ...
    screen.blit(bg(0, 0))
######################循環偵測######################
c = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if c == 0:
                title = font.render("STOP", True, (0, 0, 0))
                c = 1
            elif c == 1:
                title = font.render("START", True, (0, 0, 0))
                c = 0

    screen.blit(bg, (0, 0))
    screen.blit(title, (0, 0))
    pygame.display.update()