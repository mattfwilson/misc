import itertools

enemyPool = []

class Enemy:
    newid = itertools.count().__next__

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

    def say_type(self):
        print("Boss {} is type {} and has {} HP.".format(self.id, self.enemy_type, self.enemy_hp))

class Megaboss(Enemy):
    def __init__(self, enemy_type, enemy_hp, megaboss_hp, underlings=None):
        super().__init__(enemy_type, enemy_hp)
        if underlings == None:
            self.underlings = []
        else:
            self.underlings = underlings
    
    def add_underling(self, underling):
        if underling not in self.underlings:
            self.underlings.append(underling)

    def remove_underling(self, underling):
        if underling in self.underlings:
            self.underlings.remove(underling)

    def print_underlings(self):
        for underling in self.underlings:
            print('Underling id', underling.id)


e0 = Enemy('flying', 55)
print(e0.say_type())

e1 = Enemy('water', 47)
print(e1.say_type())

print(enemyPool)
