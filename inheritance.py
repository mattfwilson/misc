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
        
    def say_type(self):
        print("Weapon damage type is {}.".format(self.dmg_type))
    
    def sword_sound(self):
        print("Slaaaash!")

class IceSword(Sword):
    def __init__(self, element):
        self.element = element
    
    def say_element(self):
        print("Weapon element is {}.".format(self.element))

weaponList =[]

iced_sword = IceSword("Ice ice baby")
iced_sword.sword_sound()
iced_sword.say_element()

print(f"Your weapon sounds like a {iced_sword.sword_sound()}")

