#main.py

from room import Room


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

'''
# describe rooms
cavern.describe()
armoury.describe()
lab.describe()
Tavern.describe()
'''

# making varible
current_room = cavern
running = True

#main loop
while running:
    current_room.describe()
    
    command = input("> ").lower()
    
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "quit":
        running = False
    else:
        print("i dont understand")