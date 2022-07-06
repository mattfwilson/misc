import random

TOTAL_ROLLS = 0
TOTAL_ITEMS = 0
INVENTORY = []

ITEMS = {
    'Club': 30,
    'Dagger': 30,
    'Sword': 20,
    'Axe': 20,
    'Lance': 10,
    'Flail': 10,
    'Longbow': 5,
    'Boxing Gloves': 2,    
}

RARITY = [60, 30, 10]

COMMON_ADJ = {
    'Plebs': 60,
    'Common': 30,
    'Standard': 10,
    }

RARE_ADJ = {
    'Royals': 60,
    'Plated': 30,
    'Hollow': 10,
    }

LEGENDARY_ADJ = {
    'Twilight': 60,
    'Perfected': 30,
    'Blessed': 10,
    }

def showInv():
    print(f'-' * 50)
    for i in RARITY:
        print(f'{i}: {INVENTORY.count(i)}')
    print(f'Total items: {TOTAL_ITEMS}\n' + f'-' * 50 + '\n')

def roll_adj():
    adj_result = random.choices(RARITY, weights=[60, 30, 10])
    return adj_result

def roll_item():
    item_result = random.choices(RARITY, weights=[60, 30, 10])
    return item_result

print(roll_adj())
print(roll_item())

while True:
    action = input('What do you want to do? ')
    if action == 'roll':
        roll()
        TOTAL_ROLLS += 1
    elif action == 'inv':
        showInv()
    elif action == 'count':
        print(f'You have rolled {TOTAL_ROLLS} times.\n')
