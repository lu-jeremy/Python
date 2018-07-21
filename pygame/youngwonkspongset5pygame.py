import pygame
from pygame.locals import *
import time
import sys
import random
def pongset():
    pygame.init()
    screen=pygame.display.set_mode((640,640))
    upy=320
    upy2=320
    speedcirclex=5
    speedcircley=0
    circlex=320
    circley=320
    rightpadup=0
    rightpaddown=0
    leftpadup=0
    leftpaddown=0
    leftpoints=0
    rightpoints=0
    def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont("freesans",32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
    while True:
        screen.fill((255,255,255))
        show_text("Points",0,0,(0,0,0))
        show_text(str(leftpoints), 50,50, (0,0,0))
        show_text("Points",560,0,(0,0,0))
        show_text(str(rightpoints), 620,50, (0,0,0))
        pygame.draw.rect(screen,(0,0,0), (0,upy,10,100))
        pygame.draw.rect(screen,(0,0,0), (630,upy2,10,100))
        pygame.draw.circle(screen,(0,0,255),(circlex,circley),10)
        circlex=speedcirclex+circlex
        circley=speedcircley+circley
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_UP:
                    leftpadup=1
                if event.key==K_i:
                    rightpadup=1
                if event.key==K_DOWN:
                    leftpaddown=1
                if event.key==K_j:
                    rightpaddown=1
            if event.type==KEYUP:
                if event.key==K_UP:
                    leftpadup=0
                if event.key==K_i:
                    rightpadup=0
                if event.key==K_DOWN:
                    leftpaddown=0
                if event.key==K_j:
                    rightpaddown=0
        if leftpadup==1:
            upy=upy-5
        if rightpadup==1:
            upy2=upy2-5
        if leftpaddown==1:
            upy=upy+5
        if rightpaddown==1:
            upy2=upy2+5
        if upy<=0:
            upy=0
        if upy>=540:
            upy=540
        if upy2<=0:
            upy2=0
        if upy2>=540:
            upy2=540
        if circlex>=640:
            speedcircley=0
        if circlex<=0:
            speedcircley=0
        if circlex>=710:
            circlex=320
            leftpoints=leftpoints+1
            time.sleep(0.5)
        if circlex<=-60:
            circlex=320
            rightpoints=rightpoints+1
            time.sleep(0.5)
        if circley>=640:
            speedcircley=-(speedcircley)           
        if circley<=0:
            speedcircley=-(speedcircley)
        if upy<=circley<=upy+100 and circlex<=10:
            speedcirclex=-(speedcirclex)
            speedcircley=random.randint(-5,5)
        if upy2<=circley<=upy2+100 and circlex>=630:
            speedcirclex=-(speedcirclex)
            speedcircley=random.randint(-5,5)
        if leftpoints==5:
            show_text("Left side has won the whole game.", 182,320, (0,0,0))
            pygame.display.update()
            time.sleep(3)
            return
        if rightpoints==5:
            show_text("Right side has won the whole game.", 182, 320, (0,0,0))
            pygame.display.update()
            time.sleep(3)
            return
pongset()
