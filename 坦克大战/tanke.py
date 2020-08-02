import pygame
import time
import random

from pygame.sprite import Sprite

SCREEN_WIDTH = 23 * 26
SCREEN_HEIGHT = 23 * 26
BG_COLOR = pygame.Color(0, 0, 0)
TEXT_COLOR = pygame.Color(255, 0, 0)

#定义一个基类
class BaseItem(Sprite):
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)


class MainGame():
    window = None  # 接受窗口的对象
    my_tank = None  # 坦克在多个地方使用，定义为类变量
    #存储敌方坦克的列表
    enemyTankList=[]
    #定义敌方坦克的数量
    enemyTankCount=5
    # 存储我放子弹列表的类属性
    myBulletList = []
    #存储敌方子弹的列表
    enemyBulletList=[]
    #存储爆炸的列表
    explodeList = []
    #存储墙壁的列表
    wallList=[]
    # 初始化类的方法
    def __int__(self):
        pass

    # 开始游戏
    def startGame(self):
        # 加载主窗口
        # 初始化窗口
        pygame.display.init()
        # 设置窗口的大小及显示
        MainGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        # 初始化我方坦克
        self.createMyTank()
        #初始化敌方坦克，并将敌方坦克添加到列表
        self.createEnemyTank()
        #初始化墙壁
        self.createWood()
        # 设置窗口标题
        pygame.display.set_caption("坦克大战")
        while True:
            #使坦克移动的速度慢一点
            time.sleep(0.02)   #sleep方法，让循环执行的慢一点         pygame.time.delay(5)
            # 设置窗口填充色
            MainGame.window.fill(BG_COLOR)
            # 获取事件
            self.getEvent()
            MainGame.window.blit(self.getTextSUface("敌方坦克剩余数量%d" %len(MainGame.enemyTankList)), (10, 10))
            # 调用我方坦克显示方法
            #判断我发坦克是否存活
            if MainGame.my_tank and MainGame.my_tank.live:
                 MainGame.my_tank.displayTank()
            else:
                #删除我发坦克
                del MainGame.my_tank
                MainGame.my_tank=None
            #调用展示敌方坦克
            self.blitEnemyTank()
            #显示我方坦克的子弹
            self.blitMyBullet()
            #显示敌方子弹
            self.blitEnemyBullet()
            #展示爆炸效果
            self.blitExplode()
            #显示墙壁
            self.blitWood()
            #调用坦克移动
            #如果坦克的开关开启，才可以移动
            if MainGame.my_tank and MainGame.my_tank.live:
                if not MainGame.my_tank.stop:
                    MainGame.my_tank.move()
                    #检测我方坦克是否与墙壁发生碰撞
                    MainGame.my_tank.hitWood()
                    #检测我方坦克是否与敌方坦克发生碰撞
                    MainGame.my_tank.myTank_hit_enemyTank()
            pygame.display.update()
    #初始化创建墙壁
    def createWood(self):
        #初始化墙壁
        for i in range(3, 11):
            for j in range(14, 16):
                # 初始化墙壁
                wall= Wood(23 * i, j * 23)
                #将墙壁添加到列表中
                MainGame.wallList.append(wall)
    #循环遍历墙壁列表，展示墙壁
    def blitWood(self):
        for wall in MainGame.wallList:
            #判断墙壁是否存活
            if wall.live:
                #调用墙壁的显示方法
                wall.displayWall()
            else:
                #从墙壁列表移除
                MainGame.wallList.remove(wall)
    #创建我方坦克的方法
    def createMyTank(self):
        MainGame.my_tank = MyTank(23 * 7, 23 * 24)
        #创建Music对象
        music = Music('./audios/start.wav')
        #播放音乐
        music.play()
    # 初始化敌方坦克，并将敌方坦克添加到列表
    def createEnemyTank(self):
        top=100
        #循环生成敌方坦克
        for i in range(MainGame.enemyTankCount):
            left=random.randint(23*2,23*24)
            speed=random.randint(1,4)
            enemy=EnemyTank(left,top,speed)
            MainGame.enemyTankList.append(enemy)
    #循环展示爆炸效果
    def blitExplode(self):
        for explode in  MainGame.explodeList:
            #判断是否活着
            if explode.live:
                explode.displayExplode()
            else:
                #在爆炸列表中移除
                MainGame.explodeList.remove(explode)
    # 循环遍历敌方坦克列表，展示敌方坦克
    def blitEnemyTank(self):
        for enemyTank in MainGame.enemyTankList:
            #判断敌方坦克是否活着
            if enemyTank.live:
                enemyTank.displayTank()
                enemyTank.randMove()
                # 检测敌方坦克是否与墙壁发生碰撞
                enemyTank.hitWood()
                #检测敌方坦克是否与我方坦克碰撞
                if MainGame.my_tank and MainGame.my_tank.live:
                    enemyTank.enemyTank_hit_myTank()
                # 放射子弹
                enumeyBullet = enemyTank.shot()
                # 敌方子弹是否是None，如果不为None则添加到敌方子弹列表
                if enumeyBullet:
                    # 将敌方子弹存储在敌方子弹列表
                    MainGame.enemyBulletList.append(enumeyBullet)
            else:#不活着，从敌方坦克列表中移除
                MainGame.enemyTankList.remove(enemyTank)





    #循环遍历我方子弹存储列表
    def blitMyBullet(self):
        for myBullet in MainGame.myBulletList:
            #判断当前的子弹是否是活着的状态，如果是则进行显示及移动，否则在列表中删除
            if myBullet.live:
                myBullet.displayBullet()
                #调用子弹的移动
                myBullet.move()
                #调用检查我方子弹是否与敌方坦克发生碰撞
                myBullet.myBullet_hit_enemyTank()
                # 检测我方子弹是否与墙壁碰撞
                myBullet.hitWood()
            else:
                MainGame.myBulletList.remove(myBullet)

    # 循环遍历敌方子弹存储列表
    def blitEnemyBullet(self):
        for enemyBullet in MainGame.enemyBulletList:
            if enemyBullet.live:  #是否存活，敌方子弹
                enemyBullet.displayBullet()
                enemyBullet.move()
                #调用敌方子弹与我方坦克碰撞的方法
                enemyBullet.enemyBullet_hit_myTank()
                #检测敌方子弹是否与墙壁碰撞
                enemyBullet.hitWood()
            else:
                MainGame.enemyBulletList.remove(enemyBullet)
    # 结束游戏
    def endGame(self):
        print("欢迎再次使用")
        exit()

    # 左上角文字的绘制
    def getTextSUface(self, text):
        # 初始化字体模块
        pygame.font.init()
        # 查看所有的字体
        # print(pygame.font.get_fonts())
        # 获取字体
        font = pygame.font.SysFont("kaiti", 18)
        # 绘制文字信息
        textSurface = font.render(text, True, TEXT_COLOR)
        return textSurface

    # 获取事件
    def getEvent(self):
        # 获取所有事件
        eventList = pygame.event.get()
        # 遍历事件
        for event in eventList:
            # 判断按下的键是关闭还是键盘按下的键
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                #当坦克不存在（死亡）
                if not MainGame.my_tank:
                    #判断按下的是Esc键，让坦克重生
                    if event.key==pygame.K_ESCAPE:
                        #让我方坦克重生及调用创建坦克的方法
                        self.createMyTank()
                if MainGame.my_tank and MainGame.my_tank.live:
                    # 判断按下的是上。下。左。右
                    if event.key == pygame.K_LEFT:
                        # 切换方向
                        MainGame.my_tank.direction = 'L'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print("左边")
                    if event.key == pygame.K_RIGHT:
                        # 切换方向
                        MainGame.my_tank.direction = 'R'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print("右边")
                    if event.key == pygame.K_DOWN:
                        # 切换方向
                        MainGame.my_tank.direction = 'D'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print("下边")
                    if event.key == pygame.K_UP:
                        # 切换方向
                        MainGame.my_tank.direction = 'U'
                        # 修改坦克的开关状态
                        MainGame.my_tank.stop = False
                        # MainGame.my_tank.move()
                        print("上边")
                    if event.key == pygame.K_SPACE:
                        # 如果当前我方子弹列表的大小  小于等于9时候，才可以创建子弹
                        if len(MainGame.myBulletList) <= 9:
                            myBullet = Bullet(MainGame.my_tank)
                            MainGame.myBulletList.append(myBullet)
                            #添加我发坦克发射子弹添加音乐
                            music = Music('./audios/Gunfire.wav')
                            music.play()
                            print("发射")
            #松开方向键，坦克停止移动，（修改坦克开关状态）
            if event.type==pygame.KEYUP:
                #判断松开的键盘是不是方向键
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN or event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT :
                    if MainGame.my_tank and MainGame.my_tank.live:
                        MainGame.my_tank.stop = True


