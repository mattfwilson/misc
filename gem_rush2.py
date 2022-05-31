import random

inventory = []

class Stone:
    create_id = 1
    def __init__(self):
        self.id = Stone.create_id
        Stone.create_id += 1

    def roll(self):
        stone_types = ['Pebble', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Moonstone']
        weighted_roll = random.choices(stone_types, weights=[7, 6, 5, 4, 3, 2, 1])
        print(f'Roll {self.id}: {weighted_roll}')
        return weighted_roll

def check_quality(roll_lst):
    for i in roll_lst:
        if i == "Diamond":
            print(f'{i}. Godly.')
        elif i == "Moonstone":
            print(f'A {i}! Extremely Rare!')
        elif i == "Platinum":
            print(f'{i}. We take those.')
        elif i == "Gold":
            print(f'{i}. Not too shabby.')
        elif i == "Bronze":
            print(f'{i}. We take those.')
        elif i == "Silver":
            print(f'{i}. Ehhh...')
        elif i == "Pebble":
            print(f'Just a {i}, not great...')

mined_stone1 = Stone().roll()
inventory.append(mined_stone1)

mined_stone2 = Stone().roll()
inventory.append(mined_stone2)

mined_stone3 = Stone().roll()
inventory.append(mined_stone3)

print(inventory)
check_quality(inventory)

reroll = input('Roll again? ')
if reroll == 'y':
    mined_stone4 = Stone().roll()
else:
    print('You are done rolling!')


