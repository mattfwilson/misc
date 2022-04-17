import random

inventory = []

class Stone:
    create_id = 1
    def __init__(self):
        self.id = Stone.create_id
        Stone.create_id += 1

    def roll(self):
        stone_types = ["Pebble", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Moonstone"]
        weighted_roll = random.choices(stone_types, weights=[8, 8, 6, 4, 3, 2, 2])
        print(f"Roll {self.id}: {weighted_roll}")
        return weighted_roll

def check_quality(roll_lst):
    for i in roll_lst:
        if i == roll_lst[5:]:
            print(f"You found a {i}. V rare!")
        elif i == roll_lst[3:4]:
            print(f"You found a {i}. Dope AF!")
        elif i == roll_lst[1:2]:
            print(f"We'll take a {i}!")
        elif i == roll_lst[0]:
            print(f"{i}... Ehh, not great.")

mined_stone1 = Stone().roll()
inventory.append(mined_stone1[0])

mined_stone2 = Stone().roll()
inventory.append(mined_stone2[0])

mined_stone3 = Stone().roll()
inventory.append(mined_stone3[0])

print(inventory)
check = check_quality(inventory)




