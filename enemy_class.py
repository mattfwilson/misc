class Enemy:
    ID = 1
    HP = 50
    MP = 10
    ATT = 12
    DEF = 7

    def __init__(self):
        self.enemy_id = Enemy.ID
        self.enemy_hp = Enemy.HP
        self.enemy_mp = Enemy.MP
        self.enemy_att = Enemy.ATT
        self.enemy_def = Enemy.DEF
        Enemy.ID += 1

    def say_ID(self):
        print("Enemy ID: {}".format(self.enemy_id))

    def say_HP_MP(self):
        print("Enemy HP: {}, MP: {}".format(self.enemy_hp, self.enemy_mp))
    
e1 = Enemy()
e1.say_ID()

e2 = Enemy()
e2.say_HP_MP()

e3 = Enemy()
e3.say_HP_MP


