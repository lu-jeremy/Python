import argparse
import sys

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a)

def main():
    ap = argparse.ArgumentParser(description = 'The following program'
                                 'does the fibonacci sequence.')
    
    ap.add_argument('num', type = int, help = 'Give me a number that entails'
                    'the amount of times the fibonacci sequence will run')
    
    args = ap.parse_args()
    
    result = fibonacci(args.num)
    
    sys.stdout.write('Result: ' + str(result) + 'Fib Num: ' + str(args.num))

if __name__ == '__main__':
    main()

    

