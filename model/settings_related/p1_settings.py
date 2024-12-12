# -*- coding: utf-8 -*-
"""
File Name: p1_settings.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the P1_settings class, which is a subclass of Settings.
             It handles the settings for Player 1, including selecting images for the player and projectiles,
             as well as handling upgrades.

TODO: Implement behavior for handling upgrade points and player customization.
"""

from model.settings_related.settings import Settings

class P1_settings(Settings):
    """
    A class to represent the settings for Player 1.

    Inherits from the Settings class and provides methods for accessing and updating
    player-specific settings like selecting player images, projectile images, and handling upgrades.
    """

    def __init__(self, view):
        """
        Initialize the P1_settings object with a reference to the view.

        Args:
            view (object): The view object that holds images for the player and projectiles.
        """
        super().__init__(view)

    def get_choiced_player1_image(self):
        """
        Get the image currently selected for Player 1.

        Returns:
            str: The image representing Player 1.
        """
        return self.view.player_images[self.choiced_index]

    def get_choiced_player1_projectile_image(self):
        """
        Get the image currently selected for Player 1's projectile.

        Returns:
            str: The image representing Player 1's projectile.
        """
        return self.view.projectile_player_images[self.choiced_index]

    def next_upgrade(self):
        """
        Get the next upgrade points available for Player 1.

        Returns:
            int: The number of upgrade points Player 1 has.
        """
        return self.controller.upgrade_points
