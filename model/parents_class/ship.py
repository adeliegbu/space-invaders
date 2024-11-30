from model.parents_class.object import Object

class Ship(Object):
    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, life, damage, image, weapon, refresh_rate):
        super().__init__(canvas, x, y, x_speed, y_speed, width, height, life, damage, image)
        self.weapon = weapon
        self.refresh_rate = refresh_rate

    def shoot(self, projectile_class):
        self.weapon.shoot(projectile_class, self.x, self.y, self.height)

    def update_weapon(self):
        self.weapon.update()