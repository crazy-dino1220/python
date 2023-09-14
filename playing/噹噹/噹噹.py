import pygame
import sys

# 初始化Pygame
pygame.init()

# 設置視窗大小和標題
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("繁體中文遊戲")

# 設定繁體中文字型
font = pygame.font.Font(None, 36)


def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 清空視窗
        screen.fill((255, 255, 255))

        # 創建一個繁體中文文字
        text = font.render("你好，世界！", True, (0, 0, 0))

        # 在視窗上顯示文字
        screen.blit(text, (300, 250))

        # 更新視窗
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
