from model.ship import Ship

class Player_ship(Ship):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, life=3, x_speed=8, y_speed=0, width=60, height=55, image=image)
    
    def get_dimensions(self):
        return super().get_dimensions(self.width, self.height)
            
    def shoot(self, cooldown, projectile, projectile_image):
        return super().shoot(cooldown, projectile, 1, self.height, projectile_image)