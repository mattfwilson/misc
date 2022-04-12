import random

stone_inv = []

class Stone:
    create_id = 1
    def __init__(self):
        self.id = Stone.create_id
        Stone.create_id += 1

    def roll(self):
        stone_types = ["Pebble", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Moonstone"]
        bad_luck = stone_types[0]

        weighted_roll = random.choices(stone_types, weights=[10, 8, 6, 4, 3, 2, 1])
        roll_str = weighted_roll[0]

        if roll_str == bad_luck:
            print(f"Roll {self.id}: Bad luck... {weighted_roll}")
        elif weighted_roll[0] == stone_types[-1]:
            print(f"Roll {self.id}: You got something amazing! {weighted_roll}")
        else:
            print(f"Roll {self.id}: You got something good! {weighted_roll}")
        return roll_str

    
mined_stone1 = Stone().roll()
stone_inv.append(mined_stone1)
mined_stone2 = Stone().roll()
stone_inv.append(mined_stone2)
mined_stone3 = Stone().roll()
stone_inv.append(mined_stone3)

print(stone_inv)