class Tank(BaseItem):
    # 添加距离左边left   距离上边top
    def __init__(self, left, top):
        # 保存加载的图片
        self.images = {
            'U': pygame.image.load('./images/tihuan/tank_U.png'),
            'L': pygame.image.load('./images/tihuan/tank_L.png'),
            'D': pygame.image.load('./images/tihuan/tank_D.png'),
            'R': pygame.image.load('./images/tihuan/tank_R.png'),
        }
        # 方向
        self.direction = 'U'
        # 根据当前图片的方向获取图片  surface
        self.image = self.images[self.direction]
        # 根据图片获取区域
        self.rect = self.image.get_rect()
        # 设置区域的位置
        self.rect.left = left
        self.rect.top = top
        #速度    决定移动的快慢
        self.speed=4
        #坦克移动的开关
        self.stop=True
        #是否活着
        self.live=True
        #新增属性原来坐标
        self.oldLeft=self.rect.left
        self.oldTop=self.rect.top

    # 移动
    def move(self):
        #移动后记录原位置的坐标
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
        #判断坦克的方向进行移动
        if self.direction=='L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction=='U':
            if self.rect.top>0:
                self.rect.top -= self.speed
        elif self.direction=='R':
            if self.rect.left +self.rect.height<23*26:
                self.rect.left += self.speed
        elif self.direction=='D':
            if self.rect.top +self.rect.height<23*26:
                self.rect.top += self.speed

    # 射击
    def shot(self):
        return Bullet(self)

    # 展示坦克
    def displayTank(self):
        # 获取展示的对象
        self.image = self.images[self.direction]
        # 调用bilt方法显示
        MainGame.window.blit(self.image, self.rect)
    #设置当前位置为前一步的位置
    def stay(self):
        self.rect.left=self.oldLeft
        self.rect.top=self.oldTop
    #检测坦克是否与墙壁发生碰撞
    def hitWood(self):
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self,wall):
                #将坐标设置为移动之前的坐标
                self.stay()




