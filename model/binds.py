# -*- coding: utf-8 -*-
"""
File Name: binds.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: This file contains the Binds class, which manages key bindings for different game states such as game, menu, options, and upgrades.
             The class supports adding, changing, removing, and resetting key bindings, as well as handling maintainable and non-maintainable actions triggered by key presses.

TODO: Improve error handling for invalid key bindings and refactor methods for better efficiency.
"""

class Binds:
    """
    A class to manage key bindings for different game states (game, menu, options, etc.).

    This class allows the user to assign, change, remove, and reset key bindings for various actions.
    It also supports maintaining actions (i.e., actions that remain active when a key is held down) 
    and non-maintainable actions (i.e., actions that only trigger when a key is pressed once).
    """

    def __init__(self, canvas):
        """
        Initialize the Binds object and set up key bindings for different game states.

        Args:
            canvas (Canvas): The tkinter canvas object to bind keys to.
        """
        self.canvas = canvas
        self.game_binds_dico = {}
        self.menu_binds_dico = {}
        self.options_binds_dico = {}
        self.upgrade_binds_dico = {}
        self.current_binds_dico = self.game_binds_dico

        self.active_maintainable_binds = set()
        self.active_non_maintainable_binds = set()
        self.canvas.bind("<KeyPress>", self.active_bind)
        self.canvas.bind("<KeyRelease>", self.desactive_bind)
        self.canvas.focus_set()

        # Commands are tuples of (command, maintainable=boolean)

    def add_bind(self, command, key, dico):
        """
        Add a new key binding for a command if it doesn't already exist.

        Args:
            command (str): The command to bind.
            key (str): The key to bind the command to.
            dico (dict): The dictionary of current key bindings (e.g., game_binds_dico).
        """
        if not command in dico:
            dico[command] = key

    def change_bind(self, command, key, dico):
        """
        Change the key binding for an existing command.

        Args:
            command (str): The command whose key binding will be changed.
            key (str): The new key to bind the command to.
            dico (dict): The dictionary of current key bindings (e.g., game_binds_dico).
        """
        if command in dico:
            dico[command] = key

    def reset_bind(self, command, dico):
        """
        Reset the key binding for a command to None.

        Args:
            command (str): The command whose key binding will be reset.
            dico (dict): The dictionary of current key bindings (e.g., game_binds_dico).
        """
        if command in dico:
            dico[command] = None

    def remove_bind(self, command, dico):
        """
        Remove the key binding for a command.

        Args:
            command (str): The command whose key binding will be removed.
            dico (dict): The dictionary of current key bindings (e.g., game_binds_dico).
        """
        if command in dico:
            del dico[command]

    def get_binded_command(self, key, dico):
        """
        Get the command bound to a specific key.

        Args:
            key (str): The key to search for.
            dico (dict): The dictionary of current key bindings (e.g., game_binds_dico).

        Returns:
            str or None: The command bound to the key, or None if no command is bound.
        """
        for command, bind in dico.items():
            if bind == key:
                return command
        return None

    def get_binded_key(self, command, dico):
        """
        Get the key bound to a specific command.

        Args:
            command (str): The command to search for.
            dico (dict): The dictionary of current key bindings (e.g., game_binds_dico).

        Returns:
            str or None: The key bound to the command, or None if no key is bound.
        """
        if command in dico:
            return dico[command]
        return None

    def active_bind(self, event):
        """
        Handle a key press event and activate the corresponding bind.

        If the command is maintainable, it is added to the set of active maintainable binds. 
        If it is non-maintainable, it is added to the set of active non-maintainable binds.

        Args:
            event (Event): The key press event containing the key information.
        """
        command = self.get_binded_command(event.keysym, self.current_binds_dico)
        if command is not None:
            if command[1]:  # If maintainable
                self.active_maintainable_binds.add(command)
            else:  # If non-maintainable
                self.active_non_maintainable_binds.add(command)

    def desactive_bind(self, event):
        """
        Handle a key release event and deactivate the corresponding bind.

        Removes the command from the set of active binds, either maintainable or non-maintainable.

        Args:
            event (Event): The key release event containing the key information.
        """
        command = self.get_binded_command(event.keysym, self.current_binds_dico)
        if command in self.active_maintainable_binds:
            self.active_maintainable_binds.discard(command)
        if command in self.active_non_maintainable_binds:
            self.active_non_maintainable_binds.discard(command)

    def execute_active_binds(self):
        """
        Execute all active maintainable and non-maintainable binds.

        Maintainable binds are executed repeatedly as long as the key is held down. 
        Non-maintainable binds are executed once per press and are cleared after execution.
        """
        for command in self.active_maintainable_binds:
            command[0]()  # Execute maintainable bind

        non_maintainable_binds = list(self.active_non_maintainable_binds)
        self.active_non_maintainable_binds.clear()
        for command in non_maintainable_binds:
            command[0]()  # Execute non-maintainable bind

    def change_current_binds_dico(self, dico):
        """
        Change the current dictionary of key bindings.

        This resets the active binds as well.

        Args:
            dico (dict): The new dictionary of key bindings (e.g., menu_binds_dico).
        """
        self.current_binds_dico = dico
        self.reset_active_binds()

    def reset_active_binds(self):
        """
        Reset the sets of active maintainable and non-maintainable binds.
        """
        self.active_maintainable_binds.clear()
        self.active_non_maintainable_binds.clear()

    def reset_game_binds(self):
        """
        Reset game key bindings to their initial state (empty dictionaries).
        """
        self.game_binds_dico.clear()
        self.reset_active_binds()
