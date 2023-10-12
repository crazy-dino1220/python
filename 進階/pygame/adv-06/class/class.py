######################匯入模組######################
import pygame
import os
import sys
import random


####################定義函式######################
def check_click(pos, x_min, y_min, x_max, y_max):
    """判斷滑鼠是否點擊在指定的區域內"""
    x_match = x_min < pos[0] < x_max
    y_match = y_min < pos[1] < y_max
    if x_match and y_match:
        return True
    else:
        return False


def gophers_update():
    global tick, pos, times, gophers, gophers_tick

    if tick > max_tick:
        new_pos = random.randint(0, 5)
        pos = pos6[new_pos]
        tick = 0
        times += 1
    else:
        tick += 1

    if gophers == gophers2:
        if gophers_tick > gophers_tick_max:
            gophers = gophers1
            gophers_tick = 0

        else:
            gophers_tick += 1

    screen.blit(
        gophers,
        (pos[0] - gophers.get_width() / 2, pos[1] - gophers.get_height() / 2))


def score_update():
    score_sur = score_font.render(str(score), False, red)
    screen.blit(score_sur, (10, 10))


def times_update():
    times_sur = time_font.render(str(times), True, red)
    screen.blit(times_sur, (bg_x - times_sur.get_width() - 10, 10))


def game_over():
    screen.fill(black)
    end_sur = score_font.render(f"Game Over~ Your Score is:{score}", False,
                                red)
    screen.blit(end_sur, (bg_x / 2 - end_sur.get_width() / 2,
                          bg_y / 2 - end_sur.get_height() / 2))


def mouse_update():
    global hammer, hammer_tick
    if hammer == ham1:
        if hammer_tick > hammer_max_tick:
            hammer = ham2
            hammer_tick = 0
        else:
            hammer_tick += 1
    screen.blit(hammer, (mouse_pos[0] - 15, mouse_pos[1] - 15))


####################初始化######################
os.chdir(sys.path[0])
pygame.init()
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
clock = pygame.time.Clock()
tick = 0
max_tick = 20
bg_img = "Gophers_BG_800x600.png"
bg = pygame.image.load(bg_img)
bg_x = bg.get_width()
bg_y = bg.get_height()
######################建立視窗######################

screen = pygame.display.set_mode([bg_x, bg_y])
pygame.display.set_caption("打地鼠")
######################地鼠物件######################
pos6 = [[195, 305], [400, 305], [610, 305], [195, 450], [400, 450], [610, 450]]
pos = pos6[0]
gophers1 = pygame.image.load("Gophers150.png")
gophers2 = pygame.image.load("gophers2_150_360.png")
gophers = gophers1
gophers_tick = 0
gophers_tick_max = 5
######################分數物件######################
score = 0
typeface = pygame.font.get_default_font()
score_font = pygame.font.Font(typeface, 24)
######################音樂物件######################
mp3_path = "hit.mp3"
pygame.mixer.music.load(mp3_path)  # 音樂載入程式

pygame.mixer.music.fadeout(5)
######################次數物件######################
times = 0
times_max = 5
typeface = pygame.font.get_default_font()
time_font = pygame.font.Font(typeface, 24)
hit = 0
######################滑鼠物件######################
pygame.mouse.set_visible(False)
ham1 = pygame.image.load("hammer1_360.png")
ham2 = pygame.image.load("hammer2_360.png")
hammer = ham2
hammer_tick = 0
hammer_max_tick = 5
######################循環偵測######################
while True:
    clock.tick(20)
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            hammer = ham1
            if check_click(mouse_pos, pos[0] - 50, pos[1] - 50, pos[0] + 50,
                           pos[1] + 50):
                tick = max_tick + 1
                score += 1
                gophers = gophers2
                pygame.mixer.music.play()
            else:
                hit = 0
    if times >= times_max:
        game_over()
    else:
        screen.blit(bg, (0, 0))
        gophers_update()

        score_update()
        times_update()
        mouse_update()

    pygame.display.update()