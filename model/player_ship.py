from model.ship import Ship

class Player_ship(Ship):
    def __init__(self, canvas, x, y, image, cooldown):
        super().__init__(canvas, x, y, x_speed=10, y_speed=0, width=50, height=55, life=3, image=image)
        self.cooldown = cooldown
                
    def shoot(self, projectile_class):
            super().shoot(self.cooldown, projectile_class, type=1)
    
    def update_cooldown(self):
        self.cooldown.update()