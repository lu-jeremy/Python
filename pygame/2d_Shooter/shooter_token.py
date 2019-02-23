import pygame
from pygame.locals import *
import sys
import random
import math

sys.path.insert(0, '/Users/Jeremy/Desktop/Python/sqlite')
from sqlite_test import *
#restart button

WINDOW_SIZE = (640, 600)
CLOCK = pygame.time.Clock()
FPS = 60
WIN_CENTERX = WINDOW_SIZE[0] / 2
WIN_CENTERY = WINDOW_SIZE[1] / 2


# class Clock:
#     def __init__(self, screen):
        
#     def update_image(self, screen):


class FlyingToken:
    def __init__(self):
        self.velocity = 6
        self.xPos = 0
        self.step = 0
        self.AMPLITUDE = 175
        self.flying_token_image = pygame.image.load('flying_token.png').convert_alpha()
        self.flying_token_image = pygame.transform.scale(self.flying_token_image, (80, 40))
        self.flying_token_image.set_colorkey((0,0,0))
        self.rect = self.flying_token_image.get_rect()
    def update_image(self, screen):
        self.yPos = -1 * math.sin(self.step) * self.AMPLITUDE
        screen.blit(self.flying_token_image, ( (int(self.xPos), int(self.yPos + WIN_CENTERY + 60))) )
        self.step += 0.07
        self.step %= 2 * math.pi
        self.xPos += 0.5
        self.rect.x = self.xPos
        self.rect.y = self.yPos + WIN_CENTERY + 60


