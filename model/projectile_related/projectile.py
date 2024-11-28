from model.parents_class.object import Object

class Projectile(Object):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, x_speed=0, y_speed=20, width=8, height=50, image=image, life=1)
