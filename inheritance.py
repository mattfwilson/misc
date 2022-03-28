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
weapon1.say_type()
