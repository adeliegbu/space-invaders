"""
objectif : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""

class Projectile:
    def __init__(self,canvas, x, y, speed, way):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.height = 25
        self.width = 10
        self.speed = speed
        self.way = way
    
    def get_postion(self):
        return self.x, self.y
    
    def move(self):
        """Déplacer le projectile vers le haut."""
        self.y -= self.speed * self.way
        self.canvas.coords(self.image, self.x, self.y, self.x + self.height, self.y + self.width)


