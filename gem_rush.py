import random

stone_types = ['Granite', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Moonstone']

class Stone:
    def __init__(self, type="Default", name="Name"):
        self.rock_type = type
        self.name = type
        print(type, name)

    def roll_type(self):
        weighted_roll = random.choices(stone_types, weights=[10, 8, 6, 4, 3, 2, 1])
        return weighted_roll

mined_stone1 = Stone("Not default")
mined_stone2 = Stone()
print(mined_stone1.roll_type())
