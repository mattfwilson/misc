import random

TOTAL_ROLLS = 0
PITY_COUNTER = 0
TOTAL_ITEMS = 0
INVENTORY = []
RARITY = ['Flint', 'Silver', 'Gold', 'Platinum', 'Diamond']

def showInv():
    print(f'-' * 50)
    for i in RARITY:
        print(f'{i}: {INVENTORY.count(i)}')
    print(f'Total items: {TOTAL_ITEMS}\n' + f'-' * 50 + '\n')

def roll():
    global TOTAL_ITEMS
    result = random.choices(RARITY, weights=[13, 8, 5, 3, 2])
    INVENTORY.append(result[0])
    TOTAL_ITEMS += 1
    print(f'You obtained 1 {result[0]}!\n')

def pity_roll():
    global TOTAL_ITEMS
    result = random.choices(RARITY, weights=[0, 0, 0, 0, 1])
    INVENTORY.append(result[0])
    TOTAL_ITEMS += 1
    print(f'PITY ROLL: You obtained 1 {result[0]}!\n')
    return result[0]

while True:
    action = input('What do you want to do? ')
    if action == 'roll':
        if PITY_COUNTER == 25:
            pity_roll()
            TOTAL_ROLLS += 1
            PITY_COUNTER = 0
        else:
            roll()
            TOTAL_ROLLS += 1
            PITY_COUNTER += 1
    elif action == 'inv':
        showInv()
    elif action == 'count':
        print(f'You have rolled {TOTAL_ROLLS} times.\n')
