import random

COUNT = 50
ROLL_POOL = []

def roll():
    rarities = ['Common', 'Uncommon', 'Rare', 'Epic', 'Legendary']
    result = random.choices(rarities, weights=[15, 11, 8, 5, 2])
    return result[0]

for i in range(COUNT):
    ROLL_POOL.append(roll())

print(ROLL_POOL)

common = ROLL_POOL.count('Common')
print(f'Common: {common}')
uncommon = ROLL_POOL.count('Uncommon')
print(f'Uncommon: {uncommon}')
rare = ROLL_POOL.count('Rare')
print(f'Rare: {rare}')
epic = ROLL_POOL.count('Epic')
print(f'Epic: {epic}')
legendary = ROLL_POOL.count('Legendary')
print(f'Legendary: {legendary}')

