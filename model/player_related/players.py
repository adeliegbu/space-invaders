# -*- coding: utf-8 -*-
"""
File Name: players.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: Defines the Players class, managing a group of PlayerShip instances in the Space Invaders game.

TODO:
- Add methods for handling player-specific events.
- Implement additional logic for cooperative gameplay.
"""

from model.player_related.player_ship import Player_ship
from model.parents_class.group_object import Group_object
from model.weapon_related.weapons import Weapons

class Players(Group_object):
    """
    A Players class to manage multiple PlayerShip objects.

    Attributes:
        canvas: The canvas on which players are drawn.
        refresh_rate: The refresh rate for the game loop.
        projectille_class: The class used for creating projectiles.
    """

    def __init__(self, canvas, refresh_rate, projectille_class):
        """
        Initializes the Players group.

        Args:
            canvas: The canvas for rendering players.
            refresh_rate: The game's refresh rate.
            projectille_class: The class used for player projectiles.
        """
        super().__init__(canvas, refresh_rate)
        self.projectille_class = projectille_class

    def add_object(self, x, y, image, projectile_image, weapon_type):
        """
        Adds a new player to the group.

        Args:
            x: The x-coordinate for the new player.
            y: The y-coordinate for the new player.
            image: The image representing the player.
            projectile_image: The image of the player's projectiles.
            weapon_type: The type of weapon assigned to the player.

        Returns:
            None
        """
        new_player = Player_ship(self.canvas, x, y, image, self.refresh_rate, self.projectille_class, projectile_image)
        new_player.weapon = Weapons(new_player, (weapon_type, "player"), self.projectille_class, projectile_image)
        super().add_object(new_player)
    
    def define_player(self, player_number):
        """
        Retrieves a player based on their number.

        Args:
            player_number: The index of the player to retrieve.

        Returns:
            Player_ship instance or None if the number is invalid.
        """
        if player_number <= len(self.objects_list):
            return self.objects_list[player_number - 1]
        return None

    def update_weapons(self):
        """
        Updates all player weapons.

        Returns:
            None
        """
        for player in self.objects_list:
            player.weapon.update()
    
    def reset_weapons(self):
        """
        Resets all player weapons to their default state.

        Returns:
            None
        """
        for player in self.objects_list:
            player.weapon.reset()
