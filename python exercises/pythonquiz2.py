import random
#1
# A list stores elements for later use. index, element

#2
# Key: value
"""
#3
names = ['Bob', 'Bobby', 'Bill', 'Jones', 'Billy']
print(names)
print(len(names))
print(names[len(names)-1])
names[len(names)-1] = 'Jason'
print(names)

#4
randomnumbers = []
for loop_var in range(0,20,1):
    toappend = random.randint(1,100)
    randomnumbers.append(toappend)
for var in randomnumbers:
    if var%2 == 0:
        print(var,'even')
    if var%2 == 1:
        print(var,'odd')
 
#5, 6
letters = ['a', 'b','c', 'd' ,'e','f','g' ,'h', 'i' ,'j' 'k', 'l', 'm','n', 'o', 'p','q','r' ,'s' ,'t' ,'u', 'v', 'w', 'x', 'y' ,'z']
while (1):
    rsamples = random.sample(letters,8)
        
    newletters = ''.join(rsamples)
    if 'q' in rsamples:
        print(newletters)
        break
    print(newletters)
#7, 8, 9
num = {1:2,2:4,3:6,4:8,5:10}
print(num)
num[6] = 12
print(num)
num[1] = 1
print(num)
#10
chicken = {}
for var in range(0,10,1):
    randomnum = random.randint(0,1000)
    chicken[randomnum] = randomnum**2
print(chicken)
#11
caps = {"Austria":"Vienna", "Switzerland":"Bern", "Germany":"Berlin", "Netherlands":"Amsterdam"}
for key in caps:
    print(key,caps[key])

 
#12
iandprices = {'computer':500, 'pencil':1, 'glasses':20, 'book':10,'jacket':5}
least_key = ''
least_value = 1000
count = 0
while count<=4:
    for key in iandprices:
        if iandprices[key]<least_value:
            least_value = iandprices[key]
            least_key = key
    print(least_value, least_key)
    count = count+1
    iandprices.pop(least_key)
    least_key = ''
    least_value = 1000

#13
one = {'a':1}
two = {'b':2}
combined = {}
combined.update(one)
combined.update(two)
print(combined)

#14
letters = {}
word = input('give me a word\n')
for var in word:
    if var not in letters:
        letters[var] = 0
    if var in letters:
        letters[var] = letters[var]+1
    print(letters)
"""
