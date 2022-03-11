import Player


class Thief(Player.Player):
    def __init__(self, name):
        self.class_name = "Voleur"
        self.name_attack = "Furia"
        self.damage = 70
        self.speed = 10
        self.defense = 5
        self.health = 75
        self.name = name