# 我方坦克（继承坦克类）
class MyTank(Tank):
    def __init__(self,left,top):
        super(MyTank,self).__init__(left,top)

    #检测我方坦克与敌方坦克发生碰撞
    def myTank_hit_enemyTank(self):
        #循环遍历敌方坦克列表
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(self,enemyTank):
                self.stay()

# 敌方坦克
class EnemyTank(Tank):
    def __init__(self,left,top,speed):
        #调用父类的初始化方法
        super(EnemyTank,self).__init__(left,top)
        #加载图片集
        self.images={
             "L":  pygame.image.load("./images/enemyTank/enemy_L.png"),
             "R": pygame.image.load("./images/enemyTank/enemy_R.png"),
             "U": pygame.image.load("./images/enemyTank/enemy_U.png"),
             "D": pygame.image.load("./images/enemyTank/enemy_D.png")
        }
        #方向，随机生成敌方坦克的方向
        self.direction=self.randDirection()
        #根据方向获取图片
        self.image=self.images[self.direction]
        #区域
        self.rect=self.image.get_rect()
        #对left和top进行赋值
        self.rect.top=top
        self.rect.left=left
        #速度
        self.speed=speed
        #移动开关
        self.flag=True
        #步数变量
        self.step=60
    #随机生成敌方坦克的方向
    def randDirection(self):
        num=random.randint(1,4)
        if num==1:
            return 'U'
        elif num==2:
            return 'L'
        elif num ==3:
            return 'D'
        elif num ==4:
            return 'R'
    # 随机移动敌方坦克
    def randMove(self):
        if self.step<=0:
            #修改方向
            self.direction=self.randDirection()
            #让步数复位
            self.step=60
        else:
            self.move()
            #让步数递减
            self.step -=1
    #重写shot()
    def shot(self):
        #随机生成200以内的数
        num=random.randint(1,200)
        if num<10:
            return Bullet(self)
    #敌方坦克与我方坦克是否发生碰撞
    def enemyTank_hit_myTank(self):
        if pygame.sprite.collide_rect(self,MainGame.my_tank):
            self.stay()


