import pygame
from pygame.locals import*
import random
screen=pygame.display.set_mode((640,480))
pygame.init()
foodx=random.randint(0,640)
foody=random.randint(0,640)
snakex=random.randint(0,640)
snakey=random.randint(0,640)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen, (255,0,0), (foodx, foody, 10, 10))
    pygame.draw.rect(screen, (0,255,0), (snakex, snakey, 10, 10))
    
