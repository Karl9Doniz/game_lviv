"""Game module.

This module stores all classes needed to play a game about lviv.

https://github.com/Karl9Doniz/game_lviv/
"""

from __future__ import annotations

class Character:
    """
    Character class.
    """

    def __init__(self, name: str, description: str = None, conversation: str = None) -> None:
        """
        Character init method.
        """

        self.name = name
        self.set_desciption(description)
        self.set_conversation(conversation)

    def set_desciption(self, description: str) -> None:
        """
        decription setter
        """

        self.__description = description

    def get_description(self) -> str:
        """
        desciption getter.
        """

        print(self.__description)

    def set_conversation(self, conversation: str) -> None:
        """
        character convo setter.
        """

        self.__conversation = conversation

    def greet(self) -> None:
        """
        greeting method.
        """

        print(self.__conversation)

class Friend(Character):
    """
    Friend class.
    """

    def __init__(self, name: str, description: str = None, conversation: str = None,
                trade_item: Item = None) -> None:
        """
        init method.
        """

        super().__init__(name, description, conversation)
        self.set_trade_item(trade_item)

    def set_trade_item(self, trade_item: Item) -> None:
        """
        trade item setter.
        """

        self.__trade_item = trade_item

    def get_trade_item(self) -> Item:
        """
        trade item getter.
        """

        return self.__trade_item

class Enemy(Character):
    """
    Enemy class.
    """

    def __init__(self, name: str, description: str = None, conversation: str = None,
                health: int = None) -> None:
        """
        init method.
        """

        super().__init__(name, description, conversation)
        self.set_health(health)

    def set_health(self, health: int) -> None:
        """
        enemy health setter.
        """

        self.__health = health

    def get_health(self) -> int:
        """
        health getter.
        """

        return self.__health

class Item:
    """
    Item class.
    """

    def __init__(self, name: str, description: str = None) -> None:
        """
        init method.
        """

        self.name = name
        self.set_description(description)

    def get_name(self) -> str:
        """
        item name getter.
        """

        return self.name

    def set_description(self, description: str) -> None:
        """
        description setter.
        """

        self.__description = description

    def get_description(self) -> str:
        """
        description getter.
        """

        print(self.__description)

class Weapon(Item):
    """
    Weapon class.
    """

    def __init__(self, name: str, description: str = None, damage: int=None) -> None:
        super().__init__(name, description)
        self.set_damage(damage)

    def set_damage(self, damage: int) -> None:
        """
        damage setter.
        """

        self.__damage = damage

    def get_damage(self) -> int:
        """
        damage getter.
        """

        return self.__damage

class Trade(Item):
    """
    Trade class.
    """

    def __init__(self, name: str, description: str = None) -> None:
        super().__init__(name, description)

class Street:
    """
    Street class.
    """

    def __init__(self, name: str, description: str=None,
                character: Character=None, item: Item=None) -> None:
        """
        init method.
        """

        self.name = name
        self.set_description(description)
        self.set_character(character)
        self.set_item(item)
        self.linked_streets = []

    def get_name(self) -> str:
        """
        item name getter.
        """

        return self.name

    def set_description(self, description: str) -> None:
        """
        description setter.
        """

        self.__description = description

    def get_description(self) -> str:
        """
        description getter.
        """

        print(self.__description)

    def set_character(self, character: Character) -> None:
        """
        character setter.
        """

        self.__character = character

    def get_character(self) -> Character:
        """
        character getter.
        """

        return self.__character

    def set_item(self, item) -> None:
        """
        item setter.
        """

        self.__item = item

    def get_item(self) -> Item:
        """
        item getter.
        """

        return self.__item

    def move(self, command: str) -> Street:
        """
        returns a street object that exists in a given direction.
        """

        for street in self.linked_streets:
            if command == street[1]:
                return street[0]
        return self

    def link_street(self, street: Street, direction: str) -> None:
        """
        set linking street and.
        """

        self.street = street
        self.direction = direction

        self.linked_streets.append((self.street, self.direction))
