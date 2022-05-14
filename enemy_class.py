class Enemy:
    id = 1

    def __init__(self, enemy_type, enemy_hp):
        self.enemy_type = enemy_type
        self.enemy_hp = enemy_hp
        self.id += 1

    def say_type(self):
        print("Enemy {} is type {} and has {} HP.".format(self.id, self.enemy_type, self.enemy_hp))

class Boss(Enemy):

    def __init__(self, enemy_type, enemy_hp, boss_hp):
        super().__init__(enemy_type, enemy_hp)
        self.boss_hp = 1.5
        boss_health = enemy_hp * self.boss_hp
        return boss_health
    def say_type(self):
        print("Enemy {} is type {} and has {} HP.".format(self.id, self.enemy_type, self.enemy_hp))

    
e1 = Enemy("Normal", 50)
e2 = Boss("Fire", 50, None)


print(e1)
print(e2)
print(help(e1))

