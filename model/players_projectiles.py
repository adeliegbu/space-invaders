from model.projectiles import Projectiles
from model.projectile import Projectile

class Players_projectiles(Projectiles):
    def __init__(self, canvas, image):
        super().__init__(canvas)
        self.image = image
    
    def add_object(self, x, y):
        super().add_object(x, y, self.image)
    
    def move(self):
        super().move(y_direction=-1)
    
    def collision(self, aliens, walls):
        super().collision(aliens)
        super().collision(walls)