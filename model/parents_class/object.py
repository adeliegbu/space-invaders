# -*- coding: utf-8 -*-
"""
File: object.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: Implementation of the Object class, representing a generic object in the Space Invaders game.

TODO:
- Enhance collision detection for rotated or irregularly shaped objects.
- Implement advanced movement patterns.
"""

class Object:
    """Represents a generic object in the game, with position, size, and behavior."""

    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, life, damage, image, refresh_rate):
        """
        Initialize the Object.

        Args:
            canvas: The canvas on which the object is drawn.
            x (int): Initial x-coordinate of the object.
            y (int): Initial y-coordinate of the object.
            x_speed (int): Speed of the object along the x-axis.
            y_speed (int): Speed of the object along the y-axis.
            width (int): Width of the object.
            height (int): Height of the object.
            life (int): Life points of the object.
            damage (int): Damage the object can inflict.
            image: Image representation of the object.
            refresh_rate (int): Refresh rate for object updates.
        """
        self.canvas = canvas
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.width = width
        self.height = height
        self.life = life
        self.damage = damage
        self.image = image
        self.refresh_rate = refresh_rate
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor="center")

    def get_position(self):
        """Get the current position of the object."""
        return self.x, self.y

    def get_dimensions(self):
        """Get the dimensions of the object."""
        return self.width, self.height

    def change_image(self, image):
        """
        Change the image of the object.

        Args:
            image: The new image for the object.
        """
        self.delete()
        self.id = self.canvas.create_image(self.x, self.y, image=image, anchor="center")

    def collide(self, object):
        """
        Check if this object collides with another object.

        Args:
            object: The other object to check collision with.

        Returns:
            bool: True if a collision occurs, False otherwise.
        """
        x1, y1 = self.get_position()
        x2, y2 = object.get_position()
        w1, h1 = self.get_dimensions()
        w2, h2 = object.get_dimensions()
        return (
            x1 - w1 // 2 <= x2 + w2 // 2 and
            x1 + w1 // 2 >= x2 - w2 // 2 and
            y1 - h1 // 2 <= y2 + h2 // 2 and
            y1 + h1 // 2 >= y2 - h2 // 2
        )

    def will_be_out_of_bounds(self, x_direction, y_direction):
        """
        Check if the object will move out of bounds in the next step.

        Args:
            x_direction (int): Direction along the x-axis.
            y_direction (int): Direction along the y-axis.

        Returns:
            bool: True if the object will move out of bounds, False otherwise.
        """
        x_future = self.x + x_direction * self.x_speed
        y_future = self.y + y_direction * self.y_speed
        return (
            x_future - self.width // 2 <= 0 or
            x_future + self.width // 2 >= self.canvas.winfo_width() or
            y_future - self.height // 2 <= 0 or
            y_future + self.height // 2 >= self.canvas.winfo_height()
        )

    def move(self, x_direction, y_direction):
        """
        Move the object in the specified direction.

        Args:
            x_direction (int): Direction along the x-axis.
            y_direction (int): Direction along the y-axis.
        """
        if not self.will_be_out_of_bounds(x_direction, y_direction):
            self.x += x_direction * self.x_speed
            self.y += y_direction * self.y_speed
            self.canvas.move(self.id, x_direction * self.x_speed, y_direction * self.y_speed)

    def got_hit(self, damage):
        """
        Apply damage to the object.

        Args:
            damage (int): Amount of damage to apply.
        """
        self.life -= damage

    def dead(self):
        """Check if the object is dead."""
        return self.life <= 0
    
    def delete(self):
        """Delete the object from the canvas."""
        self.canvas.delete(self.id)