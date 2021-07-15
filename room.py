# room.py
class Room():
    def __init__(self,room_name):
        self.name= room_name.lower()
        self.description = None
        self.linked_rooms = {}
        
    def describe(self):
        print(f"\nYou are in the {self.name}")
        print(self.description)
        for direction in self.linked_rooms:
             print(f"to the {direction} is the {self.linked_rooms[direction].name}")
            
    def link_rooms(self, room_to_link, direction):
        self.linked_rooms[direction.lower()]= room_to_link
        