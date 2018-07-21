import pygame
from pygame.locals import *
from youngwonkspongset5pygame import pongset
import sys
pygame.init()
screen=pygame.display.set_mode((640,640))
play=pygame.image.load("yongwonksplaybuttonpongset.jpg")
play=pygame.transform.scale(play,(150,150))
stop=pygame.image.load("youngwonksexitbuttonpongset.jpeg")
stop=pygame.transform.scale(stop,(150,150))
background=pygame.image.load("youngwonksbackgroundpongset.png")
background=pygame.transform.scale(background,(640,640))
while True:
    pygame.display.update() 
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if 0<=event.pos[0]<=150 and 490<=event.pos[1]<=640:
                pongset()
            if 490<=event.pos[0]<=640 and 490<=event.pos[1]<=640:
                pygame.quit()
                sys.exit()
    screen.blit(background, (0,0))
    screen.blit(play,(0,490))
    screen.blit(stop,(490,490))
    
        
    
