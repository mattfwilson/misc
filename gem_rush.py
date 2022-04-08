import random

stone_types = ['Granite', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond']

class Stone:
    def __init__(self, type):
        self.rock_type = type

    def __str__(self, type):
        print(type)

    def roll_type(self):
        weighted_roll = random.choices(stone_types, weights=[10, 7, 5, 3, 2, 1])
        return weighted_roll

mined_stone = Stone(stone_types)
print(mined_stone.roll_type()[0])


