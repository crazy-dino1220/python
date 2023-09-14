import pygame
import sys
import math

c = 0

pygame.init()
screen = pygame.display.set_mode((640, 320))
pygame.display.set_caption("my game")

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

#迴圈 視窗x功能
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x > 500 and x < 577 and y > 168 and y < 208:

                pygame.draw.circle(background, (0, 0, 255), (200, 100), 30, 0)
                pygame.draw.circle(background, (0, 0, 255), (300, 100), 30, 0)
                pygame.draw.rect(background, (0, 255, 0), (220, 170, 80, 40),
                                 5)
                pygame.draw.ellipse(background, (255, 0, 0),
                                    [105, 10, 300, 300], 5)
    print(pygame.mouse.get_pos())
    screen.blit(background, (0, 0))
    pygame.display.update()