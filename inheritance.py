class Weapon():
    def __init__(self, id):
        self.id = id
        
    def say_id(self):
        print("Weapon id is {}.".format(self.id))

    def make_sound(self):
        print("Whooosh!")

class Sword(Weapon):
    def __init__(self, dmg_type):
        self.dmg_type = dmg_type

    def __repr__(self):
        return self.dmg_type
        
    def say_type(self):
        print("Weapon damage type is {}.".format(self.dmg_type))
    
    def swordSound(self):
        print("Slaaaash!")

weaponList =[]

weapon1 = Sword("Slashing")
weaponList.append(weapon1)

weapon2 = Sword("Piercing")
weaponList.append(weapon2)

weapon3 = Sword("Clapping")
weaponList.append(weapon3)

for i in weaponList:
    print(i)

weapon2.say_type()
weapon2.make_sound()

weaponList[2].say_type() 
weaponList[2].make_sound()


