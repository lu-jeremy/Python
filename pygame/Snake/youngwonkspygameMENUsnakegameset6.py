import pygame
from pygame.locals import *
from youngwonkssnakegameset6 import snakegame
import sys

pygame.init()
screen=pygame.display.set_mode((640,640))
#load the images
stop=pygame.image.load("exitbutton.jpeg")
stop=pygame.transform.scale(stop,(150,150))
background=pygame.image.load("youngwonkssnakegamebackground.png")
background=pygame.transform.scale(background,(640,640))
while True:
    pygame.display.update()
    screen.blit(background, (0,0))
    screen.blit(stop,(490,490))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        #if the mouse clicks on any of these areas
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            #these coordinates to these coordinates, play the game
            if 192<=event.pos[0]<=453 and 342<=event.pos[1]<=474:
                snakegame()
                screen=pygame.display.set_mode((640,640))
            #quit the game
            if 490<=event.pos[0]<=640 and 490<=event.pos[1]<=640:
                pygame.quit()
                sys.exit()

    
