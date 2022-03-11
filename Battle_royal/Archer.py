import Player
import random


class Archer(Player.Player):
    def __init__(self, name):
        self.list = [("Destructive Arrow", 60), ("Devouring Arrow", 80),("Explosive Arrow", 70),("Burning Arrow", 60),("Punitive Arrow", 65), ("Abolition Arrow", 100)]
        self.class_name = "Archer"
        self.name_attack = None
        self.damage = 70
        self.speed = 9
        self.defense = 3
        self.health = 90
        self.name = name
