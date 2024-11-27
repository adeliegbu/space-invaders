from random import choice

from model.alien_ship import Alien_ship
from model.bonus_ship import Bonus_ship
from model.cooldown import Cooldown
from model.group_object import Group_object

class Aliens(Group_object):
    def __init__(self, canvas, cooldown):
        super().__init__(canvas)
        self.cooldown = cooldown
        self.number_alien_hit = 0
        self.updating = False
        self.x_direction = 1
        self.y_direction = 0

    def create_objects(self, x, line, column):
        super().create_objects(Alien_ship, x, self.canvas.winfo_screenheight() // 3, line, column, pad_x=20, pad_y=10)
    
    def move(self):
        if self.should_change_direction():
            self.change_direction()
        super().move(self.x_direction, self.y_direction)
        self.y_direction = 0
    
    def increase_number_hit(self):
        self.number_alien_hit += 1
        self.updating = True

    def should_change_direction(self):
        for row in self.matrix:
            for alien in row:
                x_alien, y_alien = alien.get_position()
                x_future = x_alien + self.x_direction * alien.x_speed
                y_future = y_alien + self.y_direction * alien.y_speed
                if alien.will_hit_border(x_future, y_future):
                    return True
        return False

    def change_direction(self):
            self.x_direction *= -1
            self.y_direction = 1

    def should_increase_speed(self):
        if self.updating and self.number_alien_hit % 10 == 0:
                self.updating = False
                return True
        return False
    
    def increase_speed(self):
        for row in self.matrix:
            for alien in row:
                alien.x_speed += 1
    
    def should_add_bonus(self):
        return self.number_alien_hit % 5 == 0
    
    def add_bonus(self, image):
        bonus_direction = choice([-1, 1])
        if bonus_direction == 1:
            x_bonus = 50
        else:
            x_bonus = self.canvas.winfo_width() - 50
        self.matrix[0].append(Bonus_ship(self.canvas, x_bonus, 80, image, Cooldown(50), bonus_direction))

    def bonus_border_hit(self, bonus):
        x_bonus, y_bonus = bonus.get_position()
        x_future = x_bonus + bonus.direction * bonus.x_speed
        y_future = y_bonus + bonus.direction * bonus.y_speed
        return bonus.will_hit_border(x_future, y_future)
    
    def got_hit(self, alien):
        super().got_hit(alien)
        self.number_alien_hit += 1
        self.updating = True

    def alien_shooting(self):
        shooting_row = choice(self.matrix)
        if shooting_row:
            return shooting_row[-1]
        return None
    
    def shoot(self, projectile, projectile_image):
        alien_shooting = self.alien_shooting()
        if alien_shooting:
            alien_shooting.shoot(self.cooldown, projectile, projectile_image)

    def reset(self):
        super().reset()
        self.x_direction = 1
        self.y_direction = 0
        self.number_alien_hit = 0

