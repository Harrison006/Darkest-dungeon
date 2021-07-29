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
class Friend(Character):
    
    def __init__(self,name):
        super().__init__(name)
    
    def hug(self):
        print(f"{self.name} hugs you back")
        
        
class Enemy(Character):
    
    def __init__(self,name):
        super().__init__(name)
        self.weakness = None
        
    def fight(self,item):
        if item == self.weakness:
            print(f"You strike {self.name} down with {item}")
            return True
        else:
            print(f"{self.name} crushes you. Puny adventuruer")
            return False