class Fire:
    FIRE_DMG = 5

    def __init__(self):
        self.fire_dmg = Fire.FIRE_DMG
    
    def bonusDamage(self):
        print("Adding {} bonus points of fire damage!".format(self.fire_dmg))

class Enemy(Fire):
    ID = 1
    HP = 50
    MP = 10
    ATT = 12
    DEF = 7
    END = 22.6

    def __init__(self):
        self.enemy_id = Enemy.ID
        self.enemy_hp = Enemy.HP
        self.enemy_mp = Enemy.MP
        self.enemy_att = Enemy.ATT
        self.enemy_def = Enemy.DEF
        self.enemy_end = Enemy.END
        Enemy.ID += 1

    def say_ID(self):
        print("Enemy ID: {}".format(self.enemy_id))

    def say_HP_MP(self):
        print("Enemy HP: {}, MP: {}, END: {}".format(self.enemy_hp, self.enemy_mp, self.enemy_end))
    
e1 = Enemy()
e1.say_ID()

e2 = Enemy()
e2.say_HP_MP()

e3 = Enemy()
e3.say_HP_MP()

e4 = Enemy()
e4.say_HP_MP()
e4.bonusDamage()


