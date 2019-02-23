import pygame
from pygame.locals import *
import logging

pygame.init()

logging.basicConfig(level = logging.DEBUG)

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption('Quadratic Game.')

pygame.font.init()

myfont = pygame.font.SysFont('Comic Sans MS', 30)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ball_list = []
        self.surface = pygame.Surface((30,30))
        self.ball = pygame.draw.circle(self.surface, (255, 255, 255), (15,15), 15)
        
    def update(self):
        screen.blit(self.surface, (self.x, self.y))
        self.y = 0.1 * ((self.x-100)**2)
b = Ball(0, 640)
class rowBalls:
    def creatingBalls(self):
        global x, y
        for x in range(37, 164, 1):
            y = 0.1 * ((x-100)**2)
            b.update()
            #logging.debug('made the object')
            #logging.debug('appended the object')
##        for new_x in range(237, 364, 1):
##            new_y = 0.1 * ((new_x - 300)**2)
##            new_b = Ball(new_x, new_y)
##            new_b.ball_list.append(new_b)
##            new_b.update()
##        for new_x in range(437, 564, 1):
##            new_y = 0.1 * ((new_x - 500)**2)
##            new_b = Ball(new_x, new_y)
##            new_b.ball_list.append(new_b)
##            new_b.update()

while True:

    pygame.display.update()
    screen.fill((0, 0, 0))

    rowBalls().creatingBalls()
    
    for event in pygame.event.get():
        if event == QUIT:
            pygame.quit()
            sys.exit()
##        if event.type == pygame.MOUSEBUTTONUP:
##            pos = pygame.mouse.get_pos()
##            for b in b.ball_list:
##                if b.circle.collidepoint(pos):
##                    textsurface = myfont.render('%s'%(pos[0], pos[1]), False, (0, 0, 255))
##                    screen.blit(textsurface, (0,0))
            
