from model.projectile_related.projectiles import Projectiles
from model.projectile_related.projectile import Projectile

class Aliens_projectiles(Projectiles):
    def __init__(self, canvas, image):
        super().__init__(canvas)
        self.image = image
    
    def add_object(self, x, y):
        super().add_object(x, y, self.image)
    
    def move(self):
        super().move(y_direction=1)
