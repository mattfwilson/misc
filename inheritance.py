class Weapon():
    weapon_id = 10
    def __init__(self):
        self.id = Weapon.weapon_id
        Weapon.weapon_id += 1

    def say_id(self):
        print("Weapon id is {}.".format(self.id))

class IceSword(Weapon):
    pass

weapon1 = IceSword()
weapon1.say_id()

weapon2 = IceSword()
weapon2.say_id()
