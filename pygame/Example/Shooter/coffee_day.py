import pygame
from pygame.locals import *
import sys

pygame.init()

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption('')

homescreen_background = pygame.image.load('homescreen_background.png').convert()
homescreen_background = pygame.transform.scale(homescreen_background, (640, 480))

scene1 = pygame.image.load('scene1.png').convert()
scene1 = pygame.transform.scale(scene1, (640, 480))

scene2 = pygame.image.load('scene2.jpg').convert()
scene2 = pygame.transform.scale(scene2, (640, 480))
class Player:
    def __init__(self):
        self.x = 60
        self.y = 400
        self.speed_x = 8
        self.speed_y = 8
        self.gravity = 8
        self.bullet_list = []
        self.surface = pygame.Surface( (55, 70), pygame.SRCALPHA, 32)
        self.launch_image = pygame.image.load('average_joe.jpg').convert()
        self.launch_image = pygame.transform.scale(self.launch_image,(55,70))
        self.rect = self.launch_image.get_rect()
        self.new_image = self.surface.blit(self.launch_image, (0,0))
    def update(self):
        screen.blit(self.new_image, (self.x, self.y))

        self.rect.x = self.x
        self.rect.y = self.y
        
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.bullet_list = []
        self.bullet_image = pygame.image.load('/Users/Jeremy/Desktop/Python/pygame/Space Invaders/greenbullet.png')
        self.bullet_image = pygame.transform.scale(self.launch_image,(30,30))
        self.rect = self.bullet_image.get_rect()                                            
    def update(self, screen):
        screen.blit(self.bullet_image, (self.x, self.y))
        

class Game:
 #   def home_screen(self):
    def __init__(self):
        self.p = Player()
    def home_screen(self):
        while True:
            pygame.display.update()
            
            screen.blit(homescreen_background, (0,0))
            
            self.p.update()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit(); sys.exit()
##                if event.type == MOUSEMOTION:
##                    (mouse_x, mouse_y) = pygame.mouse.get_pos()
##                    p.x = mouse_x 
##                    p.y = mouse_y
    def game_loop(self):
        while True:
            pygame.display.update()
            
            screen.blit(scene1, (0,0))
            
            
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit(); sys.exit()

                    
if __name__ == '__main__':
    g = Game()
    g.home_screen()
    




    



