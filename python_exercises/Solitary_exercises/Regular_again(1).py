import sys
import logging
import random
import time
import math
import logging



logging.basicConfig(filename = 'problems.log', level = logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Example {}, Example {}'.format(1, 2))

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

if __name__ == '__main__':
    findVector(0,0,5,3).findDirection()
    findVector(0,0,5,3).findMagnitude()
        
"""

1. At program start, assume a stock of 10 nickels, 10 dimes, 10 quarters, and 10 pennies.
2. Repeatedly prompt the use for a price in the form xx.xx, where x denotes a digit, or to enter 'q' to quit.

3. When a price is entered:

If the price entered is negative, print an error message and start over requesting
either a new price or to quit (indicitated by entering a 'q')

Prompt for the number of dollars in payment. If the payment is insufficient, print an error message and
reprompt for payment.

Next determine the coins to be dispensed as change. This calculation will depend on the amount to be dispensed and
also on the number of coins left in the stock. For example, the least number of coins needed to make change of 1.30 is 6:
5 quarters and 1 nickel. But if there are only 3 quarters, 3 dimes, and 10 nickels left in the stock, then the least number is 11:
3 quarters, 3 dimes, 5 nickels.

Print the numbers of the coins to be dispensed as change and their denominations. (Omit a denomination if no coins of that
denomination will be dispensed.)

In case exact payment is made, print a message such as "No change".

If the change cannot be made up with the coins remaining, print an error message and halt the program.

4. Just before quitting, print the total amount (the number of dollars and number of cents) left in the stock.
"""



running = None

def setup():
    global price
    global money
    price = input('Give me a price in the form xx.xx, or if you want to quit press \'q\'. \n')
    print(price)
    money = input('Give me the money in the form xx.xx, or if you want to quit press \'q\'. \n')
    print(money)
def conditions():
    if price == 'q' or money == 'q':
        running = False
        sys.exit()
    if float(price) < 0:
        print('Error, the previous number was negative.')
        running = False
        setup()
    if float(money) < float(price):
        print('Error, insufficient price.')
        running = False
        setup()
count = 0
l = [10,10,10,10]
def change():
    global count
    global l
    if count == 0:
        if float(money) == float(price):
            print('No change.')
        change_Var = float(money) - float(price)

        new_quarters = float(change_Var) // 0.25
        var = float(change_Var) - float(new_quarters * 0.25)
        new_dimes = var // 0.1
        new_var = var - float(new_dimes*0.1) 
        new_nickels = new_var // 0.05
        new_pennies = new_var // 0.01
        print('The number of coins: ', new_quarters + new_dimes + new_nickels + new_pennies)
        print('Prices for each coin: ', 'quarters: ', new_quarters, 'dimes: ', new_dimes, 'nickels: ', new_nickels, 'pennies: ', new_pennies)
        l[0] -= new_quarters
        l[1] -= new_dimes
        l[2] -= new_nickels
        l[3] -= new_pennies
        total = (l[0]*0.25) + (l[1]*0.1) + (l[2]*0.05) + (l[3] * 0.01)
        if total < 0:
            print('Sorry, there is not enough money for your transaction in the stock.')
            sys.exit()
        print('This is the total amount of money left in the stock: ', total)
        count = 1
def mainloop():
    setup()
    running = True
    while running:
        conditions()
        change()
        sys.exit()
while True:
    mainloop()
    break



def isBadVersion(version_Num, given, first_Num):
    if first_Num <= version_Num <= given:
        print('True')
        return True
    return False
    print('False')


if __name__ == '__main__':
    given = 5
    first_Num = 4
    isBadVersion(3, given, first_Num)
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9, Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
Given nums = [3, 3], target 6
"""

try:
    class Solution:
        def twoSum(self, nums, target):
           for var in range(0,len(nums),1):
               for s_var in range(0,len(nums),1):
                   if nums[var] + nums[s_var] == target and var != s_var:
                        logger.info('Got through')
                        return var
                        return s_var 
                    
            
            
except ValueError:
    logger.warn('Something\'s not right.')

finally:
    if __name__ == "__main__":
        nums = [8,8,10,12]
        target = 18
        print(Solution().twoSum(nums, target))

def fibonnaci(n):
    l = [0,1]
    count = 2
    while n > count:
        l.append(l[count-2]+l[count-1])
        count += 1
        print(l)
fibonnaci(8)
