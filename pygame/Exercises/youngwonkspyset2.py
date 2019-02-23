import pygame
import time
import sys
from pygame.locals import *
def tictactoeofficial():
    pygame.init()
    screen=pygame.display.set_mode((640,640))
    screen.fill((255,255,255))
    numbers= {(0,0):"",(213,0):"",(426,0):"",(0,213):"",(213,213):"",(426,213):"",(0,426):"",(213,426):"",(426,426):""}
    counter=0
    x=0
    y=0
    def show_text(msg,x,y,color):
        fontobj=pygame.font.SysFont("freesans",32)
        msgobj=fontobj.render(msg,False,color)
        screen.blit(msgobj,(x,y))
    def tictactoe():
        a=(0,255,0)
        b=(0,0,255)
        for y in range(0,640,213):
            for x in range(0,900,213):
                pygame.draw.rect(screen, a, (x,y, 213,213))
                a,b=b,a
    tictactoe()
    def crossx(n1):   
        pygame.draw.line(screen,(0,0,0),(n1),(n1[0]+213,n1[1]+213),10)
        pygame.draw.line(screen,(0,0,0),(n1[0],n1[1]+213),(n1[0]+213,n1[1]),10)
    def circleo(n2):
        pygame.draw.circle(screen,(0,0,0),(n2[0]+106,n2[1]+107),100)
    def win():
        if numbers[(0,0)]==numbers[(213,213)]==numbers[(426,426)]=="x" or \
        numbers[(0,0)]==numbers[(213,0)]==numbers[(426,0)]=="x" or \
        numbers[(0,213)]==numbers[(426,213)]==numbers[(213,213)]=="x" or \
        numbers[(0,426)]==numbers[(213,426)]==numbers[(426,426)]=="x" or \
        numbers[(0,0)]==numbers[(0,213)]==numbers[(0,426)]=="x" or \
        numbers[(213,0)]==numbers[(213,213)]==numbers[(213,426)]=="x" or \
        numbers[(426,0)]==numbers[(426,213)]==numbers[(426,426)]=="x" or \
        numbers[(426,0)]==numbers[(213,213)]==numbers[(0,426)]=="x":
            show_text('X has won!',213,213,(255,0,0))
            pygame.display.update()
            return 1
        if numbers[(0,0)]==numbers[(213,213)]==numbers[(426,426)]=="o" or \
        numbers[(0,0)]==numbers[(213,0)]==numbers[(426,0)]=="o" or \
        numbers[(0,213)]==numbers[(426,213)]==numbers[(213,213)]=="o" or \
        numbers[(0,426)]==numbers[(213,426)]==numbers[(426,426)]=="o" or \
        numbers[(0,0)]==numbers[(0,213)]==numbers[(0,426)]=="o" or \
        numbers[(213,0)]==numbers[(213,213)]==numbers[(213,426)]=="o" or \
        numbers[(426,0)]==numbers[(426,213)]==numbers[(426,426)]=="o" or \
        numbers[(426,0)]==numbers[(213,213)]==numbers[(0,426)]=="o":
            show_text('O has won!',213,213,(255,0,0))
            pygame.display.update()
            return 1
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x=event.pos[0]-event.pos[0]%213
                y=event.pos[1]-event.pos[1]%213
                coordinates=(x,y)          
                #numbers, coordinates,x or o
                if numbers[coordinates]=="": 
                    if counter%2==1:
                        circleo(coordinates)
                        numbers[coordinates]="o"
                    else:
                        crossx(coordinates)
                        numbers[coordinates]="x"
                    counter=counter+1
                if "" not in numbers.values():
                    show_text("It is a tie!",213,213,(255,0,0))
                    pygame.display.update()
                    time.sleep(2)
                    return
                if win()==1:
                    time.sleep(1)
                    return
        
