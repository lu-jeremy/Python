
#Exercise 1-3
for loop_var in range(0,101,1):
    print("Jeremy",loop_var)
    
for loop_var in range(0,21,1):
    if loop_var%2==0:
        print("Even",loop_var)
    if loop_var%2==1:
        print("Odd",loop_var)
#Exercise4
import time
print("Where should I start from?")
number=int(input())
for loop_var in range(number,0,-1):
    print(loop_var)
    time.sleep(1)
print("BLAST OFF!")

#Exercise 5-6
print("Give me a number.")
number=int(input())
for loop_var in range(1,12,1):
    print(number,"x",loop_var,"=",number*loop_var)
    

#Exercise 7
for loop_var in range(1,5,1):
    print()
    for loop_Var in range(0,5,1):
        print('*',end='')

#Exercise 9:       
count=0
while count<50:
    print(count)
    count +=1

count=-120
while count<120:
    print(count)
    count +=1

count=20
while count>=0:
    print(count)
    count=count-1
count=1
while count<=35:
    print(count)
    count=count+1

count=-17
while count<=25:
    print(count)
    count=count+1
count=24
while count>=8:
    print(count)
    count=count-1

#exercise 11
print("Give me a store price.")
number=int(input())
if number<=10:
    print(number-0.1*number,"this is the discounted price.")
elif number>10:
    print(number-0.2*number,"this is the discounted price.")
else:
    print("This is invalid.")

#exercise 10


#Exercise 8
def main(symbol,number):
    for x in range(0,4,1):
        s=''
    for y in range(x+1):
            s +=symbol
            print(s)
main("*",4)
#exercise 12
print("Give me your age and grade.")
age=int(input())
grade=int(input())
if 3<grade and 8<age:
    print("You are eligible to play the game.")
else:
    print("You are not eligible to play the game.")
#Exercise 13
print("Give me your state that you live in.")
state=input()
if state=="California" or state=="Oregon" or state=="Washington":
    print("We suggest you go for a coastal dive.")
else:
    print("You may be better of skiing.")

#Exercise 14
print("Do you have an upcoming vacation?")
answer=input()
if answer=="yes":
    print("What is your grade?")
    grade=int(input())
    if not(grade==12):
        print("Have an adventurous vacation.")
    else:
        print("Great time to study for SAT.")
else:
    print("That's too bad.")

#Exercise 15
for loop_var in range(0,102,2):
    print(loop_var)

#Exercise 16
for numbers in range(100,-2,-3):
    if numbers>20 and numbers<30:
        print("Tick Tock.")
    else:
        print(numbers)

#Exercise 17
count=4
import time
while count>=1:
    time.sleep (1)
    print(count)
    count=count-1
print("Blast off!")

#Exercise 18
for rectangles in range(0,3,1):
    print()
    for stars in range(0,3,1):
        print()
        for row in range(0,7,1):
            print('*',end='')
        
#Exercise 18 cont.
import random
number=random.randint(1,10)

import random
var=random.uniform(0,1)
print(var)

#Exercise 19
import time
import random
integer=random.randint(0,100000)
print(integer)
time.sleep (3)
decimal=random.uniform(0,1000000)
print(decimal)

#Exercise 20
import random
for integer in range(0,20,1):
    integer=int(random.randint(0,10000))
    print(integer)
print("mean:",integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer+integer/20)
#Exercise 21
import random
for rando_integer in range(-20,20,1):
    rando_integer=int(random.randint(0,100000))
    print(rando_integer)
print("The total of the positive numbers is:",)
