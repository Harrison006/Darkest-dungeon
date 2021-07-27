#Charector.py
class Character():
    
    def __init__(self,name):
        self.name = name
        self.description = None
        self.conversation = None
        
        
    def describe(self):
        print(f"{self.name} is here, {self.description}")
        
    def hug(self):
        print(f"{self.name} doesnt want to hug you")
        
    def fight(self):
        print(f"{self.name} doesnt want to fight you")
        
        
    def talk(self):
        if self.conversation is not None:
            print(f"{self.name}: {self.conversation}")
        else:
            print(f"{self.name} doesnt want to talk to you")
