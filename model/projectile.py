from model.object import Object

class Projectile(Object):
    def __init__(self, canvas, x, y, image, type):
        super().__init__(canvas, x, y, x_speed=0, y_speed=20, width=9, height=50, image=image)
        self.type = type