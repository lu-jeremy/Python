
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

def permutation(n, r):
    factorial(n) / r
if __name__ == '__main__':
    print(factorial(3))
