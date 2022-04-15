import random

inventory = []

class Stone:
    create_id = 1
    def __init__(self):
        self.id = Stone.create_id
        Stone.create_id += 1

    def roll(self):
        stone_types = ["Pebble", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Moonstone"]
        weighted_roll = random.choices(stone_types, weights=[10, 8, 6, 4, 3, 2, 10])
        print(f"Roll {self.id}: {weighted_roll}")
        return weighted_roll

def check_quality(roll_lst):
    if "Moonstone" in roll_lst:
        print(f"You found a Moonstone. V rare!")
    elif "Diamond" in roll_lst:
        print(f"You found a Diamond. Stellar!")
    else:
        print(f"Ehh...")

mined_stone1 = Stone().roll()
inventory.append(mined_stone1[0])

mined_stone2 = Stone().roll()
inventory.append(mined_stone2[0])

mined_stone3 = Stone().roll()
inventory.append(mined_stone3[0])

print(inventory)
check = check_quality(inventory)




