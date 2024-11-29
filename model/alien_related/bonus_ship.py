from model.parents_class.ship import Ship
from model.cooldown import Cooldown

class Bonus_ship(Ship):
    def __init__(self, canvas, x, y, image, cooldown, direction):
        super().__init__(canvas, x, y, x_speed=15, y_speed=0, width=60, height=35, image=image, life=1)
        self.cooldown = cooldown
        self.direction = direction

    def move(self):
        super().move(self.direction, 0)
    
    def bonus_will_be_out_of_bounds(self):
        return super().will_be_out_of_bounds(self.direction, 0)

    def shoot(self, projectile_class):
        return super().shoot(self.cooldown, projectile_class, -1)

    def update_cooldown(self):
        self.cooldown.update()