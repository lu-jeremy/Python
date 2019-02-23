
import multiprocessing



def add(x, y):
    print(x + y)


if __name__ == '__main__':
    for i in range(5):
        mp = multiprocessing.Process(target = add, args = (i, i+1))
        mp.start()
        mp.join()



from multiprocessing import Pool

def multiply(num):
    return num ** 3

if __name__ == '__main__':
    p = Pool(processes = 20)
    data = p.map(multiply, range(2))
    p.close()
    print(data)


'
