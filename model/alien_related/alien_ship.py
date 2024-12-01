from random import choice, choices

from model.parents_class.ship import Ship


class Alien_ship(Ship):
    def __init__(self, canvas, x, y, image, refresh_rate, projectile_class, projectile_image):
        super().__init__(canvas, x, y, x_speed=5, y_speed=25, width=40, height=25, life=1, damage=1, image=image, refresh_rate=refresh_rate)
        self.projectile_class = projectile_class
        self.projectile_image = projectile_image
        self.level = 1
        self.doctor = False
        self.upgrade_choices = ["cooldown", "cooldown_rafale", "damage", "power", "rafale"]
        self.upgrade_weights = [0.4, 0.15, 0.05, 0.5, 0.15]
    
    def change_weapon(self, wepon_type):
        super().change_weapon(wepon_type, "alien")
    
    def increase_level(self):
        self.level += 1

        if self.level == 2:     # Initialise l'arme de l'alien à partir du niveau 2
            self.change_weapon(choice(["assault", "rafale", "machine_gun", "sniper", "tank"]))

        if self.level % 3 == 0:
            self.life += 1

        upgrade_choiced = choices(self.upgrade_choices, self.upgrade_weights, k=1)[0]
        self.weapon.upgrade_one_caracteristic(upgrade_choiced)
    
    def become_doctor(self):
        self.change_weapon("weapon_less")
        self.doctor = True
    
    def dead(self):
        if super().dead():
            return True



