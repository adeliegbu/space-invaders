# -*- coding: utf-8 -*-
"""
File: group_object.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: Implementation of the Group_object class, managing collections of objects and their interactions in the Space Invaders game.

TODO:
- Add advanced collision handling (e.g., multi-hit detection).
- Optimize object matrix management for large-scale gameplay.
"""

class Group_object:
    """Manages a collection of game objects, including their creation, movement, and interactions."""

    def __init__(self, canvas, refresh_rate):
        """
        Initialize the Group_object.

        Args:
            canvas: The canvas on which objects are drawn.
            refresh_rate (int): The refresh rate for object updates.
        """
        self.canvas = canvas
        self.refresh_rate = refresh_rate
        self.objects_list = []
        self.objects_matrix = []

    def create_objects_matrix(self, object_class, x, y, line, column, pad_x, pad_y, image, **kwargs):
        """
        Create a matrix of objects.

        Args:
            object_class: The class of objects to create.
            x (int): Initial x-coordinate for the matrix center.
            y (int): Initial y-coordinate for the matrix center.
            line (int): Number of rows in the matrix.
            column (int): Number of columns in the matrix.
            pad_x (int): Horizontal padding between objects.
            pad_y (int): Vertical padding between objects.
            image: The image for the objects.
            **kwargs: Additional arguments for object initialization.
        """
        for j in range(- column // 2 + 1, column // 2 + 1):
            row = []
            for i in range(line):
                temporary = object_class(self.canvas, 0, 0, image, refresh_rate=self.refresh_rate, **kwargs)
                new_object = object_class(
                    self.canvas,
                    x + j * (temporary.width + pad_x),
                    y + i * (temporary.height + pad_y),
                    image,
                    refresh_rate=self.refresh_rate,
                    **kwargs
                )
                temporary.delete()
                row.append(new_object)
            self.objects_matrix.append(row)

    def add_object(self, object):
        """Add an object to the list of objects."""
        self.objects_list.append(object)

    def move_objects_matrix(self, x_direction, y_direction):
        """Move all objects in the matrix in the specified direction."""
        for row in self.objects_matrix:
            for object in row:
                object.move(x_direction, y_direction)

    def move_objects_list(self, x_direction, y_direction):
        """Move all objects in the list in the specified direction."""
        for object in self.objects_list:
            object.move(x_direction, y_direction)

    def got_hit(self, object, damage):
        """
        Apply damage to an object and remove it if it's destroyed.

        Args:
            object: The object receiving damage.
            damage (int): The amount of damage to apply.
        """
        object.got_hit(damage)
        if object.dead():
            self.remove_object(object)

    def collision(self, targets):
        """
        Check for collisions between objects in this group and another group.

        Args:
            targets: The target group to check collisions against.

        Returns:
            tuple: (collision_occurred, target, object) indicating if a collision occurred and the involved objects.
        """
        for object in self.objects_list:
            for target in targets.objects_list:
                if object.collide(target):
                    self.got_hit(object, target.damage)
                    targets.got_hit(target, object.damage)
                    return True, target, object
            for row in targets.objects_matrix:
                for target in row:
                    if object.collide(target):
                        self.got_hit(object, target.damage)
                        targets.got_hit(target, object.damage)
                        return True, target, object

        for row in self.objects_matrix:
            for object in row:
                for target in targets.objects_list:
                    if object.collide(target):
                        self.got_hit(object, target.damage)
                        targets.got_hit(target, object.damage)
                        return True, target, object
                for row_target in targets.objects_matrix:
                    for target in row_target:
                        if object.collide(target):
                            self.got_hit(object, target.damage)
                            targets.got_hit(target, object.damage)
                            return True, target, object
        return False, None, None

    def objects_dead(self):
        """
        Check if all objects in the group are destroyed.

        Returns:
            bool: True if all objects are destroyed, False otherwise.
        """
        return not self.objects_list and all(not row for row in self.objects_matrix)

    def remove_object(self, object):
        """
        Remove an object from the group.

        Args:
            object: The object to remove.
        """
        if object in self.objects_list:
            self.objects_list.remove(object)
            object.delete()
        for row in self.objects_matrix:
            if object in row:
                row.remove(object)
                object.delete()
                break

    def reset(self):
        """Reset the group, deleting all objects."""
        for object in self.objects_list:
            object.delete()
        self.objects_list = []
        for row in self.objects_matrix:
            for object in row:
                object.delete()
        self.objects_matrix = []