from plane import *

def start():        #开始游戏
    # 1. 创建一个游戏的窗口，显示内容
    screen = pygame.display.set_mode((480, 890), 0, 32)
    #2. 创建一个和窗口大小的图片，用来充当背景
    image_file_path = './feiji/background.png'
    #3.把背景图片放到窗口中显示
    background = pygame.image.load(image_file_path).convert()
    hero_plane = HeroPlane(screen,"hero")
    # 4.把背景图片放到窗口中显示
    enemy_plane = EnemyPlane(screen,"enemy")

    while True:
        screen.blit(background, (0, 0))
        hero_plane.display()
        enemy_plane.display()
        enemy_plane.move()
        enemy_plane.launch_bullet()
        # 判断是否点击了退出按钮
        for event in pygame.event.get():
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    # 控制飞机让其向左移动
                    hero_plane.move_left()
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    # 控制飞机让其向右移动
                    hero_plane.move_right()
                elif event.key == K_SPACE:
                    print('space')
                    hero_plane.launch_bullet()
        time.sleep(0.01)
        pygame.display.update()

if __name__ == '__main__':
    start()