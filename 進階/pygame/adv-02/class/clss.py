import pygame
import sys
import math

c = 0


def check_click(pos, x_min, y_min, x_max, y_max):
    x = pos[0]
    y = pos[1]
    if x > x_min and x < x_max and y > y_min and y < y_max:
        return True
    else:
        return False


pygame.init()
screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("snow")

background = pygame.Surface((640, 320))
background.fill((0, 255, 150))

# pygame.draw.circle(background, (0, 0, 255), (200, 100), 30, 0)
# pygame.draw.circle(background, (0, 0, 255), (300, 100), 30, 0)
# pygame.draw.rect(background, (0, 255, 0), (220, 170, 80, 40), 5)
# pygame.draw.ellipse(background, (255, 0, 0), [105, 10, 300, 300], 5)
#pygame.draw.line(background, (255, 0, 255), (280, 220), (280, 1), 3)
# pygame.draw.polygon(background, (100, 200, 45),
#                     [[100, 100], [0, 200], [200, 200]], 0)
# pygame.draw.arc(background, (255, 10, 0), [100, 100, 100, 50],
#                 math.radians(180), math.radians(0), 2)
pygame.draw.rect(background, (0, 255, 0), (500, 170, 80, 40), 5)
typeface = pygame.font.get_default_font()
font = pygame.font.Font(typeface, 24)
title = font.render("start", True, (0, 0, 0))
tit_w = title.get_width()
tit_h = title.get_height()

#迴圈 視窗x功能
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if c == 0:
                x, y = pygame.mouse.get_pos()
                if x > 500 and x < 577 and y > 168 and y < 208:

                    pygame.draw.circle(background, (0, 0, 255), (200, 100), 30,
                                       0)
                    pygame.draw.circle(background, (0, 0, 255), (300, 100), 30,
                                       0)
                    pygame.draw.rect(background, (0, 255, 0),
                                     (220, 170, 80, 40), 5)
                    pygame.draw.ellipse(background, (255, 0, 0),
                                        [105, 10, 300, 300], 5)

                    c = 1
            elif c == 1:
                pos = pygame.mouse.get_pos()
                # if x > 500 and x < 577 and y > 168 and y < 208:
                if check_click(pos, 500, 168, 500 + tit_w, 168 + tit_h):
                    background.fill((0, 255, 150))
                    pygame.draw.rect(background, (0, 255, 0),
                                     (500, 170, 80, 40), 5)

                c = 0

    print(pygame.mouse.get_pos())
    screen.blit(background, (0, 0))
    screen.blit(title, (513, 178))
    pygame.display.update()