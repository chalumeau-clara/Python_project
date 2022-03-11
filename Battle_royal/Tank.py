import Player


class Tank(Player):
    def __init__(self):
        self.class_name = "Tank"
        self.name_attack = "Absorption"
        self.damage = 25
        self.speed = 1
        self.defense = 6
        self.health = 150
