from model.parents_class.ship import Ship

class Player_ship(Ship):
    def __init__(self, canvas, x, y, image, weapon, refresh_rate):
        super().__init__(canvas, x, y, x_speed=10, y_speed=0, width=65, height=50, life=3, damage=1, image=image, weapon=weapon, refresh_rate=refresh_rate)
    
    def move_left(self):
        return super().move(-1, 0)
        
    def move_right(self):
        return super().move(1, 0)
