# -*- coding: utf-8 -*-
"""
File: bonus_ship.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: Implementation of the Bonus_ship class, a specialized ship type that provides bonuses in the game.

TODO:
- Implement additional bonus effects.
- Add animations for bonus ship entry and exit.
"""

from model.parents_class.ship import Ship

class Bonus_ship(Ship):
    """Represents a bonus ship that moves across the screen and provides special bonuses."""

    def __init__(self, canvas, x, y, image, direction, refresh_rate, projectile_class, projectile_image):
        """
        Initialize the Bonus_ship.

        Args:
            canvas: The canvas on which the bonus ship will be drawn.
            x (int): The x-coordinate of the bonus ship.
            y (int): The y-coordinate of the bonus ship.
            image: The image representing the bonus ship.
            direction (int): Direction of the ship's movement (-1 for left, 1 for right).
            refresh_rate (int): The refresh rate for the ship's actions.
            projectile_class: Class representing projectiles fired by the ship.
            projectile_image: The image for the projectiles.
        """
        super().__init__(
            canvas, x, y, x_speed=17, y_speed=0, width=60, height=35, life=1, damage=0,
            image=image, refresh_rate=refresh_rate, projectile_class=projectile_class,
            projectile_image=projectile_image
        )
        self.direction = direction
        self.type = "bonus"
        self.level = 20
        self.change_weapon()

    def change_weapon(self):
        """Set the bonus ship's weapon to an assault type."""
        super().change_weapon("assault", "bonus")

    def move(self):
        """Move the bonus ship in its designated direction."""
        super().move(self.direction, 0)

    def bonus_will_be_out_of_bounds(self):
        """
        Check if the bonus ship will move out of bounds.

        Returns:
            bool: True if the ship will go out of bounds, False otherwise.
        """
        return super().will_be_out_of_bounds(self.direction, 0)
