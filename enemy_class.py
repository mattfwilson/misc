class Enemy():
    ID = 0
    HP = 50
    MP = 10
    ATT = 12
    DEF = 7
    END = 22.6
    TYPE = 'Normal'

    def __init__(self):
        self.enemy_id = Enemy.ID
        self.enemy_type = Enemy.TYPE
        self.enemy_hp = Enemy.HP
        self.enemy_mp = Enemy.MP
        self.enemy_att = Enemy.ATT
        self.enemy_def = Enemy.DEF
        self.enemy_end = Enemy.END
        Enemy.ID += 1

    def say_ID(self):
        print("Enemy ID: {}".format(Enemy.ID))
    
    def say_type(self):
        print("Enemy {} is {}".format(Enemy.ID, Enemy.TYPE))

class Fire(Enemy):
    TYPE = 'Fire'

    def __init__(self):
        # super().__init__(self)
        self.enemy_id = Enemy.ID
        self.enemy_movement = Fire.TYPE

    def say_ID(self):
        print("Enemy ID: {}".format(Enemy.ID))

    def say_type(self):
        print("Enemy {} is {}".format(Enemy.ID, Fire.TYPE))

class Water(Enemy):
    TYPE = 'Water'

    def __init__(self):
        self.enemy_id = Enemy.ID
        self.enemy_type = Water.TYPE

    def say_ID(self):
        print("Enemy ID: {}".format(Enemy.ID))

    def say_type(self):
        print("Enemy {} is {}".format(Enemy.ID, self.enemy_type))
    
e1 = Enemy()
e2 = Fire()
e3 = Water()

enemies = [e1, e2, e3]

for i in enemies:
    i.say_ID()
    i.say_type()


