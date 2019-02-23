import math
import sys
import pygame
import logging
import pygame.event

pygame.init()

pygame.font.init()

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption('')

logging.basicConfig(level = logging.DEBUG)

WINDOWWIDTH = 640

WINDOWHEIGHT = 480

WIN_CENTERX = int(WINDOWWIDTH / 2)

WIN_CENTERY = int(WINDOWHEIGHT / 2)


AMPLITUDE = 100

# standard pygame setup code
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Trig Bounce')

step = 0

while True:
    
    pygame.display.update()
    screen.fill((0,0,0))

    # fill the screen to draw from a blank state

    # draw waving ball
    yPos = -1 * math.sin(step) * AMPLITUDE
    pygame.draw.circle(DISPLAYSURF, (0,0,255), (int(WINDOWWIDTH * 0.333), int(yPos) + WIN_CENTERY), 40)

    # draw waving ball
    yPos = -1 * abs(math.sin(step)) * AMPLITUDE
    pygame.draw.circle(DISPLAYSURF, (255,0,0), (int(WINDOWWIDTH * 0.666), int(yPos) + WIN_CENTERY), 40)


    # draw the border
    pygame.draw.rect(DISPLAYSURF, (0,0,0), (0, 0, WINDOWWIDTH, WINDOWHEIGHT), 1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()


    step += 0.02
    step %= 2 * math.pi
