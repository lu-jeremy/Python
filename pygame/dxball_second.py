import pygame
from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((640,640))
screen = pygame.display.set_caption('Round 2')

# class Ball:

class Block:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.block = pygame.image.load('bricks2.png').convert()
        self.block = pygame.transform.scale(self.block,(30,30))
        self.rect = self.block.get_rect()
    def update(self):
        screen.blit(self.block,(self.x,self.y))
        self.rect.x = self.x
        self.rect.y = self.y

class Bricks:
    def __init__(self):
        self.block_list = []
        self.shape_list = [[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0],
                           [0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0],
                           [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
                            ]
                           
        for n in range(5):
           for m in range(20):
               if self.shape_list[n][m] == 1:
                   creation = Block(30+m*30,0+n*30)
                   self.block_list.append(creation)
    def update(self):
        for var in self.block_list:
            var.update()
b = Bricks()
               
            
def main_loop():
    while True:
        screen.fill((0,0,0))
        b.update()

        pygame.display.update()


