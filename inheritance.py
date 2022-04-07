class Weapon():
    def __init__(self, id):
        self.id = id
        
    def say_id(self, id):
        print("Weapon id is {}.".format(id))

    def make_sound(self):
        print("Whooosh!")

class Sword(Weapon):
    def __init__(self, dmg_type):
        self.dmg_type = dmg_type
        
    def say_type(self, dmg_type):
        print("Weapon damage type is {}.".format(dmg_type))
    
    def sword_sound(self):
        return "Slaaaash!"

class IceSword(Sword):
    def __init__(self, element):
        self.element = element
    
    def say_element(self):
        print("Weapon element is {}.".format(self.element))

weapon_roll = IceSword("Ice")
weapon_roll.say_id(4)
weapon_roll.say_element()
weapon_roll.say_type("Slashing")

print(f'Your weapon sounds like, "{weapon_roll.sword_sound()}"')

