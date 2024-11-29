from model.projectile_related.projectile import Projectile

class Weapon():
    def __init__(self, cooldown, damage, power, rafale, munitions):
        # Rafale change de cooldown pour x fois puis revient sur le long cooldown
        self.cooldown = cooldown
        self.damage = damage
        self.power = power
        self.rafale = rafale
        self.munitions = munitions
    
    def shoot(projectile):
        pass