import random


class Player:

    def __init__(self, name):
        self.list = None
        self.name = name
        self.class_name = None
        self.attack_name = None
        self.damage = None
        self.speed = None
        self.defense = None
        self.health = None
        self.bonus = None

    def attack(self, adversary):
        """
        Manage attack
        :param adversary: the adversary player
        """
        (self.attack_name, self.damage) = random.choice(self.list)
        print(self.name + " ( " + self.class_name + " ) uses " + self.attack_name + " on " + adversary.name
              + " ( " + adversary.class_name + " )")

    def take_damage(self, adversary):
        """
        Manage damage and health
        :param adversary: the adversary player
        """
        # Chance of not take damage
        list = []
        for i in range(10):
            if i < self.defense:
                list.append(1)
            else:
                list.append(0)
        take = random.choice(list)
        if take == 0:
            self.health -= adversary.damage

            # Manage bonus
            if self.health <= 0:
                print(self.name + " is dead")
                bon = random.choice(self.bonus)
                if bon[1] == "health":
                    adversary.health += bon[2]
                elif bon[1] == "speed":
                    adversary.speed += bon[2]
                elif bon[1] == "defense":
                    adversary.defense += bon[2]
                elif bon[1] == "damage":
                    adversary.damage += bon[2]
                print(adversary.name + " gets " + bon[0] + " : " + str(bon[2]) + " " + bon[1])
            print(self.name + " ( " + self.class_name + " ) lost " + str(adversary.damage) + " life points.")
        else:
            print(self.name + " ( " + self.class_name + " ) does not take any dammages.")



