#main.py

from room import Room
from Character import Character, Friend, Enemy
from item import Item

cavern = Room("Cavern")
cavern.description = ("A room so big that the light of your torch doesnt reach the walls.")

armoury = Room("Armoury")
armoury.description = ("the walls are lined with racks that once help weapons and armour.")

lab = Room("Laboratory")
lab.description = ("A strange odour hangs in a room filled with unknownabke contraptions.")

Tavern = Room("Tavern")
Tavern.description = ("A room at the front of the game that is the main room")

cavern.link_rooms(armoury,"south")
armoury.link_rooms(cavern,"north")
armoury.link_rooms(lab,"east")
lab.link_rooms(armoury,"west")
Tavern.link_rooms(cavern,"North")

cavern.describe()
armoury.describe()
lab.describe()
Tavern.describe()
#items
cheese = Item("cheese")
cheese.description = "Cheese"

chair =Item("chair")
chair.description = "is designed to be sat on"

elmo = Item("elmo")
elmo.description = "its elmo"

#items in rooms
cavern.item = chair
armoury.item = elmo
lab.item = cheese


'''
# describe rooms
cavern.describe()
armoury.describe()
lab.describe()
Tavern.describe()
'''
#characters
ugine = Enemy("ugine")
ugine.description = "a huge troll with rotting teeth."

nigel = Friend("Nigel")
nigel.description = "a burky dwarf with golden beads woven through his beard."
nigel.conversation = "well youngan, what are you doing here"

tyrone = Friend("Tyrone")
tyrone.description("Tyrone is here")
#chracters in rooms
armoury.character = ugine
lab.character = nigel
Tavern.character = tyrone
# making varible
current_room = cavern
running = True

#main loop
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
        else:
            print("there is no one here to talk to.")
    elif command == "hug":
        if current_room.character is not None:
            current_room.character.hug()
        else:
            print("there is no one to hug here")
    elif command == "fight":
        if current_room.character is not None:
            weapon = input("what will you fight with? > ").lower()
            available_weapons = []
            for item in backpack:
                available_weapons.append(item.name)
            if weapon in available_weapons:
                if current_room.character.fight(weapon):
                    current_room.character = None
                else:
                    running = False
            else:
                print(f"you dont have {weapon}")
                print(f"{current_room.character.name} strikes you down.")
                running = False
        else:
            print("there is no one here to fight")
    elif command == "take":
        if current_room.item is not None:
            backpack.append(current_room.item)
            print(f"you put {current_room.item.name} into your backpack.")
            current_room.item = None
        else:
            print("there is nothing here to take")
    elif command == "backpack"
        if backpack == []:
            print("its empty")
        else:
            print("you have:")
            for item in backpack:
                print(f"- {item.name.capitalize()}")
    elif command == "quit":
        running = False
    else:
        print("i dont understand")