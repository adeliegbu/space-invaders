from model.projectile_related.projectiles import Projectiles

class Aliens_projectiles(Projectiles):
    def __init__(self, canvas, refresh_rate, image):
        super().__init__(canvas, refresh_rate)
        self.image = image
    
    def add_object(self, x, y, height, power, projectile_width, projectile_height, damage, projectile_image):
        super().add_object(x, y + height, power, projectile_width, projectile_height, damage, projectile_image)
    
    def move(self):
        super().move(y_direction=1)
