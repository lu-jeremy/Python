import pygame
from pygame.locals import *
import random

pygame.init()
screen = pygame.display.set_mode((640,640))

green = (0,255,0)
blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
storing = []
class Ball:
    def __init__(self,x = 320,y = 240, color = blue):
        self.x = x
        self.y = y
        self.color = color
        self.surface = pygame.Surface((40,40))
        pygame.draw.circle(self.surface,self.color,(20,20), 20)
    def update(self):
        screen.blit(self.surface,(self.x,self.y))
    def isclicked(self,mouse_pos):
        if self.x < mouse_pos[0] < self.x+40 and self.y < mouse_pos[1] <self.y+40:
            self.change_color()
            return True
        else:
            return False
    def change_color(self):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        pygame.draw.circle(self.surface,(r,g,b),(20,20), 20)
b2 = Ball(200,200,red)
b1 = Ball(400,400, white)
while True:
    screen.fill((0,0,0))
    b1.update()
    b2.update()
    for b in storing:
        b.update()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            b2.isclicked(event.pos)
            b1.isclicked(event.pos)
            storing.append(b2)
            storing.append(b1)
            if event.type==KEYDOWN:
                if event.key == K_SPACE:
                    r = random.randint(0,255)
                    g = random.randint(0,255)
                    b = random.randint(0,255)
                    ccolor = (r,g,b)
                    b3 = Ball(random.randint(0,640),random.randint(0,640),ccolor)
                    storing.append(b3)
