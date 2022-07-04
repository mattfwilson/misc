import random

TOTAL_ROLLS = 0
PITY_COUNTER = 0
INVENTORY = []
RARITY = ['Pebble', 'Silver Flake', 'Gold Nugget', 'Platinum Ore', 'Diamond']

def roll():
    result = random.choices(RARITY, weights=[16, 12, 8, 4, 1])
    INVENTORY.append(result[0])
    print(f'You obtained a {result[0]}!\n')

def pity_roll():
    result = random.choices(RARITY, weights=[0, 0, 0, 0, 1])
    INVENTORY.append(result[0])
    print(f'PITY ROLL: You obtained a {result[0]}!\n')
    return result[0]

def showInv():
    for i in RARITY:
        print(f'{i}: {INVENTORY.count(i)}')

while True:
    option = input('What do you want to do? ')
    if option == 'roll':
        if PITY_COUNTER == 10:
            pity_roll()
            TOTAL_ROLLS += 1
            PITY_COUNTER = 0
        else:
            roll()
            TOTAL_ROLLS += 1
            PITY_COUNTER += 1
    elif option == 'inv':
        showInv()
    elif option == 'count':
        print(f'You have rolled {TOTAL_ROLLS} times.')
