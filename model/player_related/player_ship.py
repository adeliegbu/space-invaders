from model.parents_class.ship import Ship

class Player_ship(Ship):
    def __init__(self, canvas, x, y, image, refresh_rate, projectile_class, projectile_image):
        super().__init__(canvas, x, y, x_speed=13, y_speed=0, width=60, height=40, life=5, damage=1, image=image, refresh_rate=refresh_rate)
        self.projectile_class = projectile_class
        self.projectile_image = projectile_image
    
    def move_left(self):
        return super().move(-1, 0)
        
    def move_right(self):
        return super().move(1, 0)
    
    def change_weapon(self, wepon_type):
        super().change_weapon(wepon_type, "player")
    
    def new_life(self):
        self.life += 1
        if self.life > 5:
            self.life = 5
    
    def become_doctor(self):
        return None

        
