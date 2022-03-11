import Player
import random


class Warrior(Player.Player):

    def __init__(self, name):
        self.list = [("Strengthstorm", 50), ("Divine Sword", 50),("Celestial Sword", 40),("Evil Sword", 40),("Fit of Rage", 60), ("Last whisper", 60)]
        self.class_name = "Warrior"
        self.attack_name = None
        self.damage = 50
        self.speed = 7
        self.defense = 2
        self.health = 100
        self.name = name
        self.bonus = [["Thor's Hammer", "damage", 10], ["Heal", "health", 10], ["Warrior effect", "damage", 20]]