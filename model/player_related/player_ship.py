# -*- coding: utf-8 -*-
"""
File Name: player_ship.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: Defines the PlayerShip class, a specialized Ship controlled by the player in the Space Invaders game.

TODO:
- Implement player-specific abilities or power-ups.
- Add visual effects for movement and shooting.
"""

from model.parents_class.ship import Ship

class Player_ship(Ship):
    """
    A PlayerShip class that represents the player's controllable ship.

    Attributes:
        Inherits all attributes from the Ship class.
    """

    def __init__(self, canvas, x, y, image, refresh_rate, projectile_class, projectile_image):
        """
        Initializes the PlayerShip with predefined speed, size, and life attributes.

        Args:
            canvas: The canvas on which the ship is drawn.
            x: Initial x-coordinate of the player ship.
            y: Initial y-coordinate of the player ship.
            image: Image representing the player ship.
            refresh_rate: The refresh rate for the game loop.
            projectile_class: The class of projectiles fired by the player ship.
            projectile_image: The image of the projectiles fired by the player ship.
        """
        super().__init__(
            canvas, x, y, x_speed=13, y_speed=0, width=60, height=40, 
            life=5, damage=1, image=image, refresh_rate=refresh_rate, 
            projectile_class=projectile_class, projectile_image=projectile_image
        )
    
    def left(self):
        """
        Moves the player ship to the left.

        Returns:
            None
        """
        return super().move(-1, 0)
        
    def right(self):
        """
        Moves the player ship to the right.

        Returns:
            None
        """
        return super().move(1, 0)
    
    def change_weapon(self, wepon_type):
        """
        Changes the player ship's weapon to a new type.

        Args:
            wepon_type: The type of weapon to equip.

        Returns:
            None
        """
        super().change_weapon(wepon_type, "player")

    def become_doctor(self):
        """
        Placeholder method for compatibility; no action required for the player ship.

        Returns:
            None
        """
        return None