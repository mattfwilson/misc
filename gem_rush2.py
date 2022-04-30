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
        if i == "Diamond" or i == "Moonstone":
            print(f'A {i}! Extremely Rare!')
        elif i == "Silver" or i == "Gold" or i == "Platinum":
            print(f'{i}. We take those.')
        else:
            print(f'Just a {i}, not great...')

mined_stone1 = Stone().roll()
inventory.append(mined_stone1)

mined_stone2 = Stone().roll()
inventory.append(mined_stone2)

mined_stone3 = Stone().roll()
inventory.append(mined_stone3)

print(inventory)
check_quality(inventory)



