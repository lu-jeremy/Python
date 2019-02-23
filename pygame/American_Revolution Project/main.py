import pygame
from pygame.locals import *
import sys
import random
import math

sys.path.insert(0, '/Users/Jeremy/Desktop/Python/sqlite')
from sqlite_test import *

#starting screens
#game over screen
#restart button

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont2 = pygame.font.SysFont('Georgia', 80)
welcome_surface = myfont.render('Welcome to the Boston Tea Party Game !', False, (255, 255, 224))
instructions = myfont.render('How to play the game: ', False, (255, 255, 255))
instructions_two = myfont.render('Arrow keys for movement, click on mouse to stop running, space bar is to carry crates. Click anywhere to start.', False, (0, 0, 0))
createdby = myfont.render('Created by: Jeremy Lu', False, (165, 42, 42))

WINDOW_SIZE = (1280, 640)
CLOCK = pygame.time.Clock()
FPS = 60
WIN_CENTERX = WINDOW_SIZE[0] / 2
WIN_CENTERY = WINDOW_SIZE[1] / 2
SCREEN = pygame.display.set_mode((1280, 640))


class Player:
    def __init__(self):
        self.image_animation = [
        pygame.image.load('one.png').convert_alpha(), 
        pygame.image.load('two.png').convert_alpha(),
        pygame.image.load('three.png').convert_alpha(), 
        pygame.image.load('four.png').convert_alpha(), 
        pygame.image.load('five.png').convert_alpha(),
        pygame.image.load('six.png').convert_alpha()]
        self.image_animation = [pygame.transform.scale(image, (50, 50)) for image in self.image_animation]
        for image in self.image_animation:
            image.set_colorkey((0, 0, 0)) 
        
        self.image_right = self.image_animation
        self.image_left = [pygame.transform.flip(image, True, False) for image in self.image_right]
        self.current_index = 0
        self.current_image = self.image_animation[self.current_index]

        self.p_crate_list = []
        self.direction = pygame.math.Vector2(678, 0)
        self.velocity = 8
        self.fall_velocity = 2
        self.fall = 1

        self.animation_time = 0.1
        self.current_time = 0

        self.rect = self.current_image.get_rect()
    def update_time(self, delta_time): 
        self.current_time += delta_time
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_index = (self.current_index + 1) % 6
            self.current_image = self.image_animation[self.current_index]

        self.rect.move_ip(*self.direction)
    def jump(self):
        self.direction.y -= self.velocity + 7
    def update_image(self, delta_time):
        if self.fall == 1: 
            self.direction.y += self.fall_velocity
        self.update_time(delta_time)
        SCREEN.blit(self.current_image, (self.direction.x, self.direction.y))
        self.rect.x = self.direction.x
        self.rect.y = self.direction.y


class Crate:
    def __init__(self):
        #has platform ranges for the random x value so the crate doesn't just spawn off the ship grounds
        #x values are first two elements of tuples, and last value is y
        self.platform_range = [(0, 100, 530), (330, 500, 458), (580, 790, 480), (830, 1020, 420), (1110, 1240, 530), (970, 1050, 480)] 
        t = random.choice(self.platform_range)
        self.x = random.randint(t[0], t[1])
        self.y = t[2]
        self.crate = pygame.image.load('crate.png').convert_alpha()
        self.crate = pygame.transform.scale(self.crate, (40, 40))
        self.crate.set_colorkey((255, 255, 255))
        self.drop = 0
        self.rect = self.crate.get_rect()
        #do a self.rect.x = self.x and self.rect.y = y in init because it will make sure that the several crates that are spawned
        #have a rect without having to call the update_image() function
        self.rect.x = self.x
        self.rect.y = self.y
    def update_image(self):
        if self.drop == 1:
            self.y += 2
        SCREEN.blit(self.crate, (self.x, self.y))
        self.rect.x = self.x
        self.rect.y = self.y

        
