import functools
import random

nums = []
length = 25
largest = 0

for i in range(length):
    randNum = random.randint(0, 100)
    nums.append(randNum)

def findEvens():
    evens = list((filter(lambda x: x % 2 == 0, nums)))
    print(nums)
    print(f'Even numbers: {evens}')

def findLargest():
    largest = functools.reduce(lambda a, b: a if a > b else b, nums)
    print(nums)
    print(f'Largest number: {largest}')

findEvens()
findLargest()