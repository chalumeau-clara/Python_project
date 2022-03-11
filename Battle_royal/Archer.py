import Player
import random

class Archer(Player):
    def __init__(self):
        self.class_name = "Archer"
        #archer_spells = [("Destructive Arrow", 60), ("Devouring Arrow", 80), ("Explosive Arrow", 20),
                         #("Burning Arrow", 10), ("Punitive Arrow", 10), ("Abolition Arrow", 120)]
        #self.name_attack, self.damage = random.choice()
        self.name_attack = "Destructive Arrow"
        self.damage = 70
        self.speed = 9
        self.defense = 3
        self.health = 90
