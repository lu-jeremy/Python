input_list = [5,6,10]

def div_by_five(num):
    if num % 5 == 0:
        return True
    return False

generator = (print(i) for i in input_list if div_by_five(i))

for i in generator:
    #can just say i instead of print(i) if it is on a generator
    #because it already says print(i) in generator
    i

print('separation')

generator = [i for i in input_list if div_by_five(i)]

print(generator)

print('separation')

#print x eight times 
[ [ print(x, y) for x in range(0, 5, 5) ] for y in range(0, 10, 5) ]

#same thing as before
#for y in range(0, 40, 5), then execute the following code that many times
for y in range(0, 5, 5):
    for x in range(0, 30, 5):
        print(x, y)

