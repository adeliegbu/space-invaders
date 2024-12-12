# -*- coding: utf-8 -*-
"""
File Name: walls.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Walls class, which is a subclass of Group_object.
             It represents a collection of brick objects arranged to form walls in the game.

TODO: Implement behavior for handling brick destruction, collision detection, and interaction with other game elements.
"""

from model.wall_related.brick import Brick
from model.parents_class.group_object import Group_object

class Walls(Group_object):
    """
    A class to represent walls in the game made of bricks.

    Inherits from the Group_object class and manages a collection of Brick objects arranged in a matrix.
    It provides methods to create the wall's structure and add additional bricks in the environment.
    """

    def __init__(self, canvas, refresh_rate, image):
        """
        Initialize the Walls object with the canvas, refresh rate, and image for the bricks.

        Args:
            canvas (object): The canvas where the walls will be rendered.
            refresh_rate (int): The rate at which the walls and bricks are refreshed.
            image (str): The image representing the brick.
        """
        super().__init__(canvas, refresh_rate=refresh_rate)
        self.image = image

    def create_objects_matrix(self, x, y):
        """
        Create a matrix of brick objects at the specified position.

        Args:
            x (int): The x-coordinate of the wall's starting position.
            y (int): The y-coordinate of the wall's starting position.
        
        This method creates a grid of bricks with 3 rows and 5 columns and adds border bricks at the edges.
        """
        super().create_objects_matrix(Brick, x, y, line=3, column=5, pad_x=0, pad_y=0, image=self.image)
        temporary = Brick(self.canvas, 0, 0, image=self.image, refresh_rate=0)
        border_bricks = [Brick(self.canvas, x - 3 * temporary.width, y + temporary.height, image=self.image, refresh_rate=0),
                         Brick(self.canvas, x + 3 * temporary.width, y + temporary.height, image=self.image, refresh_rate=0)]
        temporary.delete()
        self.objects_matrix.append(border_bricks)
    
    def add_object(self, y, number):
        """
        Add a number of wall sections at different x-positions along the given y-coordinate.

        Args:
            y (int): The y-coordinate where the walls will be added.
            number (int): The number of wall sections to create.
        
        This method evenly distributes the walls along the x-axis based on the number specified.
        """
        for i in range(number):
            self.create_objects_matrix(self.canvas.winfo_screenwidth() * (i + 1) // (number + 1), y)
