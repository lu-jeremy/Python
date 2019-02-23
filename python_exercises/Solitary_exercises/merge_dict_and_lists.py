num = [1, 2, 3, 4]
num2 = [1, 2, 3, 4]

num3 = [*num, *num2]

print(num3)

num = {'apple': 1}
num2 = {'banana': 2}

num3 = {**num, **num2}

print(num3)
