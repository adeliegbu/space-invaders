from model.parents_class.ship import Ship

class Player_ship(Ship):
    def __init__(self, canvas, x, y, image, cooldown, projectile_class):
        super().__init__(canvas, x, y, x_speed=10, y_speed=0, width=50, height=55, life=3, image=image)
        self.cooldown = cooldown
        self.projectile_class = projectile_class
    
    def move_left(self):
         super().move(-1, 0)
        
    def move_right(self):
        super().move(1, 0)
                
    def shoot(self):
            super().shoot(self.cooldown, self.projectile_class, height=0.5)
    
    def update_cooldown(self):
        self.cooldown.update()