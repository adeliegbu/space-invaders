from model.object import Object

class Ship(Object):
    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, image, life):
        super().__init__(canvas, x, y, x_speed, y_speed, width, height, image)
        self.life = life

    def shoot(self, cooldown, projectile, type, projectile_image):
        if cooldown.ended():
            projectile.shot(self.x, self.y, type, self.height, projectile_image)
            cooldown.reset()
    
    def got_hit(self):
        self.life -= 1
        if self.life == 0:
            self.delete()

    

