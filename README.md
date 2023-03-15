# game_lviv

Repo is divided into two parts: Part 1: a simple walking game, Part2: also a walking game, based on Part1 bit with new classes, inheritance, new mechanics.
Game setting: a player walks through the rooms (or streets of a city, as in Part2) and encounters enemies (also Friends in Part2). Goals differ in both parts.

**Part1**

Modules: game.py, main.py

1. There are overall 3 classes in game.py: Item, Room, Enemy. No inheritance needed here, as this version is much simpler. One item and one enemy is assigned to a single room.

  Item(name, descr)
  Room(name, descr, enemy, item)
  Enemy(name, descr, convo, weakness)
  
2. main.py: main logic, a game loop. Player has to pick up items that are weaknesses to certain enemies. By properly utilizing that fact,
player will manage to defeat two enemies and win, or loose if does that incorrectly.

Example of a game flow:



