"""

#Exercise 1
friends = ["Winston", "Jason", "Arnav", "Jacob", "Nash"]
#2
print(len(friends))
#3
print(friends[1])
#4
print(friends[1:4])
#5
friends[4]="Jeremy"
print(friends[4])
#6
friends.insert(2,"olives")
print(friends)
#7
friends.append("watch")
print(friends)
#8
friends.pop(1)
print(friends)
#9
friends.remove("Arnav")
print(friends)
#10
missfriend=friends.pop(0)
print(friends)
print(missfriend)
#11 inputs = [firstinput, secondinput]
friends.sort()
print(friends)
friends.reverse()
print(friends)
#12
variable="Hello how are you string"
varvar=variable.split()
print(varvar)
character="Hello how are you?"
var=(list(character))
print(var)
ghieh="".join(variable)
print(ghieh)

#13, 14, 15
print("Enter the codename:")
firstinput=input()
while firstinput!=" ":
    print(firstinput)
    print("Access denied.")
    print("Enter the codename:")
    secondinput=input()
    while secondinput!=" ":
        print("Access denied.")
        print("Enter the code:")
        inputs = [firstinput, secondinput]
        thirdinput=input()
        if thirdinput!=" ":
            print("Access Denied. You do not have anymore tries.")
        while thirdinput==" ":
            print("Access Granted. Wrong Passwords tried:",inputs)
            thirdinput=input()

#16
import random
numbers = []
for loop_var in range(0,20,1):
   numbers.append(random.randint(1,20))
print(numbers)
print(max(numbers))
print(min(numbers))

#17
import random
cartoon = ["Attack on Titan", "Mickey Mouse", "Dora", "Spongebob"]
for loop_Var in range(1,10,1):
    random.shuffle(cartoon)
print(cartoon[0])
#18
import random
cartoon= ["Spongebob", "Donald Duck", "Mario", "Angry Birds"]
choice= random.choice(cartoon)
print(choice)
sample=random.sample(cartoon,3)
print(sample)

#19
print(list("This will be a list."))

#20
items = ["Light bulb", "Flashlight", "Phone", "Electricity"]
print('h' in items)
print('Phone' not in items)


#21
items = ["Books", "Fan", "Watch", "Clock", "Charger"]
for variable in items:
    print(variable)
"""   
#Mini project
import random
count=0
aword = ["eggs","something", "cats", "fire", "dragon"]
randomword=random.choice(aword)
alist=list(randomword)
empty = ["_"]*len(randomword)
print("Give me a letter, we will play hangman.")
print(empty)
while "_" in empty and count<3:
    letter=input()
    if letter in alist:
         for l in range(len(alist)):
             if alist[l]==letter:
                 empty[l]=letter
    else:
        print("Try again.")
        count=count+1
    if "67"==letter:
        variable=empty.index("_")
        empty[variable]=randomword[variable]
    print(empty)
if count==3:
        print("I'm sorry, you do not have any more tries.")
else:
    print("Congratulations, you've won the game")
    