class Game:
    def __init__(self):
        pygame.display.set_caption('The Boston Tea Party Saga ~ 1')
        self.background_one = pygame.image.load('background.png')
        self.background_one = pygame.transform.scale(self.background_one, (1280, 640))
        self.score = 0
        # self.score_database = DataBase('main')
        # self.score_database.createTable('player', columns = ['player_name', 'score'], data_types = ['STRING','INTEGER'])
        # self.score_database.insert('player', values = ['runner', '{}'.format(self.score)])
        self.p = Player()
        self.double_down = 0
        self.instance = 0
        #platforms have begin of x to end of x, how wide is the platform, and then thickness of it
        #put platforms inside list to update
        self.sea = pygame.Rect(0, 590, 1280, 2)
        self.platform1 = pygame.Rect(0, 570, 160, 2)
        self.platform2 = pygame.Rect(310, 498, 209, 2)
        self.platform3 = pygame.Rect(570, 520, 213, 2)
        self.platform4 = pygame.Rect(810, 460, 200, 2)
        self.platform5 = pygame.Rect(1000, 570, 200, 2)
        self.platform6 = pygame.Rect(310, 520, 800, 2)
        self.platforms = [self.platform1, self.platform2, self.platform3, self.platform4, self.platform5, self.platform6]
        self.instance_var = 0 
        #crate list to update
        self.crate_list = []
        #create an initial crate or else overlapping part does not work, checking if 
        #crate is touching another crate, but no crate there 
        self.crate_list.append(Crate())
        # self.overlapping = 0
        for var in range(10):
            self.c = Crate()
            # while self.overlapping != 1:
            #     self.overlapping = 0
            #     for crate in self.crate_list:
            #         if crate.rect.colliderect(self.c.rect):
            #             self.overlapping = 1
            #             print('hi')
            #             self.c = Crate()
            self.crate_list.append(self.c)
    def update_images(self):
        self.p.update_image(self.delta_time)
        #updating crate_list
        for crate in self.crate_list:
            crate.update_image()
        #updating the player crate list in order to remove the crate out of the crate_list
        #in order to prevent it from going back to the top of the player and instead 
        #do the drop function
        for crate in self.p.p_crate_list:
            crate.update_image()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() ; sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.instance_var = 1
                if event.key == K_LEFT:
                    self.instance_var = 2
                if event.key == K_DOWN:
                    self.double_down += 1
                    self.instance_var = 3
                if event.key == K_UP:
                    self.instance_var = 4
                if event.key == K_SPACE:
                    try:
                        #first element of player crate list's attribute is drop since it belongs to 
                        #a crate class
                        self.p.p_crate_list[0].drop = 1

                        #pop() function returns the value that it is popping
                        #therefore put it in a variable and append that to the crate list
                        #while the player crate list doesn't have it anymore, but the 
                        #crate still updates which is good
                        temp_var = self.p.p_crate_list.pop()
                        self.crate_list.append(temp_var)
                    except:
                        continue
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                #printing mouse position in order for ease of coordinates for platform and character positioning
                print(pygame.mouse.get_pos())
                self.instance_var = 0
    def movement(self):
        if self.instance_var == 1:
            self.p.direction.x += self.p.velocity
            self.p.image_animation = self.p.image_right
        #do "and self.p.direction.x >= 8" at the end because self.p.velocity is 8 and might not 
        #reach 0 if I did "and self.p.direciton >= 0"
        #moves the player to the left and prevents it from going negative and falling 
        #because it only executes the code if the direction is greater than or equal to 8
        if self.instance_var == 2 and self.p.direction.x >= 8:
            self.p.direction.x -= self.p.velocity
            self.p.image_animation = self.p.image_left
        if self.instance_var == 3:
            if self.double_down % 2 == 1:
                self.p.fall_velocity = 6
                self.instance_var = 0
            if self.double_down % 2 == 0:
                self.p.fall_velocity = 2
                self.instance_var = 0
        if self.instance_var == 4:
            self.p.jump()
            self.fall = 0
    def start_screen(self):
        while True:
            SCREEN.fill((0, 250, 154))
            SCREEN.blit(welcome_surface, (200, 150))
            SCREEN.blit(instructions, (270, 300))
            SCREEN.blit(instructions_two, (100, 400))
            SCREEN.blit(createdby, (1000, 550))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit; sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.instance == 0:
                        self.game_init()
                    return
            pygame.display.update()
    def game_over(self):
        your_score = myfont2.render('You lost! You\'re final score is: ', False, (0, 0, 0))
        new_score = myfont2.render('{}'.format(self.score), False, (0, 0, 0))
        restart = myfont2.render('Click anywhere to restart.', False, (0, 0, 0))
        while True:
            SCREEN.fill((255, 0, 0))
            SCREEN.blit(your_score, (300, 100))
            SCREEN.blit(new_score, (550, 150))
            SCREEN.blit(restart, (400, 300))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit ; sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    return
            pygame.display.update()
    def game_init(self):
        self.instance = 1
        while True:
            score_board = myfont.render('Score: %s'%self.score, False, (0, 0, 0))
            for crate in self.crate_list:
                for crate_2 in self.p.p_crate_list:
                    if crate.rect.bottom in range(self.sea.bottom, self.sea.bottom + 5) and crate.x in range(self.sea.x, self.sea.x + self.sea.width):
                        self.score += 1
                        print(self.score)  
                    if crate_2.rect.bottom in range(self.sea.bottom, self.sea.bottom + 5) and crate_2.x in range(self.sea.x, self.sea.x + self.sea.width):
                        self.score += 1
                        print(self.score)
            if self.p.rect.bottom in range(self.sea.bottom, self.sea.bottom + 5) and self.p.direction.x in range(self.sea.x, self.sea.x + self.sea.width):
                self.game_over()
                self.start_screen()
                self.score = 0
                self.p.direction.x = 678
                self.p.direction.y = 0
            #updating platform
            for platform in self.platforms:
                #if the bottom of the player's rect is in the range of the platform's bottom and 
                #if the player's x is between the platform's x coordinates then fall = 0
                #when fall = 0, then go to then refer to update_image() in player class
                if self.p.rect.bottom in range(platform.bottom, platform.bottom + 5) and self.p.direction.x in range(platform.x, platform.x + platform.width):
                    self.p.fall = 0    
                    break
                self.p.fall = 1
                #if the length of the player crate list is 0 and there is no crate drop then 
                #put the crate on top of the player's head
                #then append it to the player list and remove it from the original crate list
                #this makes it so that player can only carry one crate at a time
            for crate in self.crate_list:
                if crate.rect.colliderect(self.p.rect) and len(self.p.p_crate_list) == 0 and crate.drop == 0:
                    crate.x = self.p.direction.x
                    crate.y = self.p.direction.y - 30
                    self.p.p_crate_list.append(crate)
                    self.crate_list.remove(crate)
            #makes it so that the crate stays on top of head even when the crate is in player
            #crate list
            for crate in self.p.p_crate_list:
                crate.x = self.p.direction.x
                crate.y = self.p.direction.y - 30
            SCREEN.blit(self.background_one, (0, 0))
            self.delta_time = CLOCK.tick(FPS) / 1000
            SCREEN.blit(score_board, (0,0))
            self.update_images()
            self.handle_events()
            self.movement()
            pygame.display.flip()

if __name__ == '__main__':
    Game().start_screen()
