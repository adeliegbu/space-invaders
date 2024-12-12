# -*- coding: utf-8 -*-
"""
File Name: aliens_projectiles.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Aliens_projectiles class, which manages projectiles launched by alien ships in the game. It inherits from the Projectiles class and implements specific behavior for alien projectiles.

TODO:
- Add collision detection with player ships.
- Implement different projectile types for alien ships.
"""

from model.projectile_related.projectiles import Projectiles

class Aliens_projectiles(Projectiles):
    """Manages projectiles launched by alien ships in the game."""

    def __init__(self, canvas, refresh_rate):
        """Initialize an Aliens_projectiles instance.

        Args:
            canvas: The canvas object where projectiles are drawn.
            refresh_rate: The refresh rate for updating projectile movements.
        """
        super().__init__(canvas, refresh_rate)
    
    def add_object(self, x, y, height, imprecision, power, projectile_width, projectile_height, damage, projectile_image):
        """Add a new projectile to the game.

        Args:
            x: The x-coordinate of the projectile's initial position.
            y: The y-coordinate of the projectile's initial position.
            height: The height of the projectile's source (alien ship).
            imprecision: The imprecision factor for the projectile's trajectory.
            power: The power (speed) of the projectile.
            projectile_width: The width of the projectile.
            projectile_height: The height of the projectile.
            damage: The damage caused by the projectile on impact.
            projectile_image: The image representing the projectile.
        """
        super().add_object(x, y + height, imprecision, power, projectile_width, projectile_height, damage, projectile_image)
    
    def move(self):
        """Move all projectiles downward on the canvas."""
        super().move(y_direction=1)
