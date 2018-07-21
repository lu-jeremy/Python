import pygame
import sys
from pygame.locals import *
from youngwonkspyset2 import tictactoeofficial
pygame.init()
screen=pygame.display.set_mode((640,640))
pygame.display.set_caption("Menu")
screen.fill((255,255,255))
background=pygame.image.load("tictactoe2.jpg")
background=pygame.transform.scale(background,(640,640))
play=pygame.image.load("playbutton.png")
play=pygame.transform.scale(play,(300,300))
stop=pygame.image.load("exitbutton.jpg")
stop=pygame.transform.scale(stop,(200,300))
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if 0<=event.pos[0]<=300 and 213<=event.pos[1]<=513:
                tictactoeofficial()
            if 426<=event.pos[0]<=626 and 213<=event.pos[1]<=513:
                pygame.quit()
                sys.exit()
    screen.blit(background,(0,0))
    screen.blit(play,(0,213))
    screen.blit(stop,(426,213))
        
