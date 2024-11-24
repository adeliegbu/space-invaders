from model.ship import Ship
from model.cooldown import Cooldown

class Bonus_ship(Ship):
    def __init__(self, canvas, x, y, direction, image):
        super().__init__(canvas, x, y, life=1, x_speed=20, y_speed=0, width=40, height=35, image=image)
        self.direction = direction
        self.cooldown = Cooldown(50)
    
    def get_dimensions(self):
        return super().get_dimensions(self.width, self.height)

    def move(self):
        super().move(self.direction, 0)

    def shoot(self, projectile, projectile_image):
        return super().shoot(self.cooldown, projectile, -1, self.height, projectile_image)
    