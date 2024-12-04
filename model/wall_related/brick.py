from model.parents_class.object import Object

class Brick(Object):
    def __init__(self, canvas, x, y, image, refresh_rate):
        super().__init__(canvas, x, y, x_speed=0, y_speed=0, width=20, height=20, life=1, damage=1, image=image, refresh_rate=refresh_rate)
        
