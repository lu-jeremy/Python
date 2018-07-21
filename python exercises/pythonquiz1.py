import random
#1
1==1
#2

birth = int(input('give me your year of birth'))
years = 2018-birth
print('your age in years is:', years, ', your age in days is:', 365*years,', and your age in seconds is',86400*(365*years)) 

#3
age = int(input('what is your age'))
if age>=16:
    print('You are eligible to drive')
else:
    print('You are not eligible to drive')

#4
number = int(input('give me a number'))
prime = 1
count = 1
while count<number/2:
    count = count+1
    if number%count == 0:
        prime = 0
        break
if prime == 0:
    print('your number is not prime')
if prime == 1:
    print('your number is prime')

#5
income = int(input('give me your annual income'))
if 0<=income<9275:
    print('your tax is 10 percent')
    tax = 10
elif 9275<=income<37650: #difference between if and elif: elif says if first if is not correct it will skip and go to the next one
    print('your tax is 15 percent')
    tax = 15
elif 37650<=income<91150:
    print('your tax is 25 percent')
    tax = 25
elif 91150<=income<190150:
    print('your tax is 28 percent')
    tax = 28
elif 190150<=income<413350:
    print('your tax is 33 percent')
    tax = 33
elif 413350<=income<415050:
    print('your tax is 35 percent')
    tax = 35
else:
    print('your tax is 39.6 percent')
    tax = 39.6
result = ((tax/100)*income)+income
print('your result after tax is added is', result)

#6 & 7 (help)
while True:
    try:
        worked = int(input('please give me your hours worked'))
        rate = int(input('please give me your hourly rate'))
        break
    except:
        print('Error, please enter numeric input')
if worked<=40:
    pay = worked*rate
    print('your pay is',pay)
elif worked>40:
    pay = rate*40
    pay2 = ((worked-40)*rate)*1.5
    pay3 = pay+pay2
    print('your pay is',pay3)
   
#8
for loop_var in range(1500,2701,1):
    if loop_var%7 == 0:
        print(loop_var)
    if loop_var%5 == 0:
        print(loop_var)

#9
count = 0
for loop_var in range(1,6,1):
    print(loop_var*('*'))
    count = count+1
    if count == 5:
        for s in range(4,0,-1):
            print(s*('*'))

#10
for val in range(0,7,1):
    if val == 3:
        continue
    if val == 6:
        continue
    print(val)

#11
even = []
odd  = []
for var in range(0,21,1):
    random1 = random.randint(1,100)
    if random1%2 == 0:
        even.append(random1)
        numeven = len(even)
    if random1%2 == 1:
        odd.append(random1)
        numodd = len(odd)
print('number of odd numbers:',numodd, 'number of even numbers:', numeven)

#12
number = input('give me 6 numbers')
a,b,c,d,e,f = number.split(',')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
addition = a+b+c+d+e+f
print(addition)

#13
number = int(input('give me an number between 2 and 10'))
while True:
    ran = random.randint(1,100)
    print(ran,number)
    if ran%number == 0: 
        break

#14
threeletter = []
fiveletter = []
sevenletter = []
words = open("wordlist.100000.txt","r")
for loop_var in words:
    if len(loop_var)==4:
        threeletter.append(loop_var[0:3])
    if len(loop_var)==6:
        fiveletter.append(loop_var[0:5])
    if len(loop_var)==8:
        sevenletter.append(loop_var[0:7])
r = random.choice(threeletter)
randomone = random.choice(fiveletter)
randomtwo = random.choice(sevenletter)
print(r,randomone,randomtwo)
