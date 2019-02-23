
#win
import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((640,640))
screen.fill((255,255,255))
numbers= {1:"",2:"",3:"",4:"",5:"",6:"",7:"",8:"",9:""}
counter=0
x=0
y=0
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
            if counter%2==1:
                circleo(coordinates)
            else:
                crossx(coordinates)
            counter=counter+1

        
