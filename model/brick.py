from model.object import Object

class Brick(Object):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, x_speed=0, y_speed=0, width=20, height=20, image=image, life=1)
        
