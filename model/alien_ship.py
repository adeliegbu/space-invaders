from model.ship import Ship

class Alien_ship(Ship):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, life=1, x_speed=5, y_speed=20, width=50, height=35, image=image)

    def shoot(self, cooldown, projectile, projectile_image):
        return super().shoot(cooldown, projectile, -1, projectile_image)
    