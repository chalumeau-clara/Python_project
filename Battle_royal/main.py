import random
import Player
import Warrior
import Mage
import Thief
import Tank
import Archer


class Jeu:

    def __init__(self, nb_players):
        self.nb_players = nb_players
        self.players = [None for i in range(self.nb_players)]

    def choose_two_players(self):
        index1 = random.randint(0, len(self.players) - 1)
        index2 = random.randint(0, len(self.players) - 1)

        while index1 == index2:
            index2 = random.randint(0, len(self.players) - 1)

        if index1 < index2:
            index1, index2 = index2, index1

        return (self.players[index1], index1), (self.players[index2], index2)

    def randomPlayer(self, playerName):
        """
        Instantiate a player by picking randomly its type.
        :param playerName:
        :return:
        """
        player_types = [Warrior.Warrior, Mage.Mage, Thief.Thief, Tank.Tank, Archer.Archer]
        return random.choice(player_types)(playerName)

    def start(self):
        names = ["Dodchard", "Redan", "Edjoan", "Lassan", "Nyacas", "Samarma", "Tachet", "Jashabryt", "Daha", "Risroy",
                 "Chetvia", "Maroy", "Leofven", "Ald", "Damas", "Dod", "Barchet", "Isenphia", "Lasbar", "Thorke",
                 "Bardbald", "Wig-sara", "Mark-egar", "Bur-ceol", "Roneadbryt", "Velldocpa", "Tonchrisbard",
                 "Renferwen",
                 "Laf-guth", "Mondmasmark", "Vid-da", "Carbethord", "Barddonmenjack", "Eapherbeth", "Saraacardic",
                 "Cachell", "Chel'ra", "Anseredo", "Beorthconjo", "Charcomeard", "Annecia", "Fortinrob", "Gormaleofu",
                 "Johnvell", "Bethsyl", "Bardfast", "Fridly", "Laclaf", "Nassa", "Comesajo", "Joansan", "Edmond",
                 "Casdon",
                 "Sig'ly", "Cuthriret", "Ferumto", "Elidryt", "Do", "Lestim", "Ferumrobris", "Easter", "Egg", "Robert",
                 "Valentin", "Clara", "Clarel", "Elodie", "Mickael", "Toto"]

        # Create players
        for i in range(self.nb_players):
            print(names[i])
            self.players[i] = self.randomPlayer(names[i])

        # Run till one player left
        while self.nb_players > 1:
            # Picks two random players and returns first player to start and second
            (first, index1), (second, index2) = self.choose_two_players()

            first.attack(second)
            second.take_damage(first)

            # Come back from player 2
            if second.health > 0:
                second.attack(first)
                first.take_damage(second)
            else:
                self.players.pop(index2)
                self.nb_players -= 1

            if first.health <= 0:
                self.players.pop(index1)
                self.nb_players -= 1
                print(str(self.nb_players) + " left")
            if second.health <= 0:
                self.players.pop(index2)
                self.nb_players -= 1
                print(str(self.nb_players) + " left")

            # Remove dead players.
        if self.nb_players == 0:
            print("\nEveryone died :/")
        else:
            print("\n" + self.players[0].name + " ( " + self.players[0].class_name + " ) wins !")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to Sweet Justice battle royal!\n")
    while True:
        print("Enter a number of players between 2 and 50: ")
        while True:
            nb_players = int(input())
            if 2 <= nb_players <= 50:
                break
            print("Is not between 2 and 50 ! Please enter a number again")
        jeu = Jeu(nb_players)
        jeu.start()

        print("\nRestart game ? (Yes or No)")
        restart = input()
        if restart == "No":
            print("Bye Bye")
            break
