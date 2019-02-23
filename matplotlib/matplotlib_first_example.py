import matplotlib.pyplot as plt

#y = 3x + 4

X = [590,540,740,130,810,300,320,230,470,620,770,250]
Y = [32,36,39,52,61,72,77,75,68,57,48,48]

plt.title('Relationship Between Temperature and Iced Coffee Sales')

plt.xlabel('Cups of Iced Coffee Sold')

plt.ylabel('Temperature in Fahrenheit')

x = []
y = []

for var in range(0, 1000, 100):
    value = 3 * var + 4
    x.append(var) 
    y.append(value)
    
plt.plot(x, y)
plt.scatter(x, y)
    
##plt.xlim(0, 1000)
##plt.ylim(0, 1000)

##plt.scatter(X, Y, s=60, c='red', marker='^')
##plt.scatter(Y, X, s=60, c='blue')

plt.show()
