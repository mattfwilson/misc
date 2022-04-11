import random

stone_types = ['Granite', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Moonstone']

class Stone:
    def __init__(self, name="Default Name", type="Default Type"):
        self.name = type
        self.rock_type = type
        print(f"{name}, {type}")

    def roll_type(self):
        weighted_roll = random.choices(stone_types, weights=[10, 8, 6, 4, 3, 2, 1])
        return weighted_roll

mined_stone1 = Stone("Matt Wilson", "Gold")
mined_stone2 = Stone()
print(f"You got a {mined_stone1.roll_type()[0]}!")