class Coin:
    def __init__(self):
        self.image_animation = [
            pygame.image.load('money_one.png').convert_alpha(),
            pygame.image.load('money_two.png').convert_alpha(),
            pygame.image.load('money_three.png').convert_alpha(),
            pygame.image.load('money_four.png').convert_alpha(),
            pygame.image.load('money_five.png').convert_alpha()
        ]
        self.image_animation = [pygame.transform.scale(image, (30, 30)) for image in self.image_animation]
        for image in self.image_animation:
            image.set_colorkey((0, 0, 0))
        self.current_index = 0
        self.current_image = self.image_animation[self.current_index]
        
        self.direction = pygame.math.Vector2(random.randint(0, 600), 450)
        self.animation_time = 0.1
        self.current_time = 0

        self.rect = self.current_image.get_rect()

    def update_time(self, delta_time): 
        self.current_time += delta_time
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_index = (self.current_index + 1) % 5
            self.current_image = self.image_animation[self.current_index]

        self.rect.move_ip(*self.direction)
    def update_image(self, screen, delta_time):
        self.update_time(delta_time)
        screen.blit(self.current_image, (self.direction.x, self.direction.y))
        
        self.rect.x = self.direction.x
        self.rect.y = self.direction.y


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

        self.direction = pygame.math.Vector2(20, 450)
        self.velocity = 8

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
    def update_image(self, screen, delta_time):
        self.update_time(delta_time)
        screen.blit(self.current_image, (self.direction.x, self.direction.y))
        
        self.rect.x = self.direction.x
        self.rect.y = self.direction.y


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Shooter : Test Runner')
        self.score = 0
        self.score_database = DataBase('main')
        self.score_database.createTable('player', columns = ['player_name', 'score'], data_types = ['STRING','INTEGER'])
        self.score_database.insert('player', values = ['runner', '{}'.format(self.score)])
        self.screen = pygame.display.set_mode((WINDOW_SIZE[0], WINDOW_SIZE[1]))
        self.extend_left = pygame.image.load('extend_left.jpg')
        self.extend_left = pygame.transform.scale(self.extend_left, (10000, 600))
        self.background_left1 = pygame.image.load('bg_left1.png')
        self.background_left1 = pygame.transform.scale(self.background_left1, (640, 600))
        self.background_left2 = pygame.image.load('bg_left2.png')
        self.background_left2 = pygame.transform.scale(self.background_left2, (640, 600))
        self.background_left3 = pygame.image.load('bg_left3.png')
        self.background_left3 = pygame.transform.scale(self.background_left3, (640, 600))
        self.background_middle1 = pygame.image.load('bg_middle1.png')
        self.background_middle1 = pygame.transform.scale(self.background_middle1, (640, 600))
        self.background_middle2 = pygame.image.load('bg_middle2.png')
        self.background_middle2 = pygame.transform.scale(self.background_middle2, (640, 600))
        self.background_right1 = pygame.image.load('bg_right1.png')
        self.background_right1 = pygame.transform.scale(self.background_right1, (640, 600))
        self.background_right2 = pygame.image.load('bg_right2.png')
        self.background_right2 = pygame.transform.scale(self.background_right2, (640, 600))
        self.background_right3 = pygame.image.load('bg_right3.png')
        self.background_right3 = pygame.transform.scale(self.background_right3, (640, 600))
        self.extend_right = pygame.image.load('extend_right.png')
        self.extend_right = pygame.transform.scale(self.extend_right, (10000, 600))
        self.background_up_middle1 = pygame.image.load('bg_up_middle1.jpg')
        self.background_up_middle1 = pygame.transform.scale(self.background_up_middle1, (10000, 600))
        self.sounds = ['chaching.wav', 'chaching2.wav', 'chaching3.wav']
        self.p = Player()
        self.c = Coin()
        self.f = FlyingToken()
        # self.n = Net()
        self.instance_var = 0
        self.velocity = 4

        self.extend_left_dir_x = -11920
        self.left1_x = -1920
        self.left2_x = -1280
        self.left3_x = -640
        self.middle1_x = 0
        self.middle2_x = 640
        self.right1_x = 1280
        self.right2_x = 1920
        self.right3_x = 2560
        self.extend_right_dir_x = 3200
        self.background_up_middle1_x = -5000

        self.left1_y = 0
        self.left2_y = 0
        self.left3_y = 0
        self.middle1_y = 0
        self.middle2_y = 0
        self.right1_y = 0
        self.right2_y = 0
        self.right3_y = 0
        self.extend_right_dir_y = 0
        self.extend_left_dir_y = 0
        self.background_up_middle1_y = -600
        
    def handling_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit; sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.instance_var = 1
                elif event.key == K_LEFT:
                    self.instance_var = 2
                elif event.key == K_DOWN:
                    self.instance_var = 4
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                self.instance_var = 0
    def update_images(self):
        self.c.update_image(self.screen, self.delta_time)
        self.p.update_image(self.screen, self.delta_time)
        self.f.update_image(self.screen)
        # self.n.update_image(self.screen)
    def collisions(self):
        if self.p.rect.colliderect(self.c.rect):
            self.c.direction.x = random.randint(0, 600)
            sound = pygame.mixer.Sound(self.sounds[random.randint(0, 2)])
            sound.set_volume(0.2)
            sound.play()
            self.score += 1
            self.score_database.update('player', 'score', '{}'.format(self.score) , 'player_name', 'runner')
            self.score_database.readTable('player')
        if self.p.rect.colliderect(self.f.rect):
            self.instance_var = 3
            self.f.xPos = random.randint(40, 400)
    def movement(self):
        if self.instance_var == 1:
            self.p.direction.x += self.p.velocity
            self.p.image_animation = self.p.image_right
        if self.instance_var == 2:
            self.p.direction.x -= self.p.velocity
            self.p.image_animation = self.p.image_left
        if self.instance_var == 3:
            self.p.direction.y -= 5
        if self.instance_var == 4:
            self.p.direction.y += 5
    def movement_right_background(self):
        if self.p.direction.y >= 470:
            self.p.direction.y = 450
            self.instance_var = 0
        if self.p.direction.x >= 590:
            self.right1_x -= 7
            self.right2_x -= 7
            self.right3_x -= 7
            self.middle1_x -= 7
            self.middle2_x -= 7
            self.left1_x -= 7
            self.left2_x -= 7
            self.left3_x -= 7
            self.extend_left_dir_x -= 7
            self.extend_right_dir_x -= 7
            self.c.direction.x -= 7
            self.background_up_middle1_x -= 7
            self.instance_var = 0
        if self.p.direction.x <= 10:
            self.right1_x += 7
            self.right2_x += 7
            self.right3_x += 7
            self.middle1_x += 7
            self.middle2_x += 7
            self.left1_x += 7
            self.left2_x += 7
            self.left3_x += 7
            self.c.direction.x += 7
            self.extend_left_dir_x += 7
            self.extend_right_dir_x += 7
            self.background_up_middle1_x += 7
            self.instance_var = 0
        if self.p.direction.y < 0:
            self.instance_var = 0
            self.c.direction.y += 5
            self.right1_y += 5
            self.right2_y += 5
            self.right3_y += 5
            self.middle1_y += 5
            self.middle2_y += 5
            self.left1_y += 5
            self.left2_y += 5
            self.left3_y += 5
            self.c.direction.y += 5
            self.extend_left_dir_y += 5
            self.extend_right_dir_y += 5
            self.background_up_middle1_y += 5
            if self.background_up_middle1_y == 0:
                self.p.direction.y = 450
    def game_init(self):
        while True:       
            self.screen.blit(self.extend_left, (self.extend_left_dir_x, self.extend_left_dir_y))
            self.screen.blit(self.background_left1, (self.left1_x, self.left1_y))
            self.screen.blit(self.background_left2, (self.left2_x, self.left2_y))
            self.screen.blit(self.background_left3, (self.left3_x, self.left3_y))
            self.screen.blit(self.background_middle1, (self.middle1_x, self.middle1_y))
            self.screen.blit(self.background_middle2, (self.middle2_x, self.middle2_y))
            self.screen.blit(self.background_right1, (self.right1_x, self.right1_y))
            self.screen.blit(self.background_right2, (self.right2_x, self.right2_y))
            self.screen.blit(self.background_right3, (self.right3_x, self.right3_y))
            self.screen.blit(self.extend_right, (self.extend_right_dir_x, self.extend_right_dir_y))
            self.screen.blit(self.background_up_middle1, (self.background_up_middle1_x, self.background_up_middle1_y))
            self.delta_time = CLOCK.tick(FPS) / 1000
            self.movement_right_background()
            self.handling_events()
            self.update_images()
            self.collisions()
            self.movement()
            pygame.display.update()


if __name__ == '__main__':      
    Game().game_init()