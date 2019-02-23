import random
"""
#Exercise 1
Something = ["C", "A", "T", "S"]
dog = ["D", "O", "N","E"]
chicken = ["B", "I", "R", "D"]
everything = [Something, dog, chicken]
print(everything[1][2],everything[1][0])

#2
elements=("sun", "sun","water", "sky")
print(elements)
print(elements.count("sun"))
print(elements.index("sky"))

#3
import random
count=0
integerrand=random.randint(20,30)
number=0
while number!=integerrand:
    print("Give me the random number I put from 20-30.")
    number=int(input())
    count=count+1
    if number==integerrand:
        print("Good job, you have guessed the correct number.")
        print("Amount of tries",count)
      

#4,5,6,7
variable = {"Bob" : 2170280891, "Bobby" : 1273817892, "Robert" : 2178932776, "Bobbert": 3489038423, "Bobbyrert" : 72498729843}
print(variable["Bob"])
print(variable.keys())
print(variable.values())
for key in variable:
    print(key,variable[key])
#add a key and value
variable["Robby"]=3274987890
print(variable)
#get rid of key and value
variable.pop("Bob")
print(variable)
#8,9
items = {"Flashlight" : "$15", "IPhone" : "$300", "Clothes": "$20", "Pencil": "$0.50", "Mechanical Pencil": "$15"}
print(items.keys())
print("Pick one item from thee 5 of your choice.")
choice=input()
if choice in items:
    print(items[choice])
else:
    print("Please look elsewhere for that item.")

#10, 11
family = {"Mom": "46327", "Dad": "7430", "Sister": "47839", "Jeremy":"631"}
print("Please enter a username.")
username=input()
if username in family:
    print("The account found. Please enter password.")
    password=input()
    if password==family[username]:
        print("Access granted.")
    else:
        print("Access denied.")
else:
    print("No account found if the username is not present in the list.")

#repeat of mini game:hangman
count=0
listofwords = ["Chicken", "Pencil", "Pie", "Rhinoceros"]
randomchoice=random.choice(listofwords)
randomchoiceintolist=list(randomchoice)
underscores=["_"]*len(randomchoiceintolist)
print("Give me a letter. We are playing hangman. Make sure the first letter of the word is capitalized.")
print(underscores)
while "_" in underscores and count<3:
    letterinput=input()
    if letterinput in randomchoiceintolist:
         for variable in range(len(randomchoiceintolist)):
             if randomchoiceintolist[variable]==letterinput:
                 underscores[variable]=randomchoiceintolist[variable]                
    else:
        print("Try again.")
        count=count+1
        if count==3:
            print("I'm sorry, you do not have any more tries.")
    print(underscores)
if "_" not in underscores:
    print("Congratulations.")
"""


