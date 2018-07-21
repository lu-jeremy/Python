import pygame, sys
from pygame.locals import *
import random




# inheiriting the pygame.sprite.Sprite 
class Invaders(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.time_stamp = random.randint(0,20)
        self.ix = x
        self.iy = y
        #initiating pygame.sprite class
        super().__init__()
        self.speedchangex = 5
        self.bullet_list = []
        self.invader = pygame.sprite.Sprite()
        #convert: creates it line by line; faster
        self.invader.image = pygame.image.load("space invader.png").convert()
        
        self.invader.image = pygame.transform.scale(self.invader.image,(50,50))
        self.invader.image.set_colorkey((0,0,0))
        self.rect = self.invader.image.get_rect()

        
        pygame.time.Clock()
    def updateI(self):
            
        # double slash makes the get_ticks into integer value
        delay = pygame.time.get_ticks()//1000
        # whenever delay gets to ten, reset it to 0
        if delay%10 == self.time_stamp:
            self.time_stamp = random.randint(0,7)
            bullet = Bullet(self.ix,self.iy,'bullet.png')
            self.bullet_list.append(bullet)
        for i in self.bullet_list:
            i.updateB_I()
           
        screen.blit(self.invader.image,(self.ix, self.iy))
        self.ix = self.ix + self.speedchangex
        if self.ix > 590:
            self.speedchangex = -(self.speedchangex)
            self.iy += 40
        if self.ix < 0:
            self.speedchangex = -(self.speedchangex)
            self.iy += 40
        self.rect.x = self.ix
        self.rect.y = self.iy


        
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,bullet_image):
        super().__init__()
        self.x = x
        self.y = y
        self.bullet = pygame.sprite.Sprite()
        
        self.bullet.image = pygame.image.load(bullet_image).convert()
        
        self.bullet.image = pygame.transform.scale(self.bullet.image, (20,20))
        
        self.rect = self.bullet.image.get_rect()
        
     
        
        self.is_alive = True
        
    def updateB_S(self):
        screen.blit(self.bullet.image,(self.x, self.y))
        pygame.mixer.music.load('shoot.wav')
        pygame.mixer.music.play(0)
        self.y -= 30

        if self.y < 0:
            self.is_alive = False
        self.rect.x = self.x
        self.rect.y = self.y
    def updateB_I(self):
        
        screen.blit(self.bullet.image,(self.x, self.y))
        self.y += 4

        if self.y > 640:
            self.is_alive = False
        self.rect.x = self.x
        self.rect.y = self.y
    def updateB_M(self):
        screen.blit(self.bullet.image,(self.x, self.y))
        self.y += 20
        if self.y > 640:
            self.is_alive = False
        self.rect.x = self.x
        self.rect.y = self.y        
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #creating bullet list that stores the bullet numbers
        self.bullet_list = []
        self.sx = 20
        self.health = 5
        self.speedx = 10
        self.character = pygame.sprite.Sprite()
        self.character.image = pygame.image.load('ship2.png').convert()
        
        self.character.image = pygame.transform.scale(self.character.image, (100,20))
        self.character.image.set_colorkey((0,0,0))
        self.rect = self.character.image.get_rect()
        
    def updateS(self):
        for i in self.bullet_list:
            i.updateB_S()
            #if bullet goes out of screen, then remove it from the list
            if i.is_alive == False:
                self.bullet_list.remove(i)
        screen.blit(self.character.image,(self.sx,530))
        self.rect.x = self.sx
        self.rect.y = 530
class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.surface = pygame.Surface((10,10))
        # store draw rect into rect
        self.rect = pygame.draw.rect(self.surface,(0,255,0),(0,0, 10,10 ))
    def update(self):
        screen.blit(self.surface,(self.x,self.y))
        self.rect.x = self.x
        self.rect.y = self.y
class Blocker:
    #create x and y externally 
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #looking at it like this makes it easier to understand
        self.shape_list = [[0,1,1,1,1,1,0],
                           [1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1],
                           [1,1,1,1,1,1,1]]
        self.block_list = []
        for n in range(6):
            for m in range(7):
                """
0 1
0 2
0 3
0 4
0 5
1 0
1 1
1 2
1 3
1 4
1 5
2 0
2 1
2 2
2 3
2 4
2 5
3 0
3 1
3 2
3 3
3 4
3 5

n is one of the four lists inside the large list, while m goes through the elements in that list;
goes through every single element in those lists and check to see if they are 1 (if statement);
if they are 1, then creates a block that has the coordinates going by 10 (so essentially the blocks are next to each other
until they go to the next row, aka when n increases by 1 
"""
                
                if self.shape_list[n][m] == 1:
                    # adds x and y to m/n *10
                    b_L = Block(x+m*10,y+n*10)
                    #appends to list
                    self.block_list.append(b_L)
    def update2(self):
        #goes through list and puts them on screen
        for var in self.block_list:
            #update each block, or else bullet cannot come in contact with block rect
            var.update()
