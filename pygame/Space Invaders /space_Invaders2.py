import pygame
import sys
from pygame.locals import *
import logging
import random
import time
"""
Notes:

Triple quote string actually was
not meant to be for comments

Control + 3 = Comment out region (IDLE ide only)
Control + 4 = vice versa (Same)
"""

#Starting up pygame
pygame.init()
#Set up font
pygame.font.init()

#Setting screen to the values in the tuple
screen = pygame.display.set_mode((1200,660))

#Set title of screen
pygame.display.set_caption('Space Invaders')

#Setting up logger

logging.basicConfig(filename = 'problems.log',
                    level = logging.INFO)
                    

logger = logging.getLogger(__name__)


#formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

#Classes:

    #Ship
class Ship:
    def __init__(self):
        self.health = 20
        self.x = 150
        self.y = 600
        self.speed_x = 18
        self.bullet_list = []
        #ship.png
        self.ship_image = pygame.image.load('ship.png').convert()
        self.ship_image = pygame.transform.scale(self.ship_image,(70,70))
        self.rect = self.ship_image.get_rect()
    def update(self):
        for i in self.bullet_list:
            i.ship_bullet()
            if i.y < 0:
                self.bullet_list.remove(i)
        screen.blit(self.ship_image, (self.x, 600))
        self.rect.x = self.x
        self.rect.y = 600

        
    #Invader(s)
class Invader:
    def __init__(self, x, y, image_preference):
        self.time_stamp = random.randint(0,20)
        self.x = x
        self.y = y
        self.speed_x = 2
        self.invader_image = pygame.image.load(image_preference).convert()
        self.invader_image = pygame.transform.scale(self.invader_image, (30, 30))
        self.bullet_list = []
        self.rect = self.invader_image.get_rect()
        pygame.time.Clock()
    def update(self):
        delay = pygame.time.get_ticks()//1000
        if delay%10 == self.time_stamp:
            self.time_stamp = random.randint(0,7)
            bullet = Bullets(self.x,self.y,'bullet.png')
            self.bullet_list.append(bullet)
        for i in self.bullet_list:
            i.invader_bullet()
        screen.blit(self.invader_image, (self.x, self.y))
        self.x += self.speed_x
        if self.x > 1000:
            self.speed_x = -(self.speed_x)
            self.y += 35
        if self.x < 0:
            self.speed_x = -(self.speed_x)
            self.y += 35
        self.rect.x = self.x
        self.rect.y = self.y

    #Bullets
class Bullets:
    def __init__(self, x, y, image_preference):
        self.x = x
        self.y = y
        self.bullet_image = pygame.image.load(image_preference).convert()
        self.bullet_image = pygame.transform.scale(self.bullet_image, (20,20))
        self.rect = self.bullet_image.get_rect()
    def ship_bullet(self):
        screen.blit(self.bullet_image, (self.x, self.y))
        sound = pygame.mixer.Sound('shoot.wav')
        sound.set_volume(0.05)
        sound.play()
        sound.fadeout(1000)
        self.y -= 45
        
        self.rect.x = self.x
        self.rect.y = self.y
    def invader_bullet(self):
        screen.blit(self.bullet_image,(self.x, self.y))
        self.y += 4

        if self.y > 640:
            self.is_alive = False
        self.rect.x = self.x
        self.rect.y = self.y        
    #Blocks
class Blocks:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.surface = pygame.Surface((7,7))
        self.rect = pygame.draw.rect(self.surface, (60, 179, 113), (0, 0, 7, 7))         
    def update(self):
        screen.blit(self.surface,(self.x,self.y))
        self.rect.x = self.x
        self.rect.y = self.y
    #Blockers
class Blocker:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.shape_list = [[0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                           [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,0,0,0,1,1,1,1,1,1],
                           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
                           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1],
                           [1,1,1,1,1,0,0,0,0,0,1,1,1,1,1]]
        self.block_list = []
        for m in range(15):
            for n in range(6):
                if self.shape_list[n][m] == 1:
                    b = Blocks(x+m*7, y+n*7)
                    self.block_list.append(b)
    def update(self):
        for var in self.block_list:
            var.update()
    

#Intro Screen
def game_Intro():
    background = pygame.image.load('Menu.png').convert()
    background = pygame.transform.scale(background, (640, 640))
    while True:
        screen.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                game_Loop()
        pygame.display.update()
                
