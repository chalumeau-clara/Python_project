import Player


class Archer(Player):
    def __init__(self, name):
        self.class_name = "Archer"
        self.name_attack = "Destructive Arrow"
        self.damage = 70
        self.speed = 9
        self.defense = 3
        self.health = 90
        self.name = name
