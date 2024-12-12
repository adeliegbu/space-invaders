# -*- coding: utf-8 -*-
"""
File Name: projectile.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Projectile class, which is a subclass of the Object class.
             It represents a projectile with specific attributes such as speed, size, damage, and image.

TODO: Implement more projectile behaviors such as collision detection and interaction with objects.
"""

from model.parents_class.object import Object

class Projectile(Object):
    """
    A class to represent a projectile.

    Inherits from the Object class and adds specific behaviors related to projectiles, 
    including initializing attributes like position, speed, size, damage, and image.
    """

    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, damage, image, refresh_rate):
        """
        Initialize the Projectile object.

        Args:
            canvas (object): The canvas where the projectile is drawn.
            x (int): The x-coordinate of the projectile's starting position.
            y (int): The y-coordinate of the projectile's starting position.
            x_speed (int): The speed of the projectile along the x-axis.
            y_speed (int): The speed of the projectile along the y-axis.
            width (int): The width of the projectile.
            height (int): The height of the projectile.
            damage (int): The damage caused by the projectile.
            image (str): Path to the image representing the projectile.
            refresh_rate (int): The rate at which the projectile is refreshed.
        """
        super().__init__(canvas, x, y, x_speed=x_speed, y_speed=y_speed, width=width, height=height, life=1, damage=damage, image=image, refresh_rate=refresh_rate)
