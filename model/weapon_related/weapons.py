from random import randint, choice

from model.weapon_related.cooldown import Cooldown

class Weapons():
    def __init__(self, shooter, type, projectle_class, projectile_image):
        self.shooter = shooter
        self.type = type
        refresh_rate = shooter.refresh_rate

        if type[0] == "weapon_less":
            self.cooldown = Cooldown(100 , refresh_rate, 0)
            self.cooldown_reload = Cooldown(100 , refresh_rate, 0)
            self.cooldown_rafale = Cooldown(100 , refresh_rate, 0)
            self.damage = 0
            self.power = 0
            self.imprecision = 0
            self.rafale = 0
            self.munitions = 0
            self.projectile_width = 0
            self.projectile_height = 0

        if type[0] == "assault":
            self.cooldown = Cooldown(300, refresh_rate, 0)
            self.cooldown_reload = Cooldown(2000, refresh_rate, 0)
            self.cooldown_rafale = Cooldown(100, refresh_rate, 0)
            self.damage = 1
            self.power = 25
            self.imprecision = 1
            self.rafale = 1
            self.munitions = 10
            self.projectile_width = 8
            self.projectile_height = 40
        
        elif type[0] == "sniper":
            self.cooldown = Cooldown(1000, refresh_rate, 0)
            self.cooldown_reload = Cooldown(4000, refresh_rate, 0)
            self.cooldown_rafale = Cooldown(100, refresh_rate, 0)
            self.damage = 2
            self.power = 35
            self.imprecision = 0
            self.rafale = 1
            self.munitions = 5
            self.projectile_width = 6
            self.projectile_height = 40
        
        elif type[0] == "tank":
            self.cooldown = Cooldown(500, refresh_rate, 0)
            self.cooldown_reload = Cooldown(3000, refresh_rate, 0)
            self.cooldown_rafale = Cooldown(75, refresh_rate, 0)
            self.damage = 2
            self.power = 13
            self.imprecision = 2
            self.rafale = 2
            self.munitions = 10
            self.projectile_width = 10
            self.projectile_height = 30
        
        elif type[0] == "machine_gun":
            self.cooldown = Cooldown(150, refresh_rate, 0)
            self.cooldown_reload = Cooldown(4000, refresh_rate, 0)
            self.cooldown_rafale = Cooldown(25, refresh_rate, 0)
            self.damage = 0.5
            self.power = 18
            self.imprecision = 3
            self.rafale = 1
            self.munitions = 40
            self.projectile_width = 6
            self.projectile_height = 20
        
        elif type[0] == "rafale":
            self.cooldown = Cooldown(700, refresh_rate, 0)
            self.cooldown_reload = Cooldown(2500, refresh_rate, 0)
            self.cooldown_rafale = Cooldown(75, refresh_rate, 0)
            self.damage = 1
            self.power = 25
            self.imprecision = 2
            self.rafale = 3
            self.munitions = 12
            self.projectile_width = 8
            self.projectile_height = 40
        
        if type[1] == "alien":
            self.imprecision += 2
            self.damage = 1
            self.munitions = 1000   # Munitions illimitées pour les aliens
            if type[0] == "machine_gun":       # Les aliens ont une mitraillette modifiée à rafale
                self.rafale = 5
                self.damage = 0.5
            self.cooldown.change(4000)
            if self.rafale > 1:
                self.cooldown_rafale.add_offset(randint(0, 4000))
            else:
                self.cooldown.add_offset(randint(0, 4000))

        elif type[1] == "bonus":
            self.cooldown = Cooldown(125, refresh_rate, 0)
            self.munitions = 1000

        self.projectile_class = projectle_class
        self.projectile_image = projectile_image
        self.current_rafale = 0
        self.current_munitions = self.munitions
        self.reloading = False

    def shoot(self):
        x, y = self.shooter.get_position()
        _, height = self.shooter.get_dimensions()
        imprecision = choice([x * 0.1 for x in range(int(- 10 * self.imprecision), int(10 * self.imprecision + 1))])
        if self.rafale > 1:
            if self.current_rafale < self.rafale and self.cooldown_rafale.ended() and self.current_munitions > 0 and not self.reloading:
                self.current_rafale += 1
                self.projectile_class.add_object(x, y, height, imprecision, self.power, self.projectile_width, self.projectile_height, self.damage, self.projectile_image)
                self.current_munitions -= 1
                self.cooldown_rafale.reset()
 
        elif self.rafale == 1:
            if self.cooldown.ended() and self.current_munitions > 0 and not self.reloading:
                self.projectile_class.add_object(x, y, height, imprecision, self.power, self.projectile_width, self.projectile_height, self.damage, self.projectile_image)
                self.current_munitions -= 1
                self.cooldown.reset()
    
    def reload(self):
        if self.current_munitions < self.munitions:
            self.reloading = True
            if self.reloading and self.cooldown_reload.ended():
                self.current_munitions = self.munitions
                self.reloading = False
                self.cooldown_reload.reset()
    
    def upgrade_cooldown(self):
        if self.type[1] == "alien" and self.cooldown_reload.time > 200:
            self.cooldown_reload.change(self.cooldown_reload.time - 200)

        if self.cooldown.time > 30:
            self.cooldown.change(self.cooldown.time - 30)
    
    def upgrade_cooldown_reload(self):
        if self.cooldown_reload.time > 50:
            self.cooldown_reload.change(self.cooldown_reload.time - 50)
    
    def upgrade_cooldown_rafale(self):
        if self.cooldown_rafale.time > 15:
            self.cooldown_rafale.change(self.cooldown_rafale.time - 15)
    
    def upgrade_damage(self):
        if self.type[1] == "alien" or self.type[0] == "machine_gun":
            self.damage += 0.5
        self.damage += 1
    
    def upgrade_power(self):
        self.power += 2
    
    def upgrade_imprecision(self):
        if self.imprecision >= 0.3:
            self.imprecision -= 0.3
    
    def upgrade_rafale(self):
        self.rafale += 1
    
    def upgrade_munitions(self):
        self.munitions += 3
    
    def upgrade_one_caracteristic(self, caracteristic):
        if caracteristic == "cooldown":
            self.upgrade_cooldown()
        elif caracteristic == "cooldown_reload":
            self.upgrade_cooldown_reload()
        elif caracteristic == "cooldown_rafale":
            self.upgrade_cooldown_rafale()
        elif caracteristic == "damage":
            self.upgrade_damage()
        elif caracteristic == "power":
            self.upgrade_power()
        elif caracteristic == "imprecision":
            self.upgrade_imprecision()
        elif caracteristic == "rafale":
            self.upgrade_rafale()
        elif caracteristic == "munitions":
            self.upgrade_munitions()

    def update(self):
        self.cooldown_rafale.update()
        if self.rafale == 1 or self.current_rafale == self.rafale:
            self.cooldown.update()
            if self.cooldown.ended() and self.current_rafale == self.rafale:
                self.current_rafale = 0
                self.cooldown.reset()

        if 0 < self.current_rafale:     # Si le joueur commence une rafale
            self.shoot()

        if self.reloading:
            self.cooldown_reload.update()
            if self.cooldown_reload.ended():
                self.reloading = False
                self.current_munitions = self.munitions
                self.current_rafale = 0
                self.cooldown_reload.reset()
    
    def reset(self):
        self.current_rafale = 0
        self.current_munitions = self.munitions
        self.reloading = False
        self.cooldown.reset()
        self.cooldown_reload.reset()
        self.cooldown_rafale.reset()
