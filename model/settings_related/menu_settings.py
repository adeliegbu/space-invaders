# -*- coding: utf-8 -*-
"""
File Name: menu_settings.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Menu_settings class, which is a subclass of Settings.
             It represents the settings menu with specific options like starting a new game, viewing rules, adjusting options, or quitting.

TODO: Implement behavior for handling user selection from the menu options.
"""

from model.settings_related.settings import Settings

class Menu_settings(Settings):
    """
    A class to represent the settings menu.

    Inherits from the Settings class and initializes the menu with specific options such as
    starting a new game, viewing rules, adjusting options, or quitting.
    """

    def __init__(self):
        """
        Initialize the Menu_settings object with predefined menu options.

        The options include:
            - Nouvelle Partie
            - Règles
            - Options
            - Quitter
        """
        super().__init__(options=["Nouvelle Partie", "Règles", "Options", "Quitter"])
