# -*- coding: utf-8 -*-
"""
File Name: brick.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Brick class, which is a subclass of the Object class.
             It represents a brick object in the game with properties such as position, size, and image.

TODO: Implement additional behavior for handling brick interactions (e.g., destruction or collision).
"""

from model.parents_class.object import Object

class Brick(Object):
    """
    A class to represent a brick object.

    Inherits from the Object class and initializes a brick with predefined properties such as size, 
    speed, life, and image. This brick can be used as part of a game environment (e.g., for breaking bricks in a game).
    """

    def __init__(self, canvas, x, y, image, refresh_rate):
        """
        Initialize the Brick object with position, image, and other properties.

        Args:
            canvas (object): The canvas where the brick will be rendered.
            x (int): The x-coordinate of the brick's position.
            y (int): The y-coordinate of the brick's position.
            image (str): The path to the image representing the brick.
            refresh_rate (int): The rate at which the brick is refreshed.
        """
        super().__init__(canvas, x, y, x_speed=0, y_speed=0, width=20, height=20, life=1, damage=1, image=image, refresh_rate=refresh_rate)
