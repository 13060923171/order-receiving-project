import pygame
from pygame.locals import *
from plane import *

class Bullet(object):
    def __init__(self, x, y, screen, name):
        self.x = x + 40
        self.y = y - 20
        self.screen = screen
        self.name = name
        self.image = pygame.image.load("./feiji/bullet-3.gif").convert()
        #用来储存英雄飞机发射的所有子弹
        self.bullet_list = []
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
    def move(self):
        self.y -= 2
    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self, x, y, screen, name):
        self.x = x + 30
        self.y = y - 30
        self.screen = screen
        self.name = name
        self.image = pygame.image.load("./feiji/bullet-1.gif").convert()
        self.bullet_list = []
    def move(self):
        self.y += 2
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        need_del_list = []
        for i in self.bullet_list:
            if i.judge():
                need_del_list.append(i)
        for i in need_del_list:
            self.bullet_list.remove(i)
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
    def judge(self):
        if self.y > 890:
            return True
        else:
            return False

class PublicBullet(object):
    def __init__(self, x, y, screen, plane_name):
        self.screen = screen
        self.plane_name = plane_name
        if plane_name == "hero":
            self.x = x + 40
            self.y = y - 20
            image_name = "./feiji/bullet-3.gif"
        elif plane_name == "enemy":
            self.x = x + 30
            self.y = y + 30
            image_name = "./feiji/bullet-1.gif"
        self.image = pygame.image.load(image_name).convert()
    def move(self):
        if self.plane_name == "hero":
            self.y -= 2
        elif self.plane_name == "enemy":
            self.y += 2
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
    def judge(self):
        if self.y > 890 or self.y < 0:
            return True
        else:
            return False