class Enemy():
    id = 1

    def __init__(self):
        self.enemy_id = Enemy.id
        self.enemy_type = 'Normal'
        self.enemy_hp = 100
        Enemy.id += 1

    def say_type(self):
        print("Enemy {} is type {} and has {} HP.".format(self.enemy_id, self.enemy_type, self.enemy_hp))

class Fire(Enemy):
    def __init__(self):
        self.enemy_type = 'Fire'

class Water(Enemy):
    def __init__(self):
        self.enemy_type = 'Water'
    
e1 = Enemy()
e2 = Fire()
e3 = Water()

print(e1.say_type())
print(e2.say_type())
print(e3.say_type())

