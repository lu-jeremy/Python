import pygame
from pygame.locals import *
import random
import sys
import time

pygame.init()

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption('Snake')

class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinate_list = []
        self.coordinate_list.append(self.x)
        self.coordinate_list.append(self.y)
        self.surface = pygame.Surface((20,20))
        self.rect = pygame.draw.rect(self.surface,
                                      (60, 179, 113), (0, 0, 20, 20))
        self.snake_list = []
    def update(self, x, y):
        screen.blit(self.surface, (x, y))
        self.coordinate_list.insert(0, x)
        self.coordinate_list.insert(1, y)
        self.rect.x = self.x
        self.rect.y = self.y
    def moveUp(self):
        self.y -= 5
    def moveDown(self):
        self.y += 5
    def moveLeft(self):
        self.x -= 5
    def moveRight(self):
        self.x += 5


class Food:
    def __init__(self):
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 200)
        self.surface = pygame.Surface((20,20))
        self.rect = pygame.draw.circle(self.surface, (0, 191, 255),
                                        (10, 10), 10)
    def update(self):
        screen.blit(self.surface, (self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

        
s = Snake(300, 200)
f = Food()
s.snake_list.append(s)

count = None

while True:
    pygame.display.update()
    
    screen.fill((0,0,0))
    
    f.update()

    for snake in s.snake_list:
        snake.update(s.coordinate_list[0], s.coordinate_list[1])
        s.coordinate_list.pop(0)
        s.coordinate_list.pop(1)
        
    for snake in s.snake_list:
        if f.rect.colliderect(s.rect):
            f.x = random.randint(0, 300)
            f.y = random.randint(0, 200)
            f.update()
            x_var = s.x - 20
            y_var = s.y
            new_s = Snake(x_var, y_var)
            s.snake_list.append(new_s)
            s.coordinate_list.insert(0, x_var)
            s.coordinate_list.insert(1, y_var)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit(); sys.exit()
            
        if event.type == KEYDOWN:
            if event.key == K_UP:
                count = 0
            if event.key == K_DOWN:
                count = 1
            if event.key == K_LEFT:
                count = 2
            if event.key == K_RIGHT:
                count = 3
        
    if count == 3:
        s.moveRight()
    if count == 1:
        s.moveDown()
    if count == 2:
        s.moveLeft()   
    if count == 0:
        s.moveUp()
