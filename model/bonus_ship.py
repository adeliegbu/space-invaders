from model.ship import Ship
from model.cooldown import Cooldown

class Bonus_ship(Ship):
    def __init__(self, canvas, x, y, image, cooldown, direction):
        super().__init__(canvas, x, y, life=1, x_speed=20, y_speed=0, width=50, height=35, image=image)
        self.cooldown = cooldown
        self.direction = direction

    def move(self):
        super().move(self.direction, 0)

    def shoot(self, projectile, projectile_image):
        return super().shoot(self.cooldown, projectile, -1, projectile_image)
    
    def update(self):
        self.cooldown.update()
        self.move()
    