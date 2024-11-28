from model.object import Object

class Ship(Object):
    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, life, image):
        super().__init__(canvas, x, y, x_speed, y_speed, width, height, life, image)

    def shoot(self, cooldown, projectile_class, type):
        if cooldown.ended():
            projectile_class.add_object(self.x, self.y - type * self.height)
            cooldown.reset()