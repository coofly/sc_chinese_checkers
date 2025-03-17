import sys
import pygame
from controls import Button


def start_game():
    print("开始游戏")

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("千寻的中国跳棋")
    clock = pygame.time.Clock()
    img_background = pygame.image.load("res/background.png")
    img_background = pygame.transform.smoothscale(img_background, (768, 768)) # 缩放背景图像并抗锯齿
    
    # 创建按钮
    def_font = pygame.font.SysFont(["Microsoft Yahei","SimHei"], 32)
    button_start = Button("开始游戏", def_font, (0, 128, 0), (1024 - 150 - 20, 768 - 50 - 20), start_game)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # 处理鼠标事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_start.mouse_over():
                        button_start.click()
        # 绘制游戏背景
        window.fill((255, 255, 255))
        window.blit(img_background, ((1024 - 768) // 2, 0)) # 使用计算出的坐标
        
        # 绘制按钮
        button_start.draw(window)
        
        pygame.display.update() # 更新屏幕
        clock.tick(60) # 限制帧率
    pygame.quit()
    sys.exit()