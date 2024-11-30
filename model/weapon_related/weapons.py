from random import randint

from model.weapon_related.cooldown import Cooldown

class Weapons():
    def __init__(self, refresh_rate, type, projectile_image):

        if type[0] == "assault":
            self.cooldown = Cooldown(300, refresh_rate, 0)
            self.cooldown_reload = Cooldown(2000, refresh_rate, 0)
            self.cooldown_rafale = Cooldown(100, refresh_rate, 0)
            self.damage = 1
            self.power = 25
            self.rafale = 1
            self.munitions = 10
            self.projectile_width = 8
            self.projectile_height = 40
        
        elif type[0] == "sniper":
            self.cooldown = Cooldown(1000, refresh_rate, 0)
            self.cooldown_reload = Cooldown(4000, refresh_rate, 0)
            self.cooldown_rafale = Cooldown(100, refresh_rate, 0)
            self.damage = 3
            self.power = 35
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
            self.rafale = 2
            self.munitions = 10
            self.projectile_width = 10
            self.projectile_height = 30
        
        elif type[0] == "machine_gun":
            self.cooldown = Cooldown(150, refresh_rate, 0)
            self.cooldown_reload = Cooldown(4000, refresh_rate, 0, 0)
            self.cooldown_rafale = Cooldown(75, refresh_rate, 0)
            self.damage = 0.5
            self.power = 18
            self.rafale = 1
            self.munitions = 30
            self.projectile_width = 6
            self.projectile_height = 20
        
        elif type[0] == "rafale":
            self.cooldown = Cooldown(500, refresh_rate, 0)
            self.cooldown_reload = Cooldown(3000, refresh_rate, 0)
            self.cooldown_rafale = Cooldown(75, refresh_rate, 0)
            self.damage = 1
            self.power = 25
            self.rafale = 3
            self.munitions = 12
            self.projectile_width = 8
            self.projectile_height = 40
        
        if type[1] == "alien":
            self.cooldown.offset = randint(0, 1500)
            self.cooldown.change_time(1500)
            self.munitions = 1000   # Munitions illimitées pour les aliens

        elif type[1] == "bonus":
            self.cooldown = Cooldown(126, refresh_rate, 0)
            self.munitions = 1000

        self.projectile_image = projectile_image
        self.current_rafale = 0
        self.current_munitions = self.munitions
        self.reloading = False

    def shoot(self, projectile_class, x, y, height):
        if self.rafale > 1 and self.current_rafale < self.rafale and self.cooldown_rafale.ended() and self.current_munitions > 0 and not self.reloading:
                self.current_rafale += 1
                projectile_class.add_object(x, y, height, self.power, self.projectile_width, self.projectile_height, self.damage, self.projectile_image)
                self.current_munitions -= 1
                self.cooldown_rafale.reset()

        elif self.cooldown.ended() and self.current_munitions > 0 and not self.reloading:
            projectile_class.add_object(x, y, height, self.power, self.projectile_width, self.projectile_height, self.damage, self.projectile_image)
            self.current_munitions -= 1
            self.cooldown.reset()
    
    def reload(self):
        self.reloading = True
        if self.reloading and self.cooldown_reload.ended():
            self.current_munitions = self.munitions
            self.reloading = False
            self.cooldown_reload.reset()
    
    def upgrade_cooldown(self, value):
        self.cooldown.change(self.cooldown.time - value)
    
    def upgrade_cooldown_reload(self, value):
        self.cooldown_reload.change(self.cooldown_reload.time - value)
    
    def upgrade_cooldown_rafale(self, value):
        self.cooldown_rafale.change(self.cooldown_rafale.time - value)
    
    def upgrade_damage(self, value):
        self.damage += value
    
    def upgrade_power(self, value):
        self.power += value
    
    def upgrade_rafale(self, value):
        self.rafale += value
    
    def upgrade_munitions(self, value):
        self.munitions += value
    
    def update(self):
        if self.rafale == 1 or self.current_rafale == self.rafale:
            self.cooldown.update()
        self.cooldown_rafale.update()
        if self.reloading:
            self.cooldown_reload.update()
            if self.cooldown_reload.ended():
                self.reloading = False
                self.current_munitions = self.munitions
                self.current_rafale = 0
                self.cooldown_reload.reset()

        if self.current_rafale == self.rafale and self.cooldown.ended():
            self.current_rafale = 0
    
    def reset(self):
        self.current_rafale = 0
        self.current_munitions = self.munitions
        self.reloading = False
        self.cooldown.reset()
        self.cooldown_reload.reset()
        self.cooldown_rafale.reset()
