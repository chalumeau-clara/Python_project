import Player
import random


class Archer(Player.Player):

    def __init__(self, name):
        self.list = [("Destructive Arrow", 60), ("Devouring Arrow", 80),("Explosive Arrow", 70),("Burning Arrow", 60),("Punitive Arrow", 65), ("Abolition Arrow", 100)]
        self.class_name = "Archer"
        self.attack_name = None
        self.damage = 70
        self.speed = 9
        self.defense = 3
        self.health = 90
        self.name = name
        self.bonus = [["Big arrow", "damage", 20], ["Wolf trap", "health", -20], ["Wolf meat", "health", 10]]
