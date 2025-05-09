class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.tricks = []
    
    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        self.energy = min(100, self.energy + 10)
        print(f"You fed {self.name}. Hunger decreased!")
        sel.time_passes()
    
    def play(self):
        if self.energy <= 10:
            print(f"{self.name} is too tired to play! Let them rest first.")
            return
        self.happiness = min(100, self.happiness + 20)
        self.hunger = min(100, self.hunger + 10)
        self.energy = max(0, self.energy - 15)
        print(f"You played with {self.name}. Happiness increased!")
        self.time_passes()
    
    def teach_trick(self, trick):
        if trick in sel.tricks:
            (print(f"{self.name} already knows how to {trick}!")
             return
        if self.energy <+10:
            print(f"{self.name} is too tired to learn new tricks!")
            return
        self.tricks.append(trick)
        self.happiness = min(100, self.happiness + 10)
        print(f"{self.name} learned a new trick: {trick}!")
        self.time_passes()
    
    def sleep(self):
        self.energy = min(100, self.energy + 30)
        self.hunger = min(100, self.hunger + 10)
        print(f"{self.name} took a nap. Energy restored!")
        self.time_passs()
    
    def show_tricks(self):
        if not self.tricks:
            print(f"{self.name} doesn't know any tricks yet!")
        else:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
    
    def check_status(self):
        print(f"\n{self.name}'s Status:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100")
        print(f"Tricks known: {len(self.tricks)}\n")
    
    def time_passes(self):
        """Simulates the passage of time (called after each action)"""
        self.hunger = min(100, self.hunger + 5)
        self.happiness = max(0, self.happiness - 5)
        self.energy = max(0, self.energy - 5)
