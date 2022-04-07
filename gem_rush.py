import random

stone_types = ["Quartz", "Michah", "Limestone", "Granite", "Diamond"]
rarities = [1, 10]

class Stone():
    def __init__(self, type, rarity):
        self.rock_type = type
        self.rarity = rarity

    def roll(type, rarities):
        type_roll = random.choice(type)
        roll_rarity = random.randint(rarities)
        return type_roll, roll_rarity

mined_stone = Stone(stone_types, rarities)
print(mined_stone)

