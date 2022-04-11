import random

stone_types = ['Granite', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Moonstone']

class Stone:
    new_id = 1
    def __init__(self, name="Default Name", type="Default Type"):
        self.id = Stone.new_id
        Stone.new_id += 1
        self.name = type
        self.rock_type = type
        print(f"{name}, {type}, {self.id}")

    def roll_type(self):
        weighted_roll = random.choices(stone_types, weights=[10, 8, 6, 4, 3, 2, 1])
        return weighted_roll

mined_stone1 = Stone("Matt Wilson", "Gold")
mined_stone2 = Stone()
mined_stone3 = Stone("Third Stone")
mined_stone4 = Stone("4th Stone")
print(f"You got a {mined_stone1.roll_type()[0]}!")
