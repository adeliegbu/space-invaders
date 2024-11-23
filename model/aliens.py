from random import choice

from model.alien_ship import Alien_ship

class Aliens():
    def __init__(self, canvas, line, column):
        self.canvas = canvas
        self.line = line
        self.column = column
        self.x_direction = 1
        self.y_direction = 0
        self.list = []

    def create_matrix(self, x, y, image):
        for i in range(- self.column // 2 + 1, self.column // 2 + 1):
            row = []
            for j in range(- self.line // 2 + 1, self.line // 2 + 1):
                alien = Alien_ship(self.canvas, x + i * 80, y + j * 50, image)
                row.append(alien)
            self.list.append(row)
    
    def move(self):
        if self.border_hit():
            self.x_direction *= -1
            self.y_direction = 1
            
        for row in self.list:
            for alien in row:
                alien.move(self.x_direction, self.y_direction)
        self.y_direction = 0

    def move_down(self):
        for row in self.list:
            for alien in row:
                alien.move_down()
    
    def border_hit(self):
        for row in self.list:
            for alien in row:
                if alien.border_hit():
                    return True
        return False
    
    def got_hit(self, alien):
        alien.got_hit()
        self.remove_alien(alien)
    
    def alien_shooting(self):
        non_empty_row = [row for row in self.list if row]
        shooting_row = choice(non_empty_row)
        return shooting_row[-1]

    def remove_alien(self, alien):
        for row in self.list:
            if alien in row:
                row.remove(alien)
                break   
 
    def delete(self):
        for row in self.list:
            for alien in row:
                alien.dead()
        self.list = []

