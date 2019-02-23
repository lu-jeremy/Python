import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((640,640))

rightup=0
rightdown=0
leftup=0
leftdown=0

class Ball:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.surface = pygame.Surface((40,40))
        pygame.draw.circle(self.surface,(0,0,255),(20,20),10)
        #self.surface has to have the actual circle in the middle of it or else
        #it will not appear because it will go out out of the self.surface's boundaries
        #self.surface makes a surface for the circle to be drawn onto
    def update(self):
        screen.blit(self.surface,(self.x,self.y))
b = Ball(200,200)
class Paddles:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.up = 0
        self.down = 0
        self.surface = pygame.Surface((10,100))
        pygame.draw.rect(self.surface,(255,255,255),(0,0,10,100))
    def update(self):
        screen.blit(self.surface,(self.x,self.y))
    
left = Paddles(0,300)
right = Paddles(630,0)
while True:
    screen.fill((0,0,0))
    b.update()
    left.update()
    right.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
                if event.key==K_UP:
                    left.up=1
                if event.key==K_i:
                    right.up=1
                if event.key==K_DOWN:
                    left.down=1
                if event.key==K_j:
                    right.down=1
        if event.type==KEYUP:
                if event.key==K_UP:
                    left.up=0
                if event.key==K_i:
                    right.up=0
                if event.key==K_DOWN:
                    left.down=0
                if event.key==K_j:
                    right.down=0
