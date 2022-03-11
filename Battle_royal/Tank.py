import Player


class Tank(Player.Player):
    def __init__(self, name):
        self.class_name = "Paladin"
        self.name_attack = "Absorption"
        self.damage = 25
        self.speed = 1
        self.defense = 6
        self.health = 150
        self.name = name
