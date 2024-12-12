# -*- coding: utf-8 -*-
"""
File Name: settings.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Settings class, which manages options and the selected choice in a menu.
             It allows navigating through options, getting the current selection, and resetting or finalizing choices.

TODO: Add functionality to persist user choices and enhance input handling.
"""

class Settings:
    """
    A class to represent a menu of settings options.

    This class handles navigating through a list of options, getting the current selected option,
    and modifying the selection index. It also provides methods to reset and finalize the user's choice.
    """

    def __init__(self, options):
        """
        Initialize the Settings object with a list of options.

        Args:
            options (list): A list of options available to choose from.
        """
        self.options = options
        self.length = len(options)
        self.choiced_index = 0
        self.choosing = False

    def get_choiced_index(self):
        """
        Get the index of the currently selected option.

        Returns:
            int: The index of the selected option.
        """
        return self.choiced_index
    
    def get_choiced_option(self):
        """
        Get the option currently selected.

        Returns:
            object: The selected option from the list.
        """
        return self.options[self.choiced_index]

    def next_option(self):
        """
        Move to the next option in the list, if possible.

        This method increases the index of the selected option if there are more options available.
        """
        if self.choiced_index < self.length - 1:
            self.choiced_index += 1

    def prev_option(self):
        """
        Move to the previous option in the list, if possible.

        This method decreases the index of the selected option, ensuring it does not go below 0.
        """
        if self.choiced_index > 0:
            self.choiced_index -= 1
    
    def reset_option(self):
        """
        Reset the selected option back to the first option.

        This method sets the selection index to 0, effectively resetting the user's choice.
        """
        self.choiced_index = 0
    
    def chose_option(self):
        """
        Finalize the current selection and stop the option choosing process.

        This method sets the 'choosing' flag to False, indicating that the user has chosen an option.
        """
        self.choosing = False
    
    def chose_none(self):
        """
        Set the 'choosing' flag to None, indicating no option is being chosen.

        This method allows to reset the choosing state if necessary.
        """
        self.choosing = None
