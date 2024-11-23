class Cooldown:
    def __init__(self, time):
        self.time = time
        self.var = 0

    def ended(self):
        return self.var >= self.time
    
    def reset(self):
        self.var = 0
    
    def update(self):
        self.var += 16  # Incrémenter la variable de cooldown à chaque mise à jour