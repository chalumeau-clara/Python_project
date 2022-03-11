import Player
import random


class Warrior(Player):
    def __init__(self):
        self.class_name = "Warrior"
        self.name_attack = "Strengthstorm"
        self.damage = 50
        self.speed = 7
        self.defense = 2
        self.health = 100
