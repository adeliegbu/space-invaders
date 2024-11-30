from typing import Any


class Cooldown:
    def __init__(self, time, refresh_rate, offset):
        self.time = time + offset
        self.refresh_rate = refresh_rate
        self.offset = offset
        self.var = offset

    def get_progression(self):
        if self.time - self.offset != 0:
            return (self.var - self.offset) / (self.time - self.offset)
        
    def ended(self):
        return self.var >= self.time
    
    def reset(self):
        self.var = self.offset
    
    def update(self):
        if not self.ended():
            self.var += self.refresh_rate
    
    def change(self, time):
        self.time = time + self.offset
    
