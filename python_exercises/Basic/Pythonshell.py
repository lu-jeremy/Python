Python 3.6.2 (v3.6.2:5fd33b5926, Jul 16 2017, 20:11:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
22+44
66
>>> 
>>> 
>>> 12+12.5
24.5
>>> 13-30
-17
>>> 4x5
SyntaxError: invalid syntax
>>> 4 x 5
SyntaxError: invalid syntax
>>> 4*5
20
>>> 4.0*5
20.0
>>> 44/11
4.0
>>> 5/2
2.5
>>> 7//2%
SyntaxError: invalid syntax
>>> 7//2
3
>>> 7%2
1
>>> Hello+World
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    Hello+World
NameError: name 'Hello' is not defined
>>> Hello World
SyntaxError: invalid syntax
>>> ?Hello?+?World?
SyntaxError: invalid syntax
>>> Hello?+World?
SyntaxError: invalid syntax
>>> "Hello"+"World"
'HelloWorld'
>>> 2+"Hello"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    2+"Hello"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 2,"Hello"
(2, 'Hello')
>>> "2"+"Hello"
'2Hello'
>>> 2**4
16
>>> 2+3*4
14
>>> (2+3)*4
20
>>> teacher='Vishal'
>>> 
>>> teacher
'Vishal'
>>> print teacher
SyntaxError: Missing parentheses in call to 'print'
>>> print (teacher)
Vishal
>>> print("Hello")
Hello
>>> print('Hello'+20)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print('Hello'+20)
TypeError: must be str, not int
>>> print('Hello'+'World')
HelloWorld
>>> print('Hello','World')
Hello World
>>> print('Hello'*20)
HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello
>>> teacher=='vishal'
False
>>> teacher=='Vishal'
True
>>> 1==1
True
>>> teacher!="hello"
True
>>> 100>!
SyntaxError: invalid syntax
>>> 100>1
True
>>> "Batman"=="Superman"
False
>>> (15/2)<=(45+12-27)
True
>>> 1111>=2222/2
True
>>> 7%2<=5
True
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 8, in <module>
    print(len(c))
TypeError: object of type 'int' has no len()
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
Jeremy
Jeremy
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
Jeremy
Jeremy
Please give me 4 numbers
>>> 1
1
>>> 2
2
>>> 3
3
4
>>> 
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
Jerem
Jerem
Please give me 4 numbers
1
2
3
4
The total is 1234
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
j
j
Please give me 4 numbers
1
2
3
4
The total is 1234
11
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
in your name
in your name
Please give me 4 numbers
1
2
3
4
1234
The total is 
>>> 
>>> 
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
j
j
Please give me 4 numbers
1
2
3
4
The total is 12
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 12, in <module>
    total=g+h+j+k
NameError: name 'g' is not defined
>>> 1
1
>>> 2
2
3
>>> 
>>> 4
4
>>> 4nf
SyntaxError: invalid syntax
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
3
1
4
2
The total is 3142
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
1
2
3
4
The total is 1234
What is your name
Bobby
Bobby
Hello 
>>> 
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
3
5
2
4
The total is 3524
What is your name
B
B
Hello 
>>> 
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
b
3
4
2
The total is b342
What is your name
Hello b
Hello  b
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
2
3
4
5
The total is 2345
What is your name
b
Hello b
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
1
2
3
4
The total is 1234
What is your name
b
Hello b
Give me a Fahrenheit temperature
98.6
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 23, in <module>
    c=5/9*(ftemperature-32)
NameError: name 'ftemperature' is not defined
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
b
2
3
4
The total is b234
What is your name
b
Hello b
Give me a Fahrenheit temperature
98.6
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 23, in <module>
    c=5/9*(f-32)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
1
2
3
4
The total is 1234
What is your name
b
Hello b
Give me a Fahrenheit temperature
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 22, in <module>
    f=input(5/9*(f-32))
NameError: name 'f' is not defined
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
1
2
3
4
The total is 1234
What is your name
b
Hello b
Give me a Fahrenheit temperature
98.6
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 23, in <module>
    c=5/9*(f-32)
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
2324
213
213
312
The total is 2324213213312
What is your name
b
Hello b
Give me a Fahrenheit temperature
98.6
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 23, in <module>
    c=input(5/9*(f-32))
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
b
b
b

The total is bb
What is your nameb
b
Hello b
Give me a Fahrenheit temperature
98.6
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 24, in <module>
    c=input(5/9*(f-g))
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
1
2
3
4
The total is 1234
What is your name
b
Hello b
Give me a Fahrenheit temperature
98.7
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 23, in <module>
    c=(f-32)*5/9
TypeError: unsupported operand type(s) for -: 'str' and 'int'
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
1
2
3
4
The total is 1234
What is your name
b
Hello b
Give me any amount of quarters, dimes, nickels, and pennies
1
2
3
4
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 27, in <module>
    td=(quarters*25+dimes*10+nickels*5+pennies*1)/100
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
1
2
3
4
The total is 10
What is your name
b
Hello b
Give me any amount of quarters, dimes, nickels, and pennies
b
b
b
b
Traceback (most recent call last):
b  File "/Users/Jeremy/Documents/Python file.py", line 27, in <module>
    td=(quarters*25+dimes*10+nickels*5+pennies*1)/100

TypeError: unsupported operand type(s) for /: 'str' and 'int'
b
>>> 
>>> b
6
b
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name

============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
Bob
Bob
Please give me 4 numbers
4
3
2
5
The total is 14
What is your name
Bob
Hello Bob
Give me a Fahrenheit temperature
98.6
Traceback (most recent call last):
  File "/Users/Jeremy/Documents/Python file.py", line 22, in <module>
    f=int(input())
ValueError: invalid literal for int() with base 10: '98.6'
>>> 
============== RESTART: /Users/Jeremy/Documents/Python file.py ==============
<class 'str'>
6
<class 'int'>
Please type in your name
b
b
Please give me 4 numbers
1
2
3
4
The total is 10
What is your name
Bob
Hello Bob
Give me a Fahrenheit temperature
7
7 = -13.88888888888889
Give me any amount of quarters, dimes, nickels, and pennies
1
2
3
4
Your total in pennies is: 64 Your total in dollars is: 0.64
>>> 
