from model.parents_class.ship import Ship

class Alien_ship(Ship):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, x_speed=5, y_speed=25, width=40, height=35, life=1, image=image)
        self.level = 1

    def shoot(self, cooldown, projectile_class):
            super().shoot(cooldown, projectile_class, height=-0.6)
    
    def increase_level(self):
        self.level += 1
        if self.level == 2:
            self.life = 2
