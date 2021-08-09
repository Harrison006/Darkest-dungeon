# item.py
class Item():
    def init__(self, name):
        self.name = name. lower()
        self.description = None
    def describe(self):
        print(f"You see {self.name} in the room. It is {self.description}.")