from random import choice

from model.alien_related.alien_ship import Alien_ship
from model.alien_related.bonus_ship import Bonus_ship
from model.cooldown import Cooldown
from model.parents_class.group_object import Group_object

class Aliens(Group_object):
    def __init__(self, canvas, image, cooldown):
        super().__init__(canvas)
        self.image = image
        self.cooldown = cooldown
        self.x_direction = 1
        self.y_direction = 0
        self.number_alien_hit = 0
        self.updating = False

    def create_objects_matrix(self, line, column):
        super().create_objects_matrix(Alien_ship, self.canvas.winfo_screenwidth() // 2, 50, line=line, column=column, pad_x=20, pad_y=10, image=self.image)

    def move(self):
        if self.should_change_direction():
            self.change_direction()
        super().move_objects_matrix(self.x_direction, self.y_direction)
        self.y_direction = 0

        for bonus in self.objects_list:
            if not self.bonus_out_of_bounds(bonus):
                bonus.move()

    def alien_shooting(self):
        shooting_row = choice(self.objects_matrix)
        if shooting_row:
            return shooting_row[-1]
        return None
    
    def shoot(self, projectile_class):
        alien_shooting = self.alien_shooting()
        if alien_shooting:
            alien_shooting.shoot(self.cooldown, projectile_class)
        for bonus in self.objects_list:
            bonus.shoot(projectile_class)
            bonus.update_cooldown()
    
    def got_hit(self, alien):
        super().got_hit(alien)
        self.increase_number_hit()
    
    def increase_number_hit(self):
        self.number_alien_hit += 1
        self.updating = True

    def should_change_direction(self):
        for row in self.objects_matrix:
            for alien in row:
                if alien.will_be_out_of_bounds(self.x_direction, self.y_direction):
                    return True
        return False

    def change_direction(self):
            self.x_direction *= -1
            self.y_direction = 1

    def should_increase_speed(self):
        return self.number_alien_hit % 10 == 0
    
    def increase_speed(self):
        for row in self.objects_matrix:
            for alien in row:
                alien.x_speed += 1
    
    def should_add_bonus(self):
        if self.number_alien_hit % 5 == 0:
                 return True
        return False
    
    def add_bonus(self, image):
        bonus_direction = choice([-1, 1])
        if bonus_direction == 1:
            x_bonus = 50
        else:
            x_bonus = self.canvas.winfo_width() - 50
        super().add_object(Bonus_ship(self.canvas, x_bonus, 80, image, Cooldown(126), bonus_direction))

    def bonus_out_of_bounds(self, bonus):
        if bonus.bonus_will_be_out_of_bounds():
            super().remove_object(bonus)

    def var_update(self, bonus_image):
        if self.updating:
            var = 0
            if self.should_increase_speed():
                self.increase_speed()
                var += 1
            if self.should_add_bonus():
                self.add_bonus(bonus_image)
                var += 1
            if var > 0:
                self.updating = False
        self.cooldown.update()

    def reset(self):
        super().reset()
        self.x_direction = 1
        self.y_direction = 0
        self.number_alien_hit = 0
        self.updating = False

