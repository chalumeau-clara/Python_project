# Python project: Battle Royal

---
## Sweet Justice battle royal

---
# Python version tested on: v3.8

The project is organized as follows:

It contains a class Player that implements the methods all players need.

Player class has 7 attributes:
- name: player's name
- class_name: player's class
- attack_name: player's attack name
- damage: player's damage
- speed: player's speed
- defense: player's defense
- health: player's health
- bonus: list of bonuses tied to the class
- list: list of spells and associated damage

5 classes exist in the game: Tank, Wizard, Archer, Warrior, Thief.
The mentioned classes inherit from the Player class.

Player class contains 2 methods:
- attack: current player attacks the adversary
- take_damage: current player loses adversary_damage life points

If a player kills another one, he gains a bonus according to the
killed player's class.

Finally, we have a main class that initializes a list of players
and launches the game.
Each time a player is killed, he is removed from the players list.
The game continues until there's only one player left.

All you need to do is enter the Battle_Royal directory and use the command "python3 main.py" to launch the game.

Enjoy!
