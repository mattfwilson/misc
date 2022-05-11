numbers = [23, 10, 600, 1, -34, 17, 27, 0, 1234, -5]

def even_or_odd(nums):
    for i, num in enumerate(nums):
        if num % 2 == 0:
            print(f'{num} is an even number')
        else:
            print(f'{num} is an odd number')

even_or_odd(numbers)