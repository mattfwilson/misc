class Enemy:
    id = 1

    def __init__(self, type, hp):
        self.enemy_type = type
        self.enemy_hp = hp
        self.id += 1

    def say_type(self):
        print("Enemy {} is type {} and has {} HP.".format(self.id, self.enemy_type, self.enemy_hp))

class Fire(Enemy):
    def say_type(self):
        print("Enemy {} is type {} and has {} HP.".format(self.id, self.enemy_type, self.enemy_hp))

    
e1 = Enemy("Flying", 50)
e2 = Fire("Noob", 1)


print(e1.say_type())
print(e2.say_type())
# print(help(e1))

