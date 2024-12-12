# -*- coding: utf-8 -*-
"""
File: alien_ship.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: Implementation of the AlienShip class, inheriting from the Ship parent class. 
             The class handles alien-specific attributes and behaviors, such as level progression,
             weapon upgrades, and unique abilities.

TODO:
- Add more alien types with distinct behaviors.
- Optimize the `increase_level` method for scalability.
- Improve documentation for inherited methods.
"""

from random import choice, choices

from model.parents_class.ship import Ship

class Alien_ship(Ship):
    """Represents an alien ship, inheriting from the Ship class."""

    def __init__(self, canvas, x, y, image, refresh_rate, projectile_class, projectile_image):
        """
        Initialize an alien ship instance.

        Args:
            canvas: The canvas on which the ship will be drawn.
            x (int): The x-coordinate of the ship.
            y (int): The y-coordinate of the ship.
            image: The image representing the ship.
            refresh_rate (int): The refresh rate of the ship's actions.
            projectile_class: The class of projectiles the ship can shoot.
            projectile_image: The image for the ship's projectiles.
        """
        super().__init__(
            canvas, x, y,
            x_speed=5, y_speed=25,
            width=40, height=25,
            life=1, damage=1,
            image=image,
            refresh_rate=refresh_rate,
            projectile_class=projectile_class,
            projectile_image=projectile_image
        )
        self.level = 0
        self.type = None

    def change_weapon(self, wepon_type):
        """
        Change the alien's weapon to the specified type.

        Args:
            wepon_type (str): The type of weapon to assign.
        """
        super().change_weapon(wepon_type, "alien")

    def increase_level(self):
        """
        Increase the level of the alien ship, upgrading its characteristics.
        At level 1, assigns a random weapon type. Upgrades characteristics
        based on level milestones.
        """
        self.level += 1

        if self.level == 1:
            # Initialize the alien's weapon starting from level 1.
            self.type = choice(["assault", "rafale", "machine_gun", "sniper", "tank"])
            self.change_weapon(self.type)

        if self.level % 2 == 0:
            super().upgrade_one_caracteristic("life")

        upgrade_choiced = choices(
            ["cooldown", "cooldown_rafale", "damage", "power", "rafale"],
            [0.4, 0.1, 0.1, 0.3, 0.1],
            k=1
        )[0]
        super().upgrade_one_caracteristic(upgrade_choiced)

    def become_doctor(self):
        """Set the alien ship's type to 'doctor'."""
        self.type = "doctor"

    def dead(self):
        """
        Check if the alien ship is dead.

        Returns:
            bool: True if the ship is dead, False otherwise.
        """
        if super().dead():
            return True