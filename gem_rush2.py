import random

class Stone:
    create_id = 1
    def __init__(self):
        stone_types = ["Pebble", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Moonstone"]
        bad_luck = stone_types[0]

        self.id = Stone.create_id
        Stone.create_id += 1

        weighted_roll = random.choices(stone_types, weights=[10, 8, 6, 4, 3, 2, 1])
        roll_str = weighted_roll[0]

        if roll_str == bad_luck:
            print(f"Roll {self.id}: Bad luck... {weighted_roll}")
        elif weighted_roll[0] == stone_types[-1]:
            print(f"Roll {self.id}: You got something amazing! {weighted_roll}")
        else:
            print(f"Roll {self.id}: You got something good! {weighted_roll}")
    
mined_stone1 = Stone()
mined_stone2 = Stone()
mined_stone3 = Stone()
mined_stone4 = Stone()
mined_stone5 = Stone()
