from random import choice

from model.alien_related.alien_ship import Alien_ship
from model.alien_related.bonus_ship import Bonus_ship
from model.parents_class.group_object import Group_object

class Aliens(Group_object):
    def __init__(self, canvas, refresh_rate, alien_skins, projectile_class):
        super().__init__(canvas, refresh_rate)
        self.alien_skins = alien_skins
        self.projectile_class = projectile_class
        self.x_direction = 1
        self.y_direction = 0
        self.number_alien_killed = 0
        self.should_var_update_update = False

    def create_objects_matrix(self, line, column):
        temporary = Alien_ship(self.canvas, 0, 0, self.alien_skins["basic"], self.refresh_rate, self.projectile_class, self.alien_skins["projectile"])
        temporary.delete()
        super().create_objects_matrix(Alien_ship, self.canvas.winfo_screenwidth() // 2, 4 * temporary.height, line=line, column=column, pad_x=self.canvas.winfo_screenwidth() / 1000 * 30, pad_y=self.canvas.winfo_screenheight() / 1000 * 30, image=self.alien_skins["basic"], projectile_class=self.projectile_class, projectile_image=self.alien_skins["projectile"])

    def move(self):
        if self.should_change_direction():
            self.change_direction()
        super().move_objects_matrix(self.x_direction, self.y_direction)
        self.y_direction = 0

        for bonus in self.objects_list:
            bonus.move()
            self.bonus_out_of_bounds(bonus)

    def shoot(self):
        for bonus in self.objects_list:
            bonus.shoot()
            bonus.weapon.update()
        for row in self.objects_matrix:
            for alien in row :
                if alien.level > 0:
                    alien.shoot()
                    alien.weapon.update()
    
    def got_hit(self, alien, damage):
        super().got_hit(alien, damage)
        if alien.dead():
            self.increase_number_hit()
    
    def increase_number_hit(self):
        self.number_alien_killed += 1
        self.should_var_update_update = True

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
        return self.number_alien_killed % 5 == 0
    
    def increase_speed(self, stage_number):
        for row in self.objects_matrix:
            for alien in row:
                alien.x_speed += stage_number
    
    def should_add_bonus(self):
        if self.number_alien_killed % 10 == 0:
                 return True
        return False
    
    def add_bonus(self):
        bonus_direction = choice([-1, 1])
        if bonus_direction == 1:
            x_bonus = 50
        else:
            x_bonus = self.canvas.winfo_width() - 50
        super().add_object(Bonus_ship(self.canvas, x_bonus, 80, self.alien_skins["bonus"], bonus_direction, self.refresh_rate, self.projectile_class, self.alien_skins["projectile"]))
    def bonus_out_of_bounds(self, bonus):
        if bonus.bonus_will_be_out_of_bounds():
            super().remove_object(bonus)

    def var_update(self):
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
        if not self.objects_dead():
            increasing_aliens = []
            for _ in range(stage_number * 3):
                increasing_aliens.append(choice(choice(self.objects_matrix)))
            for alien in increasing_aliens:
                alien.increase_level()
                if 0 < alien.level <= 10 :
                    alien.change_image(self.alien_skins[alien.type][alien.level // 2])
            if choice([i for i in range(5)]) == 0:
                increasing_aliens[0].become_doctor()
                increasing_aliens[0].change_image(self.alien_skins["doctor"])
                    
    def reset_number_alien_killed(self):
        self.number_alien_killed = 0

    def reset(self):
        super().reset()
        self.x_direction = 1
        self.y_direction = 0
        self.should_var_update_update = False