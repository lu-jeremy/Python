import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()
camlist = pygame.camera.list_cameras()
if camlist:
    cam = pygame.camera.Camera(camlist[0],(640,480))
cam.set_controls(hflip = True, vflip = False)
print(camera.get_controls())
