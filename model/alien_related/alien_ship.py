from model.parents_class.ship import Ship

class Alien_ship(Ship):
    def __init__(self, canvas, x, y, image, weapon, refresh_rate):
        super().__init__(canvas, x, y, x_speed=5, y_speed=25, width=40, height=35, life=1, damage=1, image=image, weapon=weapon, refresh_rate=refresh_rate)
        self.damage = 1
        self.level = 1
    
    def increase_level(self):
        self.level += 1
        if self.level == 2:
            self.life = 2

