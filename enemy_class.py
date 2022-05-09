class Enemy():
    ID = 0
    HP = 50
    MP = 10
    ATT = 12
    DEF = 7
    END = 22.6
    MOVEMENT = 'walking'

    def __init__(self):
        self.enemy_id = Enemy.ID
        self.enemy_hp = Enemy.HP
        self.enemy_mp = Enemy.MP
        self.enemy_att = Enemy.ATT
        self.enemy_def = Enemy.DEF
        self.enemy_end = Enemy.END
        self.enemy_movement = Enemy.MOVEMENT
        Enemy.ID += 1

    def say_ID(self):
        print("Enemy ID: {}".format(Enemy.ID))
    
    def movement(self):
        print("Enemy {} is {}".format(Enemy.ID, Enemy.MOVEMENT))


class Flying(Enemy):
    MOVEMENT = 'fLying'

    def __init__(self):
        # super().__init__(self)
        self.enemy_id = Enemy.ID
        self.enemy_movement = Flying.MOVEMENT
        Enemy.ID += 1

    def movement(self):
        print("Enemy {} is {}".format(Enemy.ID, Flying.MOVEMENT))

class Water(Flying):
    MOVEMENT = 'swimming'

    def __init__(self):
        self.enemy_id = Enemy.ID
        self.enemy_movement = Water.MOVEMENT
        Enemy.ID += 1

    def movement(self):
        print("Enemy {} is {}".format(Enemy.ID, self.enemy_movement))
    
e1 = Enemy()
e1.movement()

e2 = Flying()
e2.movement()

e3 = Water()
e3.movement()


