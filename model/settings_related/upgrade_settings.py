# -*- coding: utf-8 -*-
"""
File Name: upgrade_settings.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Upgrade_settings class, which is a subclass of Settings.
             It manages the upgrade options for the game, including upgrade categories and their associated prices.

TODO: Implement behavior for handling upgrade transactions and ensuring the player has enough resources for upgrades.
"""

from model.settings_related.settings import Settings

class Upgrade_settings(Settings):
    """
    A class to represent the settings related to upgrades.

    Inherits from the Settings class and manages the upgrade options available for the player,
    including the upgrade categories and the corresponding prices for each upgrade.
    """

    def __init__(self):
        """
        Initialize the Upgrade_settings object with predefined upgrade options and their prices.

        The available upgrade options include:
            - cooldown, cooldown_reload, damage, power, rafale, imprecision,
              munitions, speed, life, auto_reload
        And each upgrade has a predefined price.
        """
        super().__init__(["cooldown", "cooldown_reload", "damage", "power", "rafale", "imprecision", "munitions", "speed", "life", "auto_reload"])
        self.upgrade_prices = [2, 1, 4, 2, 5, 2, 3, 1, 7, 3]

    def choiced_price(self):
        """
        Get the price of the currently selected upgrade.

        Returns:
            int: The price of the selected upgrade option.
        """
        return self.upgrade_prices[self.choiced_index]
