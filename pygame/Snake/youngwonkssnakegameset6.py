import pygame
from pygame.locals import*
import random
import sys
import time
def snakegame():
    screen=pygame.display.set_mode((1040,640))
    pygame.init()
    #variable divide by 40 to have a multiple of 40 to be vertically or horizontally parallel
    foodx=((random.randint(0,1000)//40))*40
    foody=((random.randint(0,600)//40))*40
    snakex=((random.randint(0,1000)//40))*40
    snakey=((random.randint(0,600)//40))*40
    points=0
    #down, left, up, and right in order for smooth motion
    down=0
    left=0
    up=0
    right=0
    snakelist= []
    #clock, to slow down or speed up time; lower value=slower
    clock=pygame.time.Clock()
    snakelist.append((snakex,snakey))
    #show text
    """
    def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont("freesans",32)
        msgobj= fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
        """
    while True:
        clock.tick(15)
        pygame.display.update()
        screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            #detection
            elif event.type == KEYDOWN:
                #HAVE to have "'opposite direction'==0", so no opposite direction occurs at the same time as occuring direction
                if event.key == K_DOWN and up==0:
                    down = 1
                    left = 0
                    up = 0
                    right =0
                    down=1
                if event.key == K_UP and down==0:
                    up=1
                    down = 0
                    left = 0
                    right =0
                if event.key==K_LEFT and right==0:
                    left=1
                    right=0
                    up=0
                    down=0
                if event.key==K_RIGHT and left==0:
                    right=1
                    left=0
                    up=0
                    down=0
        if down==1:
            #movement; +40= the y goes higher, so the snake goes down
            snakey=snakey+40
        if left==1:
            snakex = snakex-40
        if up==1:
            snakey= snakey-40
        if right==1:
            snakex=snakex+40
        #get rid of the old coordinates and replace with new snake coordinates to keep updated
        snakelist.pop()
        snakelist.insert(0,(snakex,snakey))
        #when the snake overlaps
        if (snakex,snakey) in snakelist[1:]:
            return
        #if snake goes out of boundaries
        if snakex<-10 or snakey<-10 or snakex>=1040 or snakey>=640:
            pygame.display.update()
            time.sleep(2)
            return
        #if snake touches food, make the food goes somewhere else randomly
        if snakex==foodx and snakey==foody:
            points=points+1

            pygame.display.update()
            foodx=((random.randint(0,1000)//40))*40
            foody=((random.randint(0,600)//40))*40
            #to make the snake longer
            snakelist.insert(0,(snakex,snakey))
        if points==5:
            time.sleep(2)
            clock.tick(25)
        #to draw the food
        pygame.draw.rect(screen, (255,0,0), (foodx, foody,40, 40))
        # to draw rectangles for all the coordinates in snakelist
        for loop_var in snakelist:
            pygame.draw.rect(screen, (0,255,0), (loop_var+(40, 40)))
snakegame()
