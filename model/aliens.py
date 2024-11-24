from random import choice

from model.alien_ship import Alien_ship
from model.bonus_ship import Bonus_ship

class Aliens():
    def __init__(self, canvas, line, column, number_alien_hit, image):
        self.canvas = canvas
        self.line = line
        self.column = column
        self.number_alien_hit = number_alien_hit
        self.image = image
        self.x_direction = 1
        self.y_direction = 0
        self.matrix = [[]]    # matrice des aliens en vies, la première ligne sera réservée aux aliens bonus

    def create_matrix(self, x, y):
        for i in range(- self.column // 2 + 1, self.column // 2 + 1):
            row = []
            for j in range(- self.line // 2 + 1, self.line // 2 + 1):
                alien = Alien_ship(self.canvas, x + i * 100, y + j * 60, self.image)
                row.append(alien)
            self.matrix.append(row)
    
    def move(self):
        if self.border_hit():
            self.x_direction *= -1
            self.y_direction = 1
        for bonus in self.matrix[0]:
            if self.bonus_border_hit(bonus):
                bonus.dead()
                self.remove_alien(bonus)
        for row in self.matrix[1:]:
            for alien in row:
                alien.move(self.x_direction, self.y_direction)
        for bonus in self.matrix[0]:
            bonus.move()
        self.y_direction = 0
    
    def increase_number_alien_hit(self):
        self.number_alien_hit += 1
        if self.should_increase_speed():
            self.increase_speed
        if self.should_add_bonus():
            self.add_bonus(self.image)
    
    def should_increase_speed(self):
        return self.number_alien_hit % 10 == 0
    
    def increase_speed(self):
        for row in self.matrix:
            for alien in row:
                alien.x_speed += 1
    
    def should_add_bonus(self):
        return self.number_alien_hit % 20 == 0
    
    def add_bonus(self, image):
        bonus_direction = choice([-1, 1])
        if bonus_direction == 1:
            x_bonus = 50
        else:
            x_bonus = self.canvas.winfo_width() - 50
        self.matrix[0].append(Bonus_ship(self.canvas, x_bonus, 80, bonus_direction, image))

    def border_hit(self):
        for row in self.matrix[1:]:
            for alien in row:
                x_alien, y_alien = alien.get_position()
                x_future = x_alien + self.x_direction * alien.x_speed
                y_future = y_alien + self.y_direction * alien.y_speed
                if alien.will_hit_border(x_future, y_future):
                    return True
        return False
    
    def bonus_border_hit(self, bonus):
        x_bonus, y_bonus = bonus.get_position()
        x_future = x_bonus + bonus.direction * bonus.x_speed
        y_future = y_bonus + bonus.direction * bonus.y_speed
        return bonus.will_hit_border(x_future, y_future)
    
    def got_hit(self, alien):
        alien.got_hit()
        self.remove_alien(alien)
        self.increase_number_alien_hit()

    def alien_shooting(self):
        non_empty_row = [row for row in self.matrix[1:] if row]
        if non_empty_row:
            shooting_row = choice(non_empty_row)
            return shooting_row[-1]
    
    def shoot(self, cooldown, projectile, projectile_image):
        alien_shooting = self.alien_shooting()
        if alien_shooting:
            alien_shooting.shoot(cooldown, projectile, projectile_image)
        for bonus in self.matrix[0]:
            bonus.shoot(projectile, projectile_image)

    def remove_alien(self, alien):
        for row in self.matrix:
            if alien in row:
                row.remove(alien)
                break   
 
    def delete(self):
        for row in self.matrix:
            for alien in row:
                alien.dead()
        self.matrix = [[]]

