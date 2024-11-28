from model.parents_class.ship import Ship

class Alien_ship(Ship):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, x_speed=5, y_speed=20, width=50, height=35, life=1, image=image)

    def shoot(self, cooldown, projectile_class):
            super().shoot(cooldown, projectile_class, height=-0.6)