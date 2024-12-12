# -*- coding: utf-8 -*-
"""
File Name: players_projectiles.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Players_projectiles class, which is a subclass of Projectiles.
             It adds specific behaviors related to player projectiles such as adding and moving objects.
             
TODO: Add more detailed player-specific behaviors for projectiles if needed.
"""

from model.projectile_related.projectiles import Projectiles

class Players_projectiles(Projectiles):
    """
    A class to represent the player projectiles.

    Inherits from the Projectiles class and adds functionalities
    specific to the player projectiles, including adding objects and
    moving projectiles upwards.
    """

    def __init__(self, canvas, refresh_rate):
        """
        Initialize the Players_projectiles object.

        Args:
            canvas (object): The canvas where projectiles are drawn.
            refresh_rate (int): The rate at which the projectiles are refreshed.
        """
        super().__init__(canvas, refresh_rate)

    def add_object(self, x, y, height, imprecision, power, projectile_width, projectile_height, damage, projectile_image):
        """
        Add a projectile object to the game.

        This method calls the parent class's add_object method to create a projectile
        at the specified position with the given attributes.

        Args:
            x (int): The x-coordinate of the projectile's starting position.
            y (int): The y-coordinate of the projectile's starting position.
            height (int): The height of the projectile.
            imprecision (float): The imprecision factor affecting the projectile's trajectory.
            power (float): The power of the projectile.
            projectile_width (int): The width of the projectile.
            projectile_height (int): The height of the projectile.
            damage (int): The damage the projectile causes.
            projectile_image (str): Path to the image representing the projectile.
        """
        super().add_object(x, y - height, imprecision, power, projectile_width, projectile_height, damage, projectile_image)

    def move(self):
        """
        Move the projectile upwards.

        This method calls the parent class's move method, setting the y-direction
        to -1 to move the projectile upwards.
        """
        super().move(y_direction=-1)
