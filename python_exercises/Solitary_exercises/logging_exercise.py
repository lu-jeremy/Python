import logging
import sys

logging.basicConfig(level = logging.DEBUG)
logger = logging.getLogger(__name__)

while True:
    try:
        add = lambda x, y: x + y
        x = int(input('Give me a number. \n'))
        y = int(input('Give me another number. \n'))
        result = add(x, y)
        print('Final result: {}'.format(result))
        
    except ValueError:
        logging.error('The number has to be an integer.')
