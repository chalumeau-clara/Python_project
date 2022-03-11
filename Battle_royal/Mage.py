import Player


class Mage(Player.Player):
    def __init__(self, name):
        self.list = mage_spells = [("Fire spell", 5), ("Ice spell", 15),("Annihilation Spell", 1000),("Water Spell", 0),("Meteors Spell", 5), ("sentence irrévocable", 10)]
        self.class_name = "Wizard"
        self.name_attack = None
        self.damage = 40
        self.speed = 3
        self.defense = 7
        self.health = 100
        self.name = name