class Mystery(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.x = x
        self.y = y
        self.speedchangex = 0.25
        self.bullet_list = []
        self.solo = []
        self.exclusive = pygame.sprite.Sprite()
        self.exclusive.image = pygame.image.load("mystery_invader.png").convert()
        self.exclusive.image = pygame.transform.scale(self.exclusive.image,(70,70))
        self.rect = self.exclusive.image.get_rect()
        pygame.time.Clock()
    def update(self):
        self.x += self.speedchangex
        if self.x > 590:
            self.speedchangex = -(self.speedchangex)
        if self.x < 0:
            self.speedchangex = -(self.speedchangex)
        screen.blit(self.exclusive.image,(self.x,self.y))
        b = Bullet(self.x,self.y,'bullet.png')
        self.bullet_list.append(b)
        for var in self.bullet_list:
            var.updateB_M()
pygame.init()
screen = pygame.display.set_mode((640,640))

pygame.display.set_caption("Space Invaders")


def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj= fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))

invader_list = []
for y in range(0,300,100):
    for x in range(0,640,80):   
        i = Invaders(x,y)
        invader_list.append(i)
s = Ship()


blocker_list = []
for x in range(30, 600, 170):
    blocker = Blocker(x,450)
    blocker_list.append(blocker)

count = 0
#object is created over and over if creation is in while loop
m = Mystery(320,0) 
m.solo.append(m)
while (1):
    screen.fill((0,0,0))

    
    if s.health ==2:
        s.character.image = pygame.image.load('ship.png').convert()
        s.character.image = pygame.transform.scale(s.character.image, (100,20))
    elif s.health == 1:
        s.character.image = pygame.image.load('ship1.png').convert()
        s.character.image = pygame.transform.scale(s.character.image, (100,20))

        
    if s.health == 0 or len(invader_list) == 0:
        show_text('Game Over.', 280,280, (255,255,255))
        pygame.display.update()
        pygame.mixer.music.load('explosion.wav')
        pygame.mixer.music.play(0)
        break


        
    for i in invader_list:
        i.updateI()
        
# mystery bullet and ship
    for bullet in m.bullet_list:
        if s.rect.colliderect(bullet.rect):
            m.bullet_list.remove(bullet)
            s.health -= 1
            
            
#invader and block
    for invader in invader_list:
        for blocker in blocker_list:
            for block in blocker.block_list:
                if block.rect.colliderect(invader.rect):
                    m.update()
                    pygame.mixer.music.load('ufo_highpitch.wav')
                    pygame.mixer.music.play(0)
# ship bullet and mystery invader
    for bullet in s.bullet_list:
        for mystery in m.solo:
            if mystery.rect.colliderect(bullet.rect):
                print(m.solo)
                m.solo.remove(mystery)
                s.bullet_list.remove(bullet)

    
#invader and ship bullet
    # going through invaders in the invader list
    for invader in invader_list:
        # checking for every single bullet on screen
        for bullet in s.bullet_list:
            # if any bullet hits the invader 
            if invader.rect.colliderect(bullet.rect):
                # then remove them from the list
                s.bullet_list.remove(bullet)
                invader_list.remove(invader)
                pygame.mixer.music.load('invaderkilled.wav')
                pygame.mixer.music.play(0)
            # if bullets is colliding with the invader, remove both the objects
            # from the screen

            
    s.updateS()

    
    # same thing for invaders; goes through list and updates every single blocker in list
    for blockers in blocker_list:
        blockers.update2()


        
#ship bullets and blocker
    # goes through blocker list and gets each blocker
    for blocker in blocker_list:
        # goes through individual blocks in block list
        for block in blocker.block_list:
            # going through bullets in bullet list
            for bullet in s.bullet_list:
                # if each block collides with any bullet
                if block.rect.colliderect(bullet.rect):
                    #then simply remove from list
                    blocker.block_list.remove(block)
                    s.bullet_list.remove(bullet)

                    
#invader bullet and ship
    for invader in invader_list:
        for invader_bullet in invader.bullet_list:
            if s.rect.colliderect(invader_bullet.rect):
                invader.bullet_list.remove(invader_bullet)
                s.health -= 1
                print(s.health)

                
#invader bullet and ship bullet
    for invader in invader_list:
        for invader_bullet in invader.bullet_list:
            for bullet in s.bullet_list:
                if invader_bullet.rect.colliderect(bullet.rect):
                    invader.bullet_list.remove(invader_bullet)
                    s.bullet_list.remove(bullet)


                    


                        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_l]:
        s.sx += s.speedx
    if keys[pygame.K_j]:
        s.sx -= s.speedx

        
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:               
            if event.key==K_SPACE:
                b = Bullet(s.sx+40,530,'greenbullet.png')
                b.updateB_S()
                #appends bullet into list
                s.bullet_list.append(b)
                
    pygame.display.update()



