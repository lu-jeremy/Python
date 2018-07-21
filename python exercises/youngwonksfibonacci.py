def fibbonaci(n):
    if n==0:
        return [0]
    if n==1:
        return [0,1]
    numbers=[0,1]
    count=2
    while count<n:
        numbers.append(numbers[count-2]+numbers[count-1])
        print(numbers[count-2]+numbers[count-1])
        count=count+1
    return numbers
var=fibbonaci(20)
print(var)

def fib(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
var=fib(20)
print(var)