#Game Loop
def game_Loop():
    score = 0
    
    #Variables & Functions
    invader_list = [[],[],[],[],[],[]]
    blocker_list = []
    myfont = pygame.font.SysFont('Comic Sans MS', 30)


    #Creating Objects:
        #Ship      
    s = Ship()
        #Invaders
    for x in range(80, 1000, 60):
        for y in range(30, 100, 70):
            #2
            i = Invader(x, y, 'invader2.png')
            invader_list[0].append(i)
        for y in range(95, 165, 70):
            #4
            i = Invader(x, y , 'invader4.png')
            invader_list[1].append(i)
        for y in range(160, 230, 70):
            i = Invader(x, y , 'invader1.png')
            invader_list[2].append(i)
        for y in range(225, 295, 70):
            i = Invader(x, y , 'invader5.png')
            invader_list[3].append(i)
        for y in range(290, 360, 70):
            i = Invader(x, y , 'invader3.png')
            invader_list[4].append(i)
        for y in range(355, 425, 70):
            i = Invader(x, y , 'invader6.png')
            invader_list[5].append(i)
        #Blockers
    for x in range(30, 1170, 170):
        blocker = Blocker(x,450)
        blocker_list.append(blocker)
    s.health = 20
    while (1):
        pygame.display.update()
        screen.fill((0,0,0))

        #Game Over / Win
        if s.health == 0:
            break

        if (len(invader_list[0]) == 0 and len(invader_list[1]) == 0 and 
            len(invader_list[2]) == 0 and len(invader_list[3]) == 0 and
            len(invader_list[4]) == 0 and len(invader_list[5]) == 0):
            pygame.quit()
            sys.exit()

        #Updates
        s.update()
        for n in range(5):
            for invader in invader_list[n]:
                invader.update()
        for blockers in blocker_list:
            blockers.update()

        #Collisions
            #Ship's bullets and invaders
        for bullet in s.bullet_list:
            for invader in invader_list[0]:
                if bullet.rect.colliderect(invader.rect):
                    if bullet not in s.bullet_list:
                        continue
                    invader_list[0].remove(invader)
                    pygame.mixer.music.load('invaderkilled.wav')
                    pygame.mixer.music.play(0)
                    s.bullet_list.remove(bullet)
                    score += 30
            for invader in invader_list[1]:
                if bullet.rect.colliderect(invader.rect):
                    if bullet not in s.bullet_list:
                        continue
                    invader_list[1].remove(invader)
                    sound1 = pygame.mixer.Sound('invaderkilled.wav')
                    sound1.set_volume(0.1)
                    sound1.play()
                    sound1.fadeout(1000)
                    s.bullet_list.remove(bullet)
                    score += 30
            for invader in invader_list[2]:
                if bullet.rect.colliderect(invader.rect):
                    if bullet not in s.bullet_list:
                        continue
                    invader_list[2].remove(invader)
                    sound1 = pygame.mixer.Sound('invaderkilled.wav')
                    sound1.set_volume(0.1)
                    sound1.play()
                    sound1.fadeout(1000)
                    s.bullet_list.remove(bullet)
                    score += 20
            for invader in invader_list[3]:
                if bullet.rect.colliderect(invader.rect):
                    if bullet not in s.bullet_list:
                        continue
                    invader_list[3].remove(invader)
                    sound1 = pygame.mixer.Sound('invaderkilled.wav')
                    sound1.set_volume(0.1)
                    sound1.play()
                    sound1.fadeout(1000)
                    s.bullet_list.remove(bullet)
                    score += 20
            for invader in invader_list[4]:
                if bullet.rect.colliderect(invader.rect):
                    if bullet not in s.bullet_list:
                        continue
                    invader_list[4].remove(invader)
                    sound1 = pygame.mixer.Sound('invaderkilled.wav')
                    sound1.set_volume(0.1)
                    sound1.play()
                    sound1.fadeout(1000)
                    s.bullet_list.remove(bullet)
                    score += 10
            for invader in invader_list[5]:
                
                if bullet.rect.colliderect(invader.rect):
                    if bullet not in s.bullet_list:
                        continue
                    invader_list[5].remove(invader)
                    sound1 = pygame.mixer.Sound('invaderkilled.wav')
                    sound1.set_volume(0.1)
                    sound1.play()
                    sound1.fadeout(1000)
                    s.bullet_list.remove(bullet)
                    score += 10
        for blockers in blocker_list:
            for block in blockers.block_list:
                for bullet in s.bullet_list:
                    if bullet.rect.colliderect(block.rect):
                        if block not in blockers.block_list:
                            continue
                        blockers.block_list.remove(block)
                        s.bullet_list.remove(bullet)
            #Invader bullets and ship
        for invader in invader_list:
            for invader_bullet in invader[0].bullet_list:
                if s.rect.colliderect(invader_bullet.rect):
                    invader[0].bullet_list.remove(invader_bullet)
                    s.health -= 1
      
            for invader_bullet in invader[1].bullet_list:
                if s.rect.colliderect(invader_bullet.rect):
                    invader[1].bullet_list.remove(invader_bullet)
                    s.health -= 1
       
            for invader_bullet in invader[2].bullet_list:
                if s.rect.colliderect(invader_bullet.rect):
                    invader[2].bullet_list.remove(invader_bullet)
                    s.health -= 1
                    
            for invader_bullet in invader[3].bullet_list:
                if s.rect.colliderect(invader_bullet.rect):
                    invader[3].bullet_list.remove(invader_bullet)
                    s.health -= 1
      
            for invader_bullet in invader[4].bullet_list:
                if s.rect.colliderect(invader_bullet.rect):
                    invader[4].bullet_list.remove(invader_bullet)
                    s.health -= 1
         
            for invader_bullet in invader[5].bullet_list:
                if s.rect.colliderect(invader_bullet.rect):
                    invader[5].bullet_list.remove(invader_bullet)
                    s.health -= 1
 
        #Ship "Control" keys
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            s.x += s.speed_x
        if keys[pygame.K_LEFT]:
            s.x -= s.speed_x
            
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                b = Bullets(s.x+25, s.y, 'greenbullet.png')
                b.ship_bullet()
                s.bullet_list.append(b)
        textsurface = myfont.render('Score: %s'%score, False, (255, 255, 255))
        screen.blit(textsurface, (0,0))

#Calling home screen & game loop
game_Intro()
              


