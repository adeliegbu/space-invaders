from model.parents_class.ship import Ship
from model.weapon_related.weapons import Weapons

class Bonus_ship(Ship):
    def __init__(self, canvas, x, y, image, direction, projectile_image, refresh_rate):
        super().__init__(canvas, x, y, x_speed=15, y_speed=0, width=60, height=35, life=1, damage=0, image=image, weapon=Weapons(self.refresh_rate, ("assault", "bonus"), projectile_image), refresh_rate=refresh_rate)
        self.direction = direction

    def move(self):
        super().move(self.direction, 0)
    
    def bonus_will_be_out_of_bounds(self):
        return super().will_be_out_of_bounds(self.direction, 0)
