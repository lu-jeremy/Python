      import pygame
import random
from pygame.locals import *
pygame.init()
"""
r=100
rchange=10
colors=0
"""
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption('Shapes')
"""

def triangle():
    pygame.draw.line(screen, (0,0,0), (100,244), (400,300))
    pygame.draw.line(screen, (0,0,0), (400,300), (500,400))
    pygame.draw.line(screen, (0,0,0), (500,400), (100,244))
def triangle2():
    pygame.draw.polygon(screen, (255,0,0), [(100,244),(400,400),(600,444)])
    
def checkerboard():
    a=(0,0,255)
    b=(255,0,0)
    c=(0,0,0)
    d=(255,255,255)
    e=(0,255,0)
    something=[a,b,c,d,e]
    for y in range(0,480,80):
        for x in range(0,700,80):
            randomestchoice=random.choice(something)
            if (x+y)%2==0:
                pygame.draw.rect(screen,randomestchoice, (x,y,100,200))          
while True:
    screen.fill((255,255,255))
   
    width=random.randint(0,630)
    height=random.randint(0,470)
    pygame.draw.circle(screen, colors, (320,240), r)
    r=r+rchange
    if r==240:
        rchange=-(rchange)
        a=random.randint(0,255)
        b=random.randint(0,255)
        c=random.randint(0,255)
        colors=a,b,c
    if r==0:
        rchange=-(rchange)
        

 
    checkerboard()
    #pygame.draw.rect(screen, (0,0,255), (320,240, width, height), 10)
    #triangle2()
"""

pygame.display.update()
for event in pygame.event.get():
    if event.type==QUIT:
        pygame.quit()
        exit()
    