class Bullet(BaseItem):
    def __init__(self,tank):
        #加载图片
        self.image=pygame.image.load('90/pao.jpg')
        #坦克的方向决定子弹的方向
        self.direction=tank.direction
        #获取区域
        self.rect=self.image.get_rect()
        #子弹的left和top与方向有关
        if self.direction=='U':
            self.rect.left=tank.rect.left+tank.rect.width/2-self.rect.width/2
            self.rect.top=tank.rect.top-self.rect.height
        elif self.direction=="D":
            self.rect.left=tank.rect.left+tank.rect.width/2-self.rect.width/2
            self.rect.top=tank.rect.top+tank.rect.height
        elif self.direction=='L':
            self.rect.left=tank.rect.left-self.rect.width
            self.rect.top=tank.rect.top+tank.rect.width/2-self.rect.width/2
        elif self.direction=='R':
            self.rect.left=tank.rect.left+tank.rect.height
            self.rect.top=tank.rect.top+tank.rect.width/2-self.rect.width/2
        #子弹的速度
        self.speed=6
        #子弹的状态，是否碰到墙壁，如果碰到墙壁，修改此状态
        self.live=True
    # 移动
    def move(self):
        if self.direction=='U':
            if self.rect.top>0:
                self.rect.top-=self.speed
            else:
                #修改子弹的状态
                self.live = False
        elif self.direction=='D':
            if self.rect.top+self.rect.height<SCREEN_HEIGHT:
                self.rect.top+=self.speed
            else:
                self.live = False
        elif self.direction == 'R':
            if self.rect.left+self.rect.width<SCREEN_WIDTH:
                self.rect.left+=self.speed
            else:
                self.live = False
        elif self.direction=='L':
            if self.rect.left>0:
                self.rect.left-=self.speed
            else:
                self.live = False
    # 展示子弹
    def displayBullet(self):
        #将图片surface加载到窗口
        MainGame.window.blit(self.image,self.rect)
    #我方子弹与敌方坦克的碰撞
    def myBullet_hit_enemyTank(self):
        #循环遍历敌方坦克列表，判断是否发生碰撞
        for enemyTank in MainGame.enemyTankList:
            if pygame.sprite.collide_rect(enemyTank,self):
                #修改敌方坦克和我方子弹的状态
                enemyTank.live=False
                self.live=False
                #创建爆炸对象
                explode=Explode(enemyTank)
                #将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)
    #敌方子弹与我方坦克的碰撞
    def enemyBullet_hit_myTank(self):
        if MainGame.my_tank and MainGame.my_tank.live:
            if pygame.sprite.collide_rect(MainGame.my_tank, self):
                # 产生爆炸对象
                explode = Explode(MainGame.my_tank)
                # 将爆炸对象添加到爆炸列表中
                MainGame.explodeList.append(explode)
                # 修改敌方子弹与我方坦克的状态
                self.live = False
                MainGame.my_tank.live = False
    #子弹是否碰撞墙壁
    def hitWood(self):
        #循环遍历墙壁列表
        for wall in MainGame.wallList:
            if pygame.sprite.collide_rect(self,wall):
                #修改子弹的生存状态，让子弹消失
                self.live=False
                #墙壁的生命值减少
                wall.hp-=1
                if wall.hp<=0:
                    #修改墙壁的生存状态
                    wall.live=False



class Wood():
    def __init__(self,left,top):
        #加载墙壁图片
        self.image = pygame.image.load('90/wood.jpg')
        #获取墙壁的区域
        self.rect=self.image.get_rect()
        #设置位置left、top
        self.rect.left=left
        self.rect.top=top
        #是否存活
        self.live=True
        #设置生命值
        self.hp=1
    # 展示墙壁的方法
    def displayWall(self):
        MainGame.window.blit(self.image,self.rect)


class Explode():
    def __init__(self,tank):
        #爆炸的位置由当前子弹打中的坦克位置决定
        self.rect=tank.rect
        #加载图片
        self.images=[pygame.image.load("./images/others/blast0.png"),
                       pygame.image.load("./images/others/blast1.png"),
                       pygame.image.load("./images/others/blast2.png"),
                       pygame.image.load("./images/others/blast3.png"),
                       pygame.image.load("./images/others/blast4.png")]
        self.step=0
        self.image=self.images[self.step]  #用索引获取图片
        #是否活着
        self.live=True

    # 展示爆炸效果的方法
    def displayExplode(self):
        if self.step<len(self.images):
            #根据索引获取爆炸对象
            self.image=self.images[self.step]
            self.step+=1
            #添加到主窗口
            MainGame.window.blit(self.image,self.rect)
        else:
            #修改状态
            self.live=False
            self.step=0


class Music():
    def __init__(self,filename):
        self.filename=filename
        #初始化音乐混合器
        pygame.mixer.init()
        #加载音乐
        pygame.mixer.music.load(self.filename)

    # 播放音乐的方法
    def play(self):
        pygame.mixer.music.play()


if __name__ == '__main__':
    MainGame().startGame()
    # MainGame().getTextSUface()
