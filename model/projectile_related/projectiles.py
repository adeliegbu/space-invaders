# -*- coding: utf-8 -*-
"""
File Name: projectiles.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Projectiles class, which is a subclass of Group_object.
             It handles a collection of projectile objects, adding them, moving them, and checking if they go out of bounds.

TODO: Implement additional logic for handling interactions between projectiles and other game elements.
"""

from model.projectile_related.projectile import Projectile
from model.parents_class.group_object import Group_object

class Projectiles(Group_object):
    """
    A class to represent a group of projectiles.

    Inherits from the Group_object class and adds specific behaviors related to managing
    projectiles such as adding projectiles, moving them, and removing those that go out of bounds.
    """

    def __init__(self, canvas, refresh_rate):
        """
        Initialize the Projectiles object.

        Args:
            canvas (object): The canvas where projectiles are drawn.
            refresh_rate (int): The rate at which the projectiles are refreshed.
        """
        super().__init__(canvas, refresh_rate)

    def add_object(self, x, y, imprecision, power, projectile_width, projectile_height, damage, projectile_image):
        """
        Add a projectile to the group.

        This method creates a new Projectile object and adds it to the list of projectiles.

        Args:
            x (int): The x-coordinate of the projectile's starting position.
            y (int): The y-coordinate of the projectile's starting position.
            imprecision (float): The imprecision factor affecting the projectile's trajectory.
            power (float): The power of the projectile.
            projectile_width (int): The width of the projectile.
            projectile_height (int): The height of the projectile.
            damage (int): The damage the projectile causes.
            projectile_image (str): Path to the image representing the projectile.
        """
        super().add_object(Projectile(self.canvas, x, y, imprecision, power, projectile_width, projectile_height, damage, projectile_image, self.refresh_rate))
    
    def move(self, y_direction):
        """
        Move the projectiles in the specified direction.

        This method moves all projectiles in the list by calling the parent class's move_objects_list method.
        It also checks if any projectiles will be out of bounds and removes them.

        Args:
            y_direction (int): The direction in which to move the projectiles along the y-axis.
        """
        super().move_objects_list(1, y_direction)
        self.projectiles_will_be_out_of_bounds(y_direction)
    
    def projectiles_will_be_out_of_bounds(self, y_direction):
        """
        Remove projectiles that are about to go out of bounds.

        This method iterates through all projectiles and removes any that will go out of bounds
        in the specified direction.

        Args:
            y_direction (int): The direction to check for projectiles going out of bounds.
        """
        for projectile in self.objects_list:
            if projectile.will_be_out_of_bounds(1, y_direction):
                super().remove_object(projectile)
