# -*- coding: utf-8 -*-
"""
File: alien.py
Author: Adélie GIBOU, Loann CORDEL
Date: 12 dec 2024
Description: Implementation of the Aliens class, representing a group of alien ships.
             Handles group behaviors like movement, shooting, and interaction with bonuses.

TODO:
- Optimize alien movement logic.
- Add more dynamic behaviors for different alien types.
- Implement additional bonus effects.
"""

from random import choice

from model.alien_related.alien_ship import Alien_ship
from model.alien_related.bonus_ship import Bonus_ship
from model.parents_class.group_object import Group_object

class Aliens(Group_object):
    """Represents a group of alien ships with collective behaviors."""

    def __init__(self, canvas, refresh_rate, alien_skins, projectile_class):
        """
        Initialize the Aliens group.

        Args:
            canvas: The canvas on which the aliens will be drawn.
            refresh_rate (int): The refresh rate for alien actions.
            alien_skins (dict): Dictionary containing alien skin images.
            projectile_class: Class representing alien projectiles.
        """
        super().__init__(canvas, refresh_rate)
        self.alien_skins = alien_skins
        self.projectile_class = projectile_class
        self.x_direction = 1
        self.y_direction = 0
        self.number_alien_killed = 0
        self.should_var_update_update = False

    def create_objects_matrix(self, line, column):
        """
        Create a matrix of alien objects.

        Args:
            line (int): Number of rows in the matrix.
            column (int): Number of columns in the matrix.
        """
        temporary = Alien_ship(
            self.canvas, 0, 0, self.alien_skins["basic"],
            self.refresh_rate, self.projectile_class, self.alien_skins["projectile"]
        )
        temporary.delete()
        super().create_objects_matrix(
            Alien_ship,
            self.canvas.winfo_screenwidth() // 2, 4 * temporary.height,
            line=line, column=column,
            pad_x=self.canvas.winfo_screenwidth() / 1000 * 30,
            pad_y=self.canvas.winfo_screenheight() / 1000 * 30,
            image=self.alien_skins["basic"],
            projectile_class=self.projectile_class,
            projectile_image=self.alien_skins["projectile"]
        )

    def move(self):
        """Move the aliens, changing direction if needed."""
        if self.should_change_direction():
            self.change_direction()
        super().move_objects_matrix(self.x_direction, self.y_direction)
        self.y_direction = 0

        for bonus in self.objects_list:
            bonus.move()
            self.bonus_out_of_bounds(bonus)

    def shoot(self):
        """Make all aliens and bonuses shoot."""
        for bonus in self.objects_list:
            bonus.shoot()
            bonus.weapon.update()
        for row in self.objects_matrix:
            for alien in row:
                if alien.level > 0:
                    alien.shoot()
                    alien.weapon.update()

    def got_hit(self, alien, damage):
        """
        Handle an alien getting hit.

        Args:
            alien: The alien object that was hit.
            damage (int): The amount of damage dealt.
        """
        super().got_hit(alien, damage)
        if alien.dead():
            self.increase_number_hit()

    def increase_number_hit(self):
        """Increase the counter of killed aliens and mark for updates."""
        self.number_alien_killed += 1
        self.should_var_update_update = True

    def should_change_direction(self):
        """
        Check if aliens need to change direction.

        Returns:
            bool: True if a direction change is required, False otherwise.
        """
        for row in self.objects_matrix:
            for alien in row:
                if alien.will_be_out_of_bounds(self.x_direction, self.y_direction):
                    return True
        return False

    def change_direction(self):
        """Change the movement direction of the aliens."""
        self.x_direction *= -1
        self.y_direction = 1

    def should_increase_speed(self):
        """
        Determine if the speed of the aliens should increase.

        Returns:
            bool: True if speed should increase, False otherwise.
        """
        return self.number_alien_killed % 5 == 0

    def increase_speed(self, stage_number):
        """
        Increase the speed of all aliens.

        Args:
            stage_number (int): The amount by which to increase speed.
        """
        for row in self.objects_matrix:
            for alien in row:
                alien.x_speed += stage_number

    def should_add_bonus(self):
        """
        Check if a bonus should be added.

        Returns:
            bool: True if a bonus should be added, False otherwise.
        """
        return self.number_alien_killed % 10 == 0

    def add_bonus(self):
        """Add a bonus ship to the game."""
        bonus_direction = choice([-1, 1])
        x_bonus = 50 if bonus_direction == 1 else self.canvas.winfo_width() - 50
        super().add_object(
            Bonus_ship(
                self.canvas, x_bonus, 80,
                self.alien_skins["bonus"], bonus_direction,
                self.refresh_rate, self.projectile_class, self.alien_skins["projectile"]
            )
        )

    def bonus_out_of_bounds(self, bonus):
        """
        Remove a bonus if it goes out of bounds.

        Args:
            bonus: The bonus ship object to check.
        """
        if bonus.bonus_will_be_out_of_bounds():
            super().remove_object(bonus)

    def var_update(self):
        """
        Update variables based on conditions, like increasing speed or adding bonuses."""
        if self.should_var_update_update:
            var = 0
            if self.should_increase_speed():
                self.increase_speed(1)
                var += 1
            if self.should_add_bonus():
                self.add_bonus()
                var += 1
            if var > 0:
                self.should_var_update_update = False

    def increase_aliens_level(self, stage_number):
        """
        Increase the level of a subset of aliens.

        Args:
            stage_number (int): Determines how many aliens to level up.
        """
        if not self.objects_dead():
            increasing_aliens = [choice(choice(self.objects_matrix)) for _ in range(stage_number * 8)]
            for alien in increasing_aliens:
                alien.increase_level()
                if 0 < alien.level <= 10:
                    alien.change_image(self.alien_skins[alien.type][alien.level // 2])
            if choice([i for i in range(5)]) == 0:
                increasing_aliens[0].become_doctor()
                increasing_aliens[0].change_image(self.alien_skins["doctor"])

    def reset_number_alien_killed(self):
        """Reset the counter of killed aliens."""
        self.number_alien_killed = 0

    def reset(self):
        """Reset the aliens group to its initial state."""
        super().reset()
        self.x_direction = 1
        self.y_direction = 0
        self.should_var_update_update = False
