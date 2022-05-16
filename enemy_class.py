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
        self.boss_hp = boss_hp
        boss_health = enemy_hp + self.boss_hp

    def say_type(self):
        print("Boss {} is type {} and has {} HP.".format(self.id, self.enemy_type, self.enemy_hp * 2))

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


e1 = Enemy('Normal', 50)
e1.say_type()

e2 = Boss('Boss', 50, 4)
e2.say_type()

e3 = Megaboss('Ice', 50, 100)
e3.add_underling(e2)
e3.print_underlings()


