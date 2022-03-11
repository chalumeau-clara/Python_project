import random

from Warrior import Warrior
from Warrior import Mage
from Warrior import Thief
from Warrior import Tank
from Warrior import Archer

# Instantiate a player by picking randomly its type.
def randomPlayer(playerName):
    player_types = {
        "warrior": Warrior,
        "mage": Mage,
        "thief": Thief,
        "tank": Tank,
        "archer": Archer
    }

    return random.choice(list(player_types.items()))[1](playerName)

def main():
    names = { "Leo", "King", etc}
    nb_players = 50
    players = []

    for i in range(nb_players):
        players[i] = randomPlayer(names[i])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
