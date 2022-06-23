import random

loop = True
count = 0

while loop is True:
    num = int(input('Enter a number: '))

    while (num > 0):
        num = num // 10
        count = count + 1
    if count <= 2:
        print('Oh come on that\'s a puny number to count...')
        count = 0
    else:
        print('Total number of digits:', count)
        count = 0