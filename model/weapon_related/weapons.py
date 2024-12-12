# -*- coding: utf-8 -*-
"""
File Name: weapons.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Weapons class, which handles the various weapons that a shooter can use in the game.
             It includes functionality for shooting, reloading, upgrading weapons, and handling cooldowns and ammunition.

TODO: Refactor and test different weapon types and interactions. Add more weapon types or features like auto-aim or weapon upgrades.
"""

from random import randint, choice
from model.weapon_related.cooldown import Cooldown

class Weapons:
    """
    A class to represent the weapons a shooter can use.

    This class includes the configuration of different weapon types, handling of ammunition, cooldowns for shooting,
    reloading, and rafale (burst) shooting mechanics. It also includes methods to upgrade weapon characteristics.
    """

    def __init__(self, shooter, type, projectile_class, projectile_image):
        """
        Initialize the weapon with the given parameters.

        Args:
            shooter (Shooter): The shooter object that will use the weapon.
            type (list): The type of the weapon, including both the main type and special modifiers.
            projectile_class (Projectile): The class responsible for creating projectiles fired by the weapon.
            projectile_image (Image): The image used to represent the projectile.
        """
        self.shooter = shooter
        self.type = type
        refresh_rate = shooter.refresh_rate

        # Initialize cooldowns for different weapon types
        self.cooldown = Cooldown(100, refresh_rate, 0)
        self.cooldown_reload = Cooldown(100, refresh_rate, 0)
        self.cooldown_rafale = Cooldown(100, refresh_rate, 0)

        # Default weapon attributes
        self.damage = 0
        self.power = 0
        self.imprecision = 0
        self.rafale = 0
        self.munitions = 0
        self.projectile_width = 0
        self.projectile_height = 0

        # Setup weapon types
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
        
        # Alien or bonus weapon modifications
        if type[1] == "alien":
            self.imprecision += 2
            self.damage = 1
            self.munitions = 1000   # Unlimited ammunition for aliens
            self.cooldown.change(3000)
            self.cooldown_rafale.add_offset(randint(0, 3000))
            self.cooldown.add_offset(randint(0, 3000))
            if type[0] == "machine_gun":       # Aliens have modified machine guns with higher burst rate
                self.rafale = 5

        elif type[1] == "bonus":
            self.cooldown = Cooldown(125, refresh_rate, 0)
            self.munitions = 1000

        self.projectile_class = projectile_class
        self.projectile_image = projectile_image
        self.current_rafale = 0
        self.current_munitions = self.munitions
        self.reloading = False
        self.auto_reload = False

    def shoot(self):
        """
        Fire a projectile from the weapon. It handles rafale (burst) firing, cooldown, and ammunition checks.

        This method checks if the weapon is ready to shoot, takes the current shooter position, and fires the
        projectile while adjusting for any imprecision. It reduces the ammunition accordingly and manages cooldown.
        """
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
        """
        Reload the weapon's ammunition. It checks if the weapon is not already reloading and if the cooldown for reloading is done.

        This method resets the ammunition count to the maximum when reloading is finished.
        """
        if self.current_munitions < self.munitions:
            self.reloading = True
            if self.reloading and self.cooldown_reload.ended():
                self.current_munitions = self.munitions
                self.reloading = False
                self.cooldown_reload.reset()
    
    def upgrade_cooldown(self):
        """
        Upgrade the cooldown time to make it faster. This method decreases the cooldown by 30.
        """
        if self.cooldown.time > 30:
            self.cooldown.change(self.cooldown.time - 30)
    
    def upgrade_cooldown_reload(self):
        """
        Upgrade the reload cooldown to make it faster. This method decreases the reload cooldown by 50.
        """
        if self.cooldown_reload.time > 50:
            self.cooldown_reload.change(self.cooldown_reload.time - 50)
    
    def upgrade_damage(self):
        """
        Upgrade the damage of the weapon. For aliens or machine guns, the damage is upgraded more significantly.
        """
        if self.type[1] == "alien" or self.type[0] == "machine_gun":
            self.damage += 0.5
        self.damage += 1
    
    def upgrade_power(self):
        """
        Increase the power of the weapon.
        """
        self.power += 2
    
    def upgrade_imprecision(self):
        """
        Decrease the imprecision of the weapon, making it more accurate.
        """
        if self.imprecision >= 0.3:
            self.imprecision -= 0.3
    
    def upgrade_rafale(self):
        """
        Increase the number of shots in a burst (rafale).
        """
        self.rafale += 1
    
    def upgrade_munitions(self):
        """
        Increase the maximum ammunition capacity of the weapon.
        """
        self.munitions += 3
    
    def upgrade_one_caracteristic(self, caracteristic):
        """
        Upgrade a specific characteristic of the weapon.

        Args:
            caracteristic (str): The characteristic to upgrade (e.g., "cooldown", "damage", "power", etc.).
        """
        if caracteristic == "cooldown":
            self.upgrade_cooldown()
        elif caracteristic == "cooldown_reload":
            self.upgrade_cooldown_reload()
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
        elif caracteristic == "auto_reload":
            self.auto_reload = True

    def update(self):
        """
        Update the cooldowns and handle actions like reloading or shooting in rafale mode.

        This method manages the cooldowns and the automatic reloading if the current ammunition reaches 0 and auto_reload is enabled.
        """
        self.cooldown_rafale.update()
        if self.rafale == 1 or self.current_rafale == self.rafale:
            self.cooldown.update()
            if self.cooldown.ended() and self.current_rafale == self.rafale:
                    self.current_rafale = 0
                    self.cooldown.reset()

        if self.current_munitions == 0 and self.auto_reload:
            self.reload()

        if 0 < self.current_rafale:     # If the player starts a rafale, it automatically finishes
            self.shoot()

        if self.reloading:
            self.cooldown_reload.update()
            if self.cooldown_reload.ended():
                self.reloading = False
                self.current_munitions = self.munitions
                self.current_rafale = 0
                self.cooldown_reload.reset()
    
    def reset(self):
        """
        Reset the weapon to its initial state, clearing ammunition and resetting cooldowns.

        This method is typically used when the weapon is switched or the game is restarted.
        """
        self.current_rafale = 0
        self.current_munitions = self.munitions
        self.reloading = False
        self.cooldown.reset()
        self.cooldown_reload.reset()
        self.cooldown_rafale.reset()
