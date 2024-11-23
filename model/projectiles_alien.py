from model.projectile import Projectile

class Projectile_alien(Projectile):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, type=1, image=image)
        self.projectiles_alien = []
        self.type = 1

    def alien_shot(self):
        self.projectiles_alien.append(Projectile(self.canvas, self.x, self.y, self.image))
