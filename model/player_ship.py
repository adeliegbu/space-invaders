from model.ship import Ship

class Player_ship(Ship):
    def __init__(self, canvas, x, y, image, cooldown):
        super().__init__(canvas, x, y, x_speed=8, y_speed=0, width=60, height=55, image=image, life=3)
        self.cooldown = cooldown
                
    def shoot(self, projectile, projectile_image):
            super().shoot(self.cooldown, projectile, 1, self.height, projectile_image)
    
    def update(self):
        self.cooldown.update()