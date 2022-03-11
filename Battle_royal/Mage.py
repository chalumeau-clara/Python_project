import Player


class Mage(Player.Player):

    def __init__(self, name):
        self.list = [("Fire spell", 30), ("Ice spell", 25),("Annihilation Spell", 30),("Water Spell", 5),("Meteors Spell", 15), ("sentence irrévocable", 10)]
        self.class_name = "Mage"
        self.attack_name = None
        self.damage = 40
        self.speed = 3
        self.defense = 7
        self.health = 100
        self.name = name
        self.bonus = [["Poison", "health", -10], ["Heal", "health", 20], ["Poison Mushrooms", "defense", -2]]
