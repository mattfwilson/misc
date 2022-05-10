class Enemy():

    def __init__(self):
        self.enemy_id = 0
        self.enemy_type = 'Normal'
        self.enemy_hp = 50
        self.enemy_id += 1
    
    def say_type(self):
        print("Enemy {} is {} type".format(self.enemy_id, self.enemy_type))

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

