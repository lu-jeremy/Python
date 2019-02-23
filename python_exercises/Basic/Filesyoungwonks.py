import time
import random
"""
#Exercise 1
g="hello will"
print([0], g[1], g[2])
print(g[-1])
print(g[0:3])
print(g[4:7])
print(g[:4])
print(g[4:])
print(g[:])
#2
"Hello"
"Hi"
print("Hello"+"Hi")
print("Hello"*3)
#3
longestwordindictionary="Pneumonoultramicroscopcsilicovolcanoconiosis"
for loop_var in longestwordindictionary:
    print(loop_var,"-",end="")
    
#4
print("Give me your first name and last name in order for us to make you a fresh new username.")
firstname=input()
lastname=input()
print(firstname[0]+lastname)

#5 and 6 and 7
numlist = []
months="JanFebMarAprMayJunJulAugSepOctNovDec"
for loop_var in range(1,13,1):
    stp=(loop_var-1)*3
    enp=stp+3
    chickenpie=months[stp:enp]
    numlist.append(chickenpie)
    print(numlist)

emplist=[]
Myname="Lgtgo{"
for loop_var in Myname:
    numbers=ord(loop_var)
    numbers=numbers-2
    emplist.append(chr(numbers))
    print(emplist)
    
#8
for loop_var in range(33,256,1):
    print(chr(loop_var))

#9
variable="a string"
print(variable.capitalize())
print(variable.title())
print(variable.lower())
print(variable.upper())
print(variable.replace("a","s"))
print(variable.find("s"))
#10
name="Bobby"
age="10"
state="California"
print("My name is {0}. I am {1} old. I live in {2}.".format(name,age,state))
print(variable.endswith("ing"))
print(variable.isalpha())
print(variable.isnumeric())
print(variable.isupper())
print(variable.islower())

#11
ingredients = "Milk,Flour,Cookies"
Step1, Step2, Product= ingredients.split(",")
print(Step1)
print(Step2)
print(Product)
print(Step1, Step2, Product)
#12
stringvar="   chicken   "
print(len(stringvar))
astripoflife=stringvar.strip()
print(len(astripoflife))

#13
line=open("test_file.txt","r")
print(line.read(1),"1")
time.sleep(1)
print(line.read(2),"2")
time.sleep(1)
print(line.read(3),"3")
time.sleep(1)
print(line.read(4),"4")
time.sleep(1)
print(line.read(5),"5")

#14
def filething():
    afile=open("emptyfileyoungwonkstest.txt","w")
    for loop_var in range(100):
        print(loop_var)
        randomnum=(random.randint(1,1000))
        afile.write(str(randomnum)+" ")
        print(randomnum,file=afile)
    afile.close()
    afile=open("emptyfileyoungwonkstest.txt","r")
    for variable in afile:
        print(variable)
    afile.close()
filething()

#15
print("Give me the source file.")
inpsf=input()
print('Now give me the name of the destination file.')
inpdf=input()
sourcefile=open(inpsf,"r")
destinationfile=open(inpdf,"w")
for lines in sourcefile:
        first,second=lines.split()
        name=first[0]+second.lower()
        print(name, file=destinationfile)
sourcefile.close()
destinationfile.close()
"""
#Dictionary analysis
def semordnilap(n2):
    return n2[::-1]
def reverse(n1):
    return n1[::-1]
print("Give me three letters.")
letter1=input()
letter2=input()
letter3=input()
linesinwordlist=[]
dictionary = {}
athing=0
alphabetincrease=0
words100000=open("wordlist.100000.txt","r")
for loop_var in words100000:
    athing=athing+1
    #how many maximum words in dictionary 
    if loop_var[0] not in dictionary:
        dictionary[loop_var[0]]=1
    if loop_var[0] in dictionary:
       dictionary[loop_var[0]]=dictionary[loop_var[0]]+1
    #finding out the words with the three letters typed in
    #if letter1 in loop_var and letter2 in loop_var and letter3 in loop_var:
        #print(loop_var)
    #no. of words starting with a 'y' pt.1
    #if 'y'==loop_var[-1]:
        #print(loop_var)
    #no. of words starting with a 'y' pt.2
    #if loop_var.endswith('y'):
        #print(loop_var)
    #no. of words starting with a 'y' pt.3
    #if loop_var==something:
        #print(loop_var)
    #print all semordnilap
    something=reverse(loop_var)
    chicken=semordnilap(loop_var)
    linesinwordlist.append(loop_var)
print(linesinwordlist)
for variable in linesinwordlist:
    print(variable,semordnilap(variable))
    if variable in linesinwordlist and semordnilap(variable) in linesinwordlist:
        print(chicken,loop_var)
print('This is the amount of letters that end with y:',alphabetincrease)
print(dictionary)
print('The number of words in this file is',athing)
words100000.close()

                 
    
