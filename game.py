"""Game module.

This module stores all classes neede to play a game.

https://github.com/Karl9Doniz/game_lviv/
"""

from __future__ import annotations

class Room:
    """
    Room class.
    """

    def __init__(self, name: str, description: str="",
                character: Enemy=None, item: Item=None) -> None:
        """
        init method.
        """

        self.name = name
        self.set_description(description)
        self.set_character(character)
        self.set_item(item)
        self.linked_rooms = []

    def set_description(self, description: str) -> None:
        """
        setter for description.
        """

        self.description = description

    def get_details(self):
        """
        getter for description
        """

        print(self.description)

    def link_room(self, room: Room, direction: str) -> None:
        """
        set linking room and.
        """

        self.room = room
        self.direction = direction

        self.linked_rooms.append((self.room, self.direction))

    def set_character(self, character: Enemy) -> None:
        """
        setter for character in the room.
        """

        self.character = character

    def get_character(self) -> Enemy:
        """
        getter for character in the room.
        """

        return self.character

    def set_item(self, item: Item) -> None:
        """
        setter for item in the room.
        """

        self.item = item

    def get_item(self) -> Item:
        """
        getter for item in the room.
        """

        return self.item

    def move(self, command: str) -> Room:
        """
        returns a room object that exists in a given direction.
        """

        for room in self.linked_rooms:
            if command == room[1]:
                return room[0]
        return self


class Enemy:
    """
    Enemy class.
    """

    defeated = 0

    def __init__(self, name:str, description:str, conversation: str=None,
                weakness: str=None) -> None:
        """
        init method.
        """

        self.name = name
        self.description = description
        self.set_weakness(weakness)
        self.set_conversation(conversation)

    def set_description(self, description: str) -> None:
        """
        setter for enemy description.
        """

        self.description = description

    def describe(self) -> None:
        """
        get enemy's description.
        """

        print(self.description)

    def set_conversation(self, conversation: str) -> None:
        """
        setter for enemy's conversation.
        """

        self.conversation = conversation

    def talk(self) -> None:
        """
        prints enemy's conversation.
        """

        print(self.conversation)

    def set_weakness(self, weakness: str) -> None:
        """
        setter for enemy weakness.
        """

        self.weakness = weakness

    def fight(self, fight_with: str) -> bool:
        """
        Returns true if defeated, false if not. Outcome
        depends on weakness.
        """

        if fight_with == self.weakness:
            Enemy.defeated += 1
            return True
        return False

    def get_defeated(self) -> int:
        """
        gets count of defeated enemies.
        """

        return self.defeated


class Item:
    """
    Item class.
    """

    def __init__(self, name: str, description: str=None) -> None:
        """
        init method.
        """

        self.name = name
        self.set_description(description)

    def get_name(self) -> str:
        """
        getter for item name.
        """

        return self.name

    def set_description(self, description: str) -> None:
        """
        setter for description.
        """

        self.description = description

    def describe(self) -> None:
        """
        print description of an item.
        """

        print(self.description)
