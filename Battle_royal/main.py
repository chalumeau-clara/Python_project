import random
import Player
import Warrior
import Mage
import Thief
import Tank
import Archer


def choose_two_players(players):
    index1 = random.randint(0, len(players) - 1)
    index2 = random.randint(0, len(players) - 1)

    while index1 == index2:
        index2 = random.randint(0, len(players)- 1)

    return (players[index1], index1), (players[index2], index2)


# Instantiate a player by picking randomly its type.
def randomPlayer(playerName):
    player_types = [Warrior.Warrior, Mage.Mage, Thief.Thief, Tank.Tank, Archer.Archer]

    return random.choice(player_types)(playerName)


def main():
    names = ["Dodchard", "Redan", "Edjoan", "Lassan", "Nyacas", "Samarma", "Tachet", "Jashabryt", "Daha", "Risroy",
             "Chetvia", "Maroy", "Leofven", "Ald", "Damas", "Dod", "Barchet", "Isenphia", "Lasbar", "Thorke",
             "Bardbald", "Wig-sara", "Mark-egar", "Bur-ceol", "Roneadbryt", "Velldocpa", "Tonchrisbard", "Renferwen",
             "Laf-guth", "Mondmasmark", "Vid-da", "Carbethord", "Barddonmenjack", "Eapherbeth", "Saraacardic",
             "Cachell", "Chel'ra", "Anseredo", "Beorthconjo", "Charcomeard", "Annecia", "Fortinrob", "Gormaleofu",
             "Johnvell", "Bethsyl", "Bardfast", "Fridly", "Laclaf", "Nassa", "Comesajo", "Joansan", "Edmond", "Casdon",
             "Sig'ly", "Cuthriret", "Ferumto", "Elidryt", "Do", "Lestim", "Ferumrobris", "Easter", "Egg", "Robert",
             "Valentin", "Clara", "Clarel", "Elodie", "Mickael"]

    nb_players = 5
    players = [None for i in range(nb_players)]

    # Create players
    for i in range(nb_players):
        players[i] = randomPlayer(names[i])

    # Run till one player left
    while nb_players > 1:
        # Picks two random players and returns first player to start and second
        (first, index1), (second, index2) = choose_two_players(players)

        first.attack(second)
        second.take_damage(first.damage)

        # Come back from player 2
        if second.health > 0:
            second.attack(first)
            first.take_damage(second.damage)
        else:
            players.pop(index2)
            nb_players -= 1

        if first.health <= 0:
            players.pop(index1)
            nb_players -= 1

        # Remove dead players.
    print(players[0].name + " ( " + players[0].name + " ) Wins !")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
