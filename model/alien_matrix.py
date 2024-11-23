from random import choice

from model.alien_ship import Alien_ship

class Alien_matrix():
    def __init__(self, canvas, x, y, image, projectile_image, line, column):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.image = image
        self.projectile_image = projectile_image
        self.line = line
        self.column = column
        self.direction = 1
        self.alien_matrix = []

    def create_matrix(self):
        for i in range(- self.column // 2 + 1, self.column // 2 + 1):
            row = []
            for j in range(- self.line // 2 + 1, self.line // 2 + 1):
                alien = Alien_ship(self.canvas, self.x + i * 80, self.y + j * 50, image=self.image, projectile_image=self.projectile_image)
                row.append(alien)
            self.alien_matrix.append(row)
    
    def remove_alien(self, alien):
        for row in self.alien_matrix:
            if alien in row:
                row.remove(alien)
                break
    
    def move(self):
        for row in self.alien_matrix:
            for alien in row:
                alien.move(self.direction)
        if self.border_hit():
            self.direction *= -1
            self.move_down()
    
    def border_hit(self):
        for row in self.alien_matrix:
            for alien in row:
                if alien.border_hit():
                    return True
        return False
    
    def move_down(self):
        for row in self.alien_matrix:
            for alien in row:
                alien.move_down()
    
    def alien_shooting(self):
        non_empty_row = [row for row in self.alien_matrix if row]
        shooting_row = choice(non_empty_row)
        return shooting_row[-1]
    
    def delete(self):
        for row in self.alien_matrix:
            for alien in row:
                alien.dead()
        self.alien_matrix = []

