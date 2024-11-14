"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
from tkinter import Tk
class Projectile:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed = 10
        
        # Créer le projectile (un petit rectangle)
        self.image = canvas.create_rectangle(self.x - 2, self.y - 10, self.x + 2, self.y, fill="red")
    
    def move(self):
        """Déplacer le projectile vers le haut."""
        self.y -= self.speed
        self.canvas.coords(self.image, self.x - 2, self.y - 10, self.x + 2, self.y)