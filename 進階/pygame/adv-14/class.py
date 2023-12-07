######################載入套件######################
import pygame
import sys
import os
from pygame.locals import *


class Missile:
    def __init__(self, x, y, image, shift):
        self.x = x
        self.y = y
        self.image = image
        self.active = False
        self.shift = shift

    def launch(self, x, y):
        if not self.active:
            self.x = x
            self.y = y
            self.active = True

    def move(self):
        if self.active:
            self.y -= self.shift
            if self.y < 0:
                self.active = False

    def draw(self, screen):
        if self.active:
            screen.blit(self.image, (self.x, self.y))


######################定義函式區######################
def roll_bg():
    """捲動背景"""
    global roll_y
    roll_y = (roll_y + 20) % bg_y  # 背景捲動
    screen.blit(img_bg, [0, roll_y - bg_y])  # 上半部
    screen.blit(img_bg, [0, roll_y])  # 下半部


def move_starship():
    global ss_x, ss_y, ss_wh, ss_hh, ss_img, burn_shift
    key = pygame.key.get_pressed()
    ss_img = img_sship[0]
    if key[pygame.K_UP]:
        ss_y -= 20
    if key[pygame.K_DOWN]:
        ss_y += 20
    if key[pygame.K_LEFT]:
        ss_x -= 20
        ss_img = img_sship[1]
    if key[pygame.K_RIGHT]:
        ss_x += 20
        ss_img = img_sship[2]
    ss_hh = ss_img.get_height() / 2
    ss_wh = ss_img.get_width() / 2
    if ss_y < ss_hh:
        ss_y = ss_hh
    if ss_y > bg_y - ss_hh:
        ss_y = bg_y - ss_hh
    if ss_x < ss_wh:
        ss_x = ss_wh
    if ss_x > bg_x - ss_wh:
        ss_x = bg_x - ss_wh
    burn_shift = (burn_shift + 2) % 6
    screen.blit(img_burn, [ss_x - burn_w / 2, ss_y + burn_h + burn_shift])
    screen.blit(ss_img, [ss_x - ss_wh, ss_y - ss_hh])


######################初始化設定######################
os.chdir(sys.path[0])
pygame.init()
clock = pygame.time.Clock()

######################載入圖片######################
# 載入背景圖片
img_bg = pygame.image.load("space_720.png")
img_sship = pygame.image.load("fighter_m_360.png")
img_sship = [
    pygame.image.load("fighter_m_360.png"),
    pygame.image.load("fighter_l_360.png"),
    pygame.image.load("fighter_r_360.png"),
]
img_burn = pygame.image.load("starship_burner_360.png")
######################遊戲視窗設定######################
bg_x = img_bg.get_width()  # 背景圖片寬度
bg_y = img_bg.get_height()  # 背景圖片高度
bg_size = (bg_x, bg_y)  # 背景圖片大小
pygame.display.set_caption("Galaxy Lancer")
screen = pygame.display.set_mode(bg_size)
roll_y = 0

######################玩家設定######################
ss_x = bg_x / 2
ss_y = bg_y / 2
ss_wh = img_sship[0].get_width() / 2
ss_hh = img_sship[0].get_height() / 2
ss_img = img_sship[0]
burn_shift = 0
burn_w, burn_h = img_burn.get_rect().size
######################主程式######################
while True:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_F11:
                screen = pygame.display.set_mode(bg_size, FULLSCREEN)
            elif event.key == K_ESCAPE:
                screen = pygame.display.set_mode(bg_size)

    roll_bg()  # 捲動背景
    move_starship()
    pygame.display.update()
