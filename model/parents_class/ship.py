# -*- coding: utf-8 -*-
"""
File Name: ship.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: Defines the Ship class, a specialized Object that includes weapon functionality for shooting,
             upgrading characteristics, and changing weapons. This class is used as a base for implementing
             different types of ships in the Space Invaders game.

TODO:
- Implement additional ship types with unique characteristics.
- Add more weapon types to enhance gameplay variety.
"""

from model.parents_class.object import Object
from model.weapon_related.weapons import Weapons

class Ship(Object):
    """
    A Ship class that represents a game object capable of shooting and using weapons.

    Attributes:
        weapon: The weapon currently equipped on the ship.
        projectile_class: Class of projectiles used by the weapon.
        projectile_image: Image of the projectiles used by the weapon.
    """

    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, life, damage, image, refresh_rate, projectile_class, projectile_image):
        """
        Initializes a Ship object with movement attributes, life, damage, and weapon configuration.

        Args:
            canvas: The canvas on which the ship is drawn.
            x: Initial x-coordinate of the ship.
            y: Initial y-coordinate of the ship.
            x_speed: Speed of the ship along the x-axis.
            y_speed: Speed of the ship along the y-axis.
            width: Width of the ship.
            height: Height of the ship.
            life: Initial life of the ship.
            damage: Damage dealt by the ship.
            image: Image representing the ship.
            refresh_rate: The refresh rate for the game loop.
            projectile_class: The class of projectiles fired by the ship.
            projectile_image: The image of the projectiles fired by the ship.
        """
        super().__init__(canvas, x, y, x_speed, y_speed, width, height, life, damage, image, refresh_rate)
        self.weapon = None
        self.projectile_class = projectile_class
        self.projectile_image = projectile_image

    def shoot(self):
        """
        Triggers the ship to shoot using its equipped weapon.
        """
        if self.weapon is not None:
            self.weapon.shoot()
    
    def change_weapon(self, wepon_type, shooter_type):
        """
        Changes the ship's weapon to a new type.

        Args:
            wepon_type: The type of weapon to equip.
            shooter_type: The type of shooter (e.g., "alien", "player").
        """
        self.weapon = Weapons(self, (wepon_type, shooter_type), self.projectile_class, self.projectile_image)

    def update_weapon(self):
        """
        Updates the current weapon's state (e.g., reloading, cooldown).
        """
        self.weapon.update()
    
    def upgrade_one_caracteristic(self, caracteristic):
        """
        Upgrades a specific characteristic of the ship or its weapon.

        Args:
            caracteristic: The characteristic to upgrade (e.g., "life", "speed", weapon-related attributes).
        """
        if caracteristic == "life":
            self.life += 1
        elif caracteristic == "speed":
            self.x_speed += 1
        else:
            self.weapon.upgrade_one_caracteristic(caracteristic)
