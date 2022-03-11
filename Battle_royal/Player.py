import random


class Player:
    def __init__(self, name):
        self.name = name
        self.class_name = None
        self.name_attack = None
        self.damage = None
        self.speed = None
        self.defense = None
        self.health = None

    def attack(self, adversary_name):
        print(self.name + " utilise " + self.name_attack + " sur " + adversary_name)

    def take_damage(self, adversary_damage):
        list = []
        for i in range(10):
            if i < self.defense:
                list.append(1)
            else:
                list.append(0)
        take = random.choice(list)
        if take == 0:
            self.health -= adversary_damage
            print(self.name + " perd " + adversary_damage + " point de vies")
        else:
            print(self.name + " arrive à se defendre et ne prend aucun dommage")



