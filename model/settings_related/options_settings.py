# -*- coding: utf-8 -*-
"""
File Name: options_settings.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Options_settings class, which is a subclass of Settings.
             It manages the options available for the game settings, including modes, levels, classes, skins, and controls.

TODO: Implement methods to handle user input for changing settings options and saving the configurations.
"""

from model.settings_related.settings import Settings

class Options_settings(Settings):
    """
    A class to represent the options menu for game settings.

    Inherits from the Settings class and initializes the settings menu with options for different categories:
    - Game mode (solo, coop)
    - Difficulty level (easy, ranked, défi)
    - Character class (assault, rafale, etc.)
    - Skin colors (green, red, etc.)
    - Key bindings (left, right, reload, shoot)
    """

    def __init__(self):
        """
        Initialize the Options_settings object with predefined options for each category.

        The categories include:
            - mode: solo, coop
            - level: easy, ranked, défi
            - class: assault, rafale, mitraille, tank, sniper
            - skin: green, red, blue, yellow, pink, grey
            - binds: left, right, reload, shoot
        """
        super().__init__([["solo", "coop"], ["easy", "ranked", "defi"], ["assault", "rafale", "mitraillette", "tank", "sniper"], ["green", "blue", "red", "yellow", "pink"], ["left", "right", "reload", "shoot"]])
        self.categorises = ["mode", "level", "class", "skin", "binds"]
        self.choiced_sub_index_list = [0] * self.length
        self.should_update_binds_view = False
        self.key_error = False

    def get_choiced_sub_option(self, index):
        """
        Get the currently selected sub-option for a given category.

        Args:
            index (int): The index of the category (mode, level, etc.)

        Returns:
            str: The currently selected sub-option.
        """
        return self.options[index][self.choiced_sub_index_list[index]]

    def get_choiced_sub_index(self, index):
        """
        Get the index of the currently selected sub-option for a given category.

        Args:
            index (int): The index of the category (mode, level, etc.)

        Returns:
            int: The index of the selected sub-option.
        """
        return self.choiced_sub_index_list[index]
    
    def get_choiced_options(self):
        """
        Yield the currently selected options for all categories.

        Returns:
            generator: A generator that yields the selected sub-options for each category.
        """
        for i in range(self.length):
            yield self.options[i][self.choiced_sub_index_list[i]]

    def next_sub_option(self):
        """
        Move to the next sub-option in the current category.

        This method increases the index of the selected sub-option, looping back if necessary.
        """
        if self.choiced_sub_index_list[self.choiced_index] < len(self.options[self.choiced_index]) - 1:
            self.choiced_sub_index_list[self.choiced_index] += 1

    def prev_sub_option(self):
        """
        Move to the previous sub-option in the current category.

        This method decreases the index of the selected sub-option, preventing it from going below zero.
        """
        if self.choiced_sub_index_list[self.choiced_index] > 0:
            self.choiced_sub_index_list[self.choiced_index] -= 1
    
    def reset_sub_options(self):
        """
        Reset all sub-options to the first option in each category.

        This method sets all selected sub-option indexes to 0, effectively resetting all settings.
        """
        self.choiced_sub_index_list = [0] * self.length
