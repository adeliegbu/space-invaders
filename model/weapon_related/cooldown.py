# -*- coding: utf-8 -*-
"""
File Name: cooldown.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This module defines the Cooldown class, which handles the cooldown logic for a timed event.
             It tracks the time remaining, progress, and provides methods for updating, resetting, and modifying the cooldown period.

TODO: Implement any additional functionality to handle cooldown-based events or integrate with other game systems.
"""

class Cooldown:
    """
    A class to represent a cooldown timer.

    This class is used to track the progress of a cooldown period, update it over time,
    and check if the cooldown has ended. It also supports modifying the cooldown time and adding offsets.
    """

    def __init__(self, time, refresh_rate, offset):
        """
        Initialize the Cooldown object with the given time, refresh rate, and offset.

        Args:
            time (int): The initial cooldown time.
            refresh_rate (int): The rate at which the cooldown is updated.
            offset (int): An offset to be added to the cooldown time.
        """
        self.time = time + offset
        self.refresh_rate = refresh_rate
        self.offset = offset
        self.var = 0

    def get_progression(self):
        """
        Get the progression of the cooldown as a ratio between 0 and 1.

        Returns:
            float: The progression of the cooldown, where 0 means no progression and 1 means cooldown is complete.
        
        The progression is calculated based on the current time and the total cooldown time minus the offset.
        """
        if self.time - self.offset > 0:
            return (self.var - self.offset) / (self.time - self.offset)
        
    def ended(self):
        """
        Check if the cooldown has ended.

        Returns:
            bool: True if the cooldown has ended, False otherwise.
        
        This method checks if the current time (var) has reached or exceeded the cooldown time.
        """
        return self.var >= self.time
    
    def reset(self):
        """
        Reset the cooldown to the initial offset.

        This method sets the current time (var) to the offset, effectively restarting the cooldown.
        """
        self.var = self.offset
    
    def update(self):
        """
        Update the cooldown by the refresh rate.

        This method increases the current time (var) by the refresh rate, unless the cooldown has ended.
        """
        if not self.ended():
            self.var += self.refresh_rate
    
    def change(self, time):
        """
        Change the cooldown time to a new value.

        Args:
            time (int): The new cooldown time to be set.
        
        This method adjusts the total cooldown time by adding the offset.
        """
        self.time = time + self.offset
    
    def add_offset(self, offset):
        """
        Add an offset to the cooldown time.

        Args:
            offset (int): The value to be added to both the offset and the cooldown time.
        
        This method modifies the cooldown time and the offset by the given value.
        """
        self.offset += offset
        self.time += offset
