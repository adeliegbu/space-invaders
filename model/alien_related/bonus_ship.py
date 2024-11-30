from model.parents_class.ship import Ship

class Bonus_ship(Ship):
    def __init__(self, canvas, x, y, image, direction, projectile_class, projectile_image, refresh_rate):
        super().__init__(canvas, x, y, x_speed=15, y_speed=0, width=60, height=20, life=1, damage=0, image=image, refresh_rate=refresh_rate)
        self.direction = direction
        self.projectile_class = projectile_class
        self.projectile_image = projectile_image
        self.change_weapon()
    
    def change_weapon(self):
        super().change_weapon("assault", "bonus")
 
    def move(self):
        super().move(self.direction, 0)
    
    def bonus_will_be_out_of_bounds(self):
        return super().will_be_out_of_bounds(self.direction, 0)
