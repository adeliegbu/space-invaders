from model.object import Object

class Projectile(Object):
    def __init__(self, canvas, x, y, image, type):
        super().__init__(canvas, x, y, x_speed=0, y_speed=30, width=8, height=50, image=image)
        self.type = type

    def move(self):
        super().move(x_direction=0, y_direction= - self.type)
