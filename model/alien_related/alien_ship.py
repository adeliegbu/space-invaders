from random import choice, choices

from model.parents_class.ship import Ship


class Alien_ship(Ship):
    def __init__(self, canvas, x, y, image, refresh_rate, projectile_class, projectile_image):
        super().__init__(canvas, x, y, x_speed=5, y_speed=25, width=40, height=25, life=1, damage=1, image=image, refresh_rate=refresh_rate, projectile_class=projectile_class, projectile_image=projectile_image)
        self.level = 0
        self.type = None
    
    def change_weapon(self, wepon_type):
        super().change_weapon(wepon_type, "alien")
    
    def increase_level(self):
        self.level += 1

        if self.level == 1:     # Initialise l'arme de l'alien à partir du niveau 1
            self.type = choice(["assault", "rafale", "machine_gun", "sniper", "tank"])
            self.change_weapon(self.type)

        if self.level % 2 == 0:
            super().upgrade_one_caracteristic("life")

        upgrade_choiced = choices(["cooldown", "cooldown_rafale", "damage", "power", "rafale"], [0.4, 0.1, 0.1, 0.3, 0.1], k=1)[0]
        super().upgrade_one_caracteristic(upgrade_choiced)
    
    def become_doctor(self):
        self.type = "doctor"
    
    def dead(self):
        if super().dead():
            return True



