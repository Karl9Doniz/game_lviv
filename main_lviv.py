import game_lviv

pidvalna = game_lviv.Street("Pidvalna st.")
pidvalna.set_description("A narrow street with a tram railway and a bus stop")

stryiska = game_lviv.Street("Stryiska st.")
stryiska.set_description("A long street, with a Stryisky park on the left side.")

kozelnytska = game_lviv.Street("Kozelnytska st.")
kozelnytska.set_description("Home sweet home... Finally safe!")

vynnychenka = game_lviv.Street("V. Vynnychenka st.")
vynnychenka.set_description("Dark street with old Soviet-era buildings.")

ruska = game_lviv.Street("Ruska st.")
ruska.set_description("Wet pavements with Austrian buildings surrounding the alley.")

fedorova = game_lviv.Street("I. Fedorova st.")
fedorova.set_description("Stone roads and a blinking lamp on the corner.")

arsenalna = game_lviv.Street("Arsenalna st.")
arsenalna.set_description("Short street with nice cafes... Closed in that time of day.")

pidvalna.link_street(vynnychenka, "east")
vynnychenka.link_street(pidvalna, "west")
vynnychenka.link_street(stryiska, "south")
stryiska.link_street(vynnychenka, "north")
stryiska.link_street(kozelnytska, "south")
kozelnytska.link_street(stryiska, "north")
pidvalna.link_street(ruska, "west")
ruska.link_street(fedorova, "south")
ruska.link_street(pidvalna, "east")
fedorova.link_street(ruska, "north")
fedorova.link_street(arsenalna, "east")
arsenalna.link_street(fedorova, "west")

alcoholic = game_lviv.Enemy("Alcoholic")
alcoholic.set_health(50)
alcoholic.set_desciption(f"A nameless alcoholic with a bottle of horilka in his hands. \
HP: {alcoholic.get_health()}")
alcoholic.set_conversation("Heyy...Got any penny for an old man?")


ruska.set_character(alcoholic)

bandit = game_lviv.Enemy("Bandit")
bandit.set_health(75)
bandit.set_desciption(f"Strong man, i'd better have something tough to get through him. \
HP: {bandit.get_health()}")
bandit.set_conversation("Looking for problems mate?")

stryiska.set_character(bandit)

lost_tourist = game_lviv.Friend("Lost tourist")
lost_tourist.set_desciption("A tourist. He seems lost, probably first time here... and at night!")
lost_tourist.set_conversation("Hey! Umm, maybe got a map? I-i could use one. Can trade it for\
 some patches")

vynnychenka.set_character(lost_tourist)

sketchy_guy = game_lviv.Friend("Sketchy guy")
sketchy_guy.set_desciption("Seems sketchy...but maybe he'll help me")
sketchy_guy.set_conversation("Hey you! Come here! I see you're in trouble, so there's mybaseball bat.\
 Maybe you have a beer or something?")

arsenalna.set_character(sketchy_guy)

beer = game_lviv.Trade("Beer")
beer.set_description("A bootle of beer, full.")
pidvalna.set_item(beer)

map = game_lviv.Trade("Map")
map.set_description("A detailed map of Lviv.")
arsenalna.set_item(map)

bottle = game_lviv.Weapon("Bottle")
bottle.set_damage(25)
bottle.set_description("An empty bottle.")
ruska.set_item(bottle)

bat = game_lviv.Weapon("Baseball bat")

bat.set_damage(50)

sketchy_guy.set_trade_item(bat)

current_street = pidvalna
backpack = []

dead = False
points = 2

while dead == False:

    print("\n")
    current_street.get_description()

    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.get_description()

    item = current_street.get_item()
    if item is not None:
        item.get_description()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        current_street = current_street.move(command)
        if current_street.get_name == "Kozelnytska st.":
            print("You're home! That was a hell of a night walk.")
            dead = True

    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.greet()
    elif command == "fight":
        if isinstance(inhabitant, game_lviv.Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:

                if fight_with in ['Bottle', 'Baseball bat']:
                    weapon = None
                    if fight_with == 'Bottle':
                        weapon = bottle
                    else:
                        weapon = bat
                    # What happens if you win?
                    current_hp = inhabitant.get_health() - weapon.get_damage()
                    inhabitant.set_health(current_hp)
                    print(current_hp)
                    if current_hp > 0:
                        points -= 1
                        if points == 0:
                            dead == True
                    else:
                        current_street.set_character = None
                        print("You won in this fight!")
                else:
                    print("That's not a weapon!")
            else:
                print("You don't have a " + fight_with)
        elif isinstance(inhabitant, game_lviv.Friend):
            print("He's friendly!")
        else:
            print("There is no one here to fight with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")
    elif command == "trade":
        if isinstance(inhabitant, game_lviv.Friend):
            print("Choose what you want to trade")
            entry = input("> ")
            if inhabitant.get_trade_item() == None and inhabitant.name != "Lost tourist":
                print("Got nothing to trade with now")
            elif inhabitant.name == "Sketchy guy" and entry == "Beer":
                print("You put the " + inhabitant.get_trade_item().get_name() + " in your backpack")
                backpack.append(inhabitant.get_trade_item().get_name())
                inhabitant.set_trade_item(None)
            elif inhabitant.name == "Lost tourist" and entry == "Map":
                print("Thanks! Now I'll go.")
                current_street.set_character(None)
                print("You healed 1 point!")
                points += 1
            else:
                print("Can't trade for that")
        else:
            print("Can't trade here")
    else:
        print("I don't know how to " + command)
