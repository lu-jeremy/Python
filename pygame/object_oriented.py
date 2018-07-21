import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((640,640))
"""
class Ball:
    def __init__(self,x=240,y=460,color=(0,0,255)):
        self.x = x
        self.y = y
        self.color = color
        self.surface = pygame.Surface((40,40))
        pygame.draw.circle(self.surface,self.color,(20,20), 20)
    def update(self):
        screen.blit(self.surface,(self.x,self.y))
    def isclicked(self, mouse_pos):
        if self.x<mouse_pos[0] < self.x + 40 and self.y<mouse_pos[1]<self.y+40 :

            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color = (r,g,b)
            self.change_color(color)
            return True
        else:
            return False
    def change_color(self,color):
        self.color = color
        pygame.draw.circle(self.surface,self.color,(20,20), 20)
blue =  (0,0,255)
green = (0,255,0)
# making an object
ballone = Ball()
ball = Ball(240,390,blue)
balltwo = Ball(random.randint(0,640),random.randint(0,640),green)
ball_objects = []
ball_objects.append(balltwo)
ball_objects.append(ball)

print(ball_objects)
while True:
    screen.fill((0,0,0))
    for b in ball_objects:
        b.update()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for b in ball_objects:
                b.isclicked(event.pos)
        if event.type==KEYDOWN:
            if event.key == K_SPACE:
                ball = Ball(random.randint(0,640),random.randint(0,640),green)
                ball_objects.append(ball)
"""

