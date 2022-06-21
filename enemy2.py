import itertools

enemyPool = []

class Enemy:
    newid = itertools.count(1).__next__

    def __init__(self, enemy_type, enemy_hp):
        self.newid = Enemy.newid()
        self.enemy_type = enemy_type
        self.enemy_hp = enemy_hp
        enemyPool.append(self)

    @property
    def health(self):
        return self.enemy_hp

    @health.setter
    def health(self, enemy_hp):
        if enemy_hp <= 10:
            self.enemy_hp = 10
    
    @health.deleter
    def health(self):
        del self.enemy_hp

    def say_type(self):
        print("Enemy {} is type {} and has {} HP.".format(self.newid, self.enemy_type, self.enemy_hp))
    
    def __repr__(self):
        return '{}'.format(self.newid)

class Boss(Enemy):

    def __init__(self, enemy_type, enemy_hp, boss_hp):
        super().__init__(enemy_type, enemy_hp)
        self.boss_hp = boss_hp
        boss_health = enemy_hp + self.boss_hp
        return boss_health

    def say_type(self):
        print("Boss {} is type {} and has {} HP.".format(self.id, self.enemy_type, self.enemy_hp))


e0 = Enemy('flying', 55)
print(e0.say_type())

e1 = Enemy('water', 47)
print(e1.say_type())

e3 = Enemy('earth', 1769)
print(e3.say_type())

print(enemyPool)
for i in enemyPool:
    pass
print(f'There are {len(enemyPool)} active enemies')
