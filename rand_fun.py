import random

# x = random.random()
# x_length = len(x)

# print(x_length)

loop = True
count = 0

while loop == True:
    num = int(input('Enter a number: '))

    while (num > 0):
        num = num // 10
        count = count + 1

    print('Total number of digits:', count)