"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""

from model.projectile import Projectile

class Vaisseau:
    def __init__(self, canvas, x, y, type):
        self.canvas = canvas
        self.width = 50
        self.height = 30
        self.x = x
        self.y = y

        if type == "player":
            self.type = 1
            self.speed = 10
            self.life = 3

        elif type == "alien":
            self.type = -1
            self.speed = 5
            self.life = 1
    
    def move_left(self):
        """Déplacer le vaisseau à gauche."""
        if self.x > 0:  # Empêche le vaisseau de sortir à gauche
            self.x -= self.speed
            self.canvas.coords(self.image, self.x, self.y, self.x + self.width, self.y + self.height)
        
        elif self.type == -1:
            self.y -= 30
        
    def move_right(self):
        """Déplacer le vaisseau à droite."""
        if self.x + self.width < self.canvas.winfo_width():  # Empêche le vaisseau de sortir à droite
            self.x += self.speed
        
        elif self.type == -1:
            self.y -= 30

    def shoot(self):
        """Créer un projectile."""
        return Projectile(self.canvas, self.x, self.y, self.type)
    
    def hit(self):
        proj_x, proj_y = Projectile.get_position()
        return proj_x -25 <= self.x and self.x <= proj_x + 25 and proj_y -50 <= self.y and self.y <= proj_y + 15
    
    def dead(self):
        return self.life == 0
    