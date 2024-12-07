from model.parents_class.object import Object
from model.weapon_related.weapons import Weapons

class Ship(Object):
    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, life, damage, image, refresh_rate, projectile_class, projectile_image):
        super().__init__(canvas, x, y, x_speed, y_speed, width, height, life, damage, image, refresh_rate)
        self.weapon = None
        self.projectile_class = projectile_class
        self.projectile_image = projectile_image

    def shoot(self):
        if self.weapon is not None:
            self.weapon.shoot()
    
    def change_weapon(self, wepon_type, shooter_type):
        self.weapon = Weapons(self, (wepon_type, shooter_type), self.projectile_class, self.projectile_image)

    def update_weapon(self):
        self.weapon.update()
    
    def upgrade_one_caracteristic(self, caracteristic):
        if caracteristic == "life":
            self.life += 1
        elif caracteristic == "speed":
            self.x_speed += 1
        else:
            self.weapon.upgrade_one_caracteristic(caracteristic)