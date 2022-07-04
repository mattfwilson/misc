import random
import time

NUM_ROLLS = 0
COUNTER = 10
POOL = []
RARITIES = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']

def roll():
    result = random.choices(RARITIES, weights=[15, 12, 8, 4, 2])
    POOL.append(result[0])
    print(f'You obtained a {result[0]} item!')
    return result[0]

def pity_roll():
    result = random.choices(RARITIES, weights=[0, 0, 0, 0, 1])
    return result[0]

def summary():
    common = POOL.count(RARITIES[0])
    print(f'Common: {common}')
    uncommon = POOL.count(RARITIES[1])
    print(f'Uncommon: {uncommon}')
    rare = POOL.count(RARITIES[2])
    print(f'Rare: {rare}')
    epic = POOL.count(RARITIES[3])
    print(f'Epic: {epic}')
    legendary = POOL.count(RARITIES[4])
    print(f'Legendary: {legendary}')

while True:
    option = input('What do you want to do? [roll/inv/count] ')
    if option == 'roll':
        roll()
        NUM_ROLLS += 1
    elif option == 'inv':
        summary()
    elif option == 'count':
        print(f'You have rolled {NUM_ROLLS} times.')
