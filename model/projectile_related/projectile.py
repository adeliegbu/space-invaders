from model.parents_class.object import Object

class Projectile(Object):
    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, damage, image, refresh_rate):
        super().__init__(canvas, x, y, x_speed=x_speed, y_speed=y_speed, width=width, height=height, life=1, damage=damage, image=image, refresh_rate=refresh_rate)