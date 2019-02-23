import sys
import logging
import random
import time
import math
import logging



logging.basicConfig(filename = 'problems.log', level = logging.INFO)
logger = logging.getLogger(__name__)

##logger.info('Example {}, Example {}'.format(1, 2))



class findVector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def findDirection(self):
        theta = math.degrees(math.atan((self.y2-self.y1) /(self.x2-self.x1)))
        print('This is the angle of the vector:', 
              theta)
    def findMagnitude(self):
        distance = math.sqrt(((self.x2-self.x1)**2) + ((self.y2-self.y1)**2))
        print('This is the distance of the vector:', 
              distance)
