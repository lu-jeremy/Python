import random
import time
import turtle
#Exercise 1
"""
#2
def mean(n1,n2,n3,n4):
    print((n1+n2+n3+n4)/4)
mean(57,54,23,4898)
mean(1,2,3,4)
#3

def chicken(something):
    listthing=(list(something))
    listthing.reverse()
    jointhing="".join(listthing)
    print(jointhing)
chicken("thunderleopard")

#4
print("Give me your name, age, address, state")
name=input()
age=input()
address=input()
state=input()
def properties(name,age,address,state):
    print(name,"aged",age,"years lives at",address,",",state)
properties(name,age,address,state)

#6
def total(price,tax):
    thing=price+tax*price/100
    return thing
variable=total(50,1)
print(variable)
"""
"""
#7
def three(a,b,c):
    power=a**(b**c)
    return power
threevariable=three(3,4,6)
print(threevariable)
#8
def quarters(q):
    return q*25
def dimes(d):
    return d*10
def nickels(n):
    return n*5
def pennies(p):
    return p
change=quarters(43)+dimes(20)+nickels(4)+pennies(1238)
print(change)
"""
#9
print("Give me a rectangle, triangle, or circle for the AREA of that shape(no numbers).")
shape=input()
import Shapes 
if shape=="rectangle":
    Shapes.rectangle()
if shape=="triangle":
    Shapes.triangle()
if shape=="circle":
    Shapes.circle()
#10
randomnumbers = []
def numbers():
    for something in range(5):
        anint=random.randint(1,20)
        randomnumbers.append(anint)
    print(randomnumbers)
numbers()
"""
#11
def randdecim():
    while True:
        afloat=random.uniform(1.5,100.5)
        print(afloat)
        time.sleep(3)
randdecim()
"""
#12 
def family(relation,state,city,name):
    print(relation,state,city,name)
family("mother","China","HongKong","Mei")
family("sister","CA","Saratoga","Olivia")
family("brother", "CA","Saratoga","Jeremy")
family("father", "CA", "Saraoga", "Gordon")

"""
#Reference sheet and 2
def header():
    print("This function just prints some text.")
    print("But oiihnrfiwobn")
header()
"""
"""
#rock,paper,scissors
screen=turtle.Screen()
image= r"/Users/Jeremy/Desktop/rocks.gif"
screen.addshape(image)
turtle.shape(image)
threeelement = ["rock","paper", "scissors"]
def index():
    print(threeelement[0])
    time.sleep(1)
    print(threeelement[1])
    time.sleep(1)
    print(threeelement[2],"!!!")
    time.sleep(1)
while True:
    choice=random.choice(threeelement)
    print(choice)
    print("Give me rock, paper, or scissors.")
    oneelement=input()
    index()
    print("Input:",oneelement)
    if oneelement==threeelement[0] and random=="scissors":
        print("You won!")
    if oneelement==threeelement[0] and random=="paper":
        print("You lose!")           
    if oneelement==threeelement[1] and random=="scissors":
        print("You lose!")           
    if oneelement==threeelement[1] and random=="rock":
        print("You won!")           
    if oneelement==threeelement[2] and random =="rock":
        print("You lose!")           
    if oneelement==threeelement[2] and random=="paper":
        print("You win!")
    if oneelement and random==threeelement[2] or oneelement and random==threeelement[1] or oneelement and random==threeelement[0]:
        print("Tie, try again.")
"""
