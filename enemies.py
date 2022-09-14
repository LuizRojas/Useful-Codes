from random import randint


class Character():
    def __init__(self):
        self.life = 0
        self.attack = 0
        self.defense = 0
        self.defending = False

    def attack_enemy(self, enemy: object):
        damage = (self.attack * 50) // (50 + enemy.defense)
        enemy.life -= damage

    def active_defense(self):
        self.defending = True
    
    def critical_attack(self, enemy: object):
        sorted_rand_value = randint(1, 3)

        if (sorted_rand_value > 1):
            print("{}CRITICAL ATTACK{}".format("\033[1;31m", "\033[0m"))
            
            if (sorted_rand_value == 2):
                print("{}DOUBLE CRITICAAAL >:({}".format("\033[1;91m", "\033[0m"))
            
            elif (sorted_rand_value == 3):
                print("{} OH MY GAAAA, TRIPLEE CRITICALLL YEAAAH{}\n".format("\033[1;95", "\033[0m"))
        
        damage = ((self.attack * 50) // (50 + enemy.defense)) * sorted_rand_value
        enemy.life -= damage

class Skeleton(Character):
    def __init__(self):
        Character.__init__(self)
        self.life = 100
        self.attack = 12
        self.defense = 10
        self.defending = False

class Hero(Character):
    def __init__(self):
        Character.__init__(self)
        self.life = 115
        self.attack = 10
        self.defense = 14
        self.defending = False
