import Player


class Mage(Player):
    def __init__(self, name):
        self.class_name = "Mage"
        self.name_attack = "Fire spell"
        self.damage = 40
        self.speed = 3
        self.defense = 7
        self.health = 100
        self.name = name
