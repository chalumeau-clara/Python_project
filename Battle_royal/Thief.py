import Player


class Thief(Player.Player):
    def __init__(self, name):
        self.list = [("Insidious Poison", 60), ("Cut Throat", 70), ("Fear", 80)]
        self.class_name = "Thief"
        self.name_attack = None
        self.damage = 70
        self.speed = 10
        self.defense = 5
        self.health = 75
        self.name = name
