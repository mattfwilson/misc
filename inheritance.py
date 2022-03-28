weaponList =[]

class Weapon():
    def __init__(self, id):
        self.id = id

    def say_id(self):
        print("Weapon id is {}.".format(self.id))

class Sword(Weapon):
    def __init__(self, dmg_type):
        self.dmg_type = dmg_type
        
    def say_type(self):
        print("Weapon damage type is {}.".format(self.dmg_type))

weapon1 = Sword("Slashing")
weaponList.append(weapon1)

weapon2 = Sword("Piercing")
weaponList.append(weapon2)

weapon3 = Sword("Slapping")
weaponList.append(weapon3)

for i in weaponList:
    print(i)



