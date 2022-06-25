import functools

nums = [0, 1, 475, 5, 4, 3, 20, 86, 21, 7]
largest = []

def findLargest():
    result = list((filter(lambda x: x % 2 == 0, nums)))
    for i in result:
        print(i)

findLargest()