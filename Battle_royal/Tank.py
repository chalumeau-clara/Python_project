import Player


class Tank(Player.Player):
    def __init__(self, name):
        self.list = [("Assault", 15), ("Furia", 10),("Immolation", 20),("Templar's Hostility", 25),("Madness of the templar", 50), ("Absorption", 40)]
        self.class_name = "Tank"
        self.name_attack = "Absorption"
        self.damage = 25
        self.speed = 1
        self.defense = 6
        self.health = 150
        self.name = name
