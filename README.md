# game_lviv

Repo is divided into two parts: Part 1: a simple walking game, Part2: also a walking game, based on Part1 bit with new classes, inheritance, new mechanics.
Game setting: a player walks through the rooms (or streets of a city, as in Part2) and encounters enemies (also Friends in Part2). Goals differ in both parts.

**Part1**

Modules: game.py, main.py

1. There are overall 3 classes in game.py: Item, Room, Enemy. No inheritance needed here, as this version is much simpler. One item and one enemy is assigned to a single room.

  Item(name, descr),
  
  Room(name, descr, enemy, item),
  
  Enemy(name, descr, convo, weakness),
  
2. main.py: main logic, a game loop. Player has to pick up items that are weaknesses to certain enemies. By properly utilizing that fact,
player will manage to defeat two enemies and win, or loose if does that incorrectly.

Example of a game flow:

<img width="694" alt="Screenshot 2023-03-15 at 02 39 36" src="https://user-images.githubusercontent.com/44242769/225175896-f7e2719c-93b3-402d-81bc-c21e867e0d26.png">

**Part2**

Modules: game_lviv.py, main_lviv.py

1. In addition to previous classes, added new parent classes and children: Character -> Enemy, Character -> Friend, Item -> Weapon, Item -> Trade, Street.
Now each of two enemies has hp and each weapon has a level of damage. Also player can heal if trades a desired object with an NPC.

2. main_lviv.py is based on a samilar main.py from Part1, but modified, notably added trade feature.

Example of a game flow:

<img width="734" alt="Screenshot 2023-03-15 at 03 03 57" src="https://user-images.githubusercontent.com/44242769/225177834-34098142-04c3-40f0-abf2-f3306ea945ed.png">
