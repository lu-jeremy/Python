import pygame, sys
from pygame.locals import *
from dxball_second import main_loop
import sys
import random

pygame.init()
screen = pygame.display.set_mode((640,640))

pygame.display.set_caption("Round 1")


class Pad:
    def __init__(self):
        self.x = 100
        self.y = 540
        self.speedx = 15
        self.pad = pygame.image.load('launch_pad.png').convert_alpha()
        self.pad.set_colorkey((0,0,0))
        self.pad = pygame.transform.scale(self.pad,(120,120))
        self.rect = self.pad.get_rect()
    def update(self):
        screen.blit(self.pad,(self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

class Ball:
    def __init__(self,x ,y ):
        self.x = x
        self.y = y
        self.speedy = -7
        self.speedx = 3
        self.ball = pygame.image.load('dx_ball.png').convert()
        self.ball = pygame.transform.scale(self.ball,(35,35)).convert_alpha()
        self.ball.set_colorkey((0,0,0))
        self.rect = self.ball.get_rect()
    def update(self):
        screen.blit(self.ball,(self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y
    def movement(self):
        self.y += self.speedy
        self.x += self.speedx
        if self.x >= 625:
            self.speedx = -(self.speedx)
        if self.y <= 0:
            self.speedy = -(self.speedy)
        if self.x <= 0:
            self.speedx = -(self.speedx)

class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.block = pygame.image.load('brick.png').convert()
        self.block = pygame.transform.scale(self.block,(30,30))
        self.rect = self.block.get_rect()
    def update(self):
        screen.blit(self.block,(self.x,self.y))
        self.rect.x = self.x
        self.rect.y = self.y

class Bricks:
    def __init__(self):
        self.block_list = []
        self.shape_list = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                           [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                           [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
                           [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
                           [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
                           [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
                           ]
        for n in range(10):
           for m in range(20):
               if self.shape_list[n][m] == 1:
                   creation = Block(30+m*30,0+n*30)
                   self.block_list.append(creation)
    def update(self):
        for var in self.block_list:
            var.update()

def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
p = Pad()
b = Ball(p.x+40,p.y-40)
c = Bricks()
b2 = Ball(20,50)
#variables:
count = 0
i = 1
v = 0
score = 0

running = True
while running:
    screen.fill((0,0,0))
    c.update()
    p.update()
    b.update()
    
    show_text("Points: %s"%score, 476,600, (255,255,255))

    pygame.display.update()
    if b.y >= 640:
        show_text("Game Over.", 300,320, (255,255,255))
        show_text("Try again?", 0,600, (0,255,0))
        pygame.display.update()
        break                  
    if len(c.block_list) == 0:
        show_text("You Win!", 300,320, (255,255,255))
        pygame.display.update()
        main_loop()                           

    for block in c.block_list:
        if b.rect.colliderect(block.rect):
            c.block_list.remove(block)
            b.speedy = -(b.speedy)
            i = 1
            score += 10
            pygame.mixer.music.load('bounce_sound.wav')
            pygame.mixer.music.play(0)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        p.x -= p.speedx
    if keys[pygame.K_RIGHT]:
        p.x += p.speedx


    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_UP:
                count = 1
            if event.key == K_DOWN:
                if score >= 100:
                    v = 1
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if 0<=event.pos[0]<=32 and 600<=event.pos[1]<=632:
                running = False
                
    if v == 1:
        show_text("Double Mode Activated",10,400, (255,0,0))
        pygame.display.update()
        b2.update()
        b2.movement()
        print(len(b2))
    if count == 1:
        b.movement()
        if i == 1:
            if b.rect.colliderect(p.rect):
                b.speedy = -(b.speedy)
                i = 0


