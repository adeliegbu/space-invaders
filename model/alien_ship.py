from model.ship import Ship

class Alien_ship(Ship):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, life=1, x_speed=5, y_speed=30, width=50, height=70, image=image)
    
    def get_dimensions(self):
        return super().get_dimensions(self.width, self.height)

    def shoot(self, projectile, projectile_image):
        return super().shoot(projectile, -1, self.height, projectile_image)
    