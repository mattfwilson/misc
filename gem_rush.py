import random

stone_types = ["Granite", "Michah", "Quartz", "Limestone", "Diamond"]
qualities = [1, 100]

class Stone():
    def __init__(self, type, quality):
        self.rock_type = type
        self.rarity = quality

    def roll_type(self, type):
        type_roll = random.choice(type)
        return type_roll

mined_stone = Stone(stone_types, qualities)
print(mined_stone)

