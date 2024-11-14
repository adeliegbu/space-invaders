"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
from tkinter import Tk
class Vaisseau:
    def __init__(self, canvas):
        self.canvas = canvas
        self.width = 50
        self.height = 30
        self.x = self.canvas.winfo_width() // 2 - self.width // 2  # Centré horizontalement
        self.y = self.canvas.winfo_height() - 50  # Positionné en bas
        self.speed = 20
        
        # Créer l'image du vaisseau dans le canvas
        self.image = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="blue")
    
    def move_left(self):
        """Déplacer le vaisseau à gauche."""
        if self.x > 0:  # Empêche le vaisseau de sortir à gauche
            self.x -= self.speed
            self.canvas.coords(self.image, self.x, self.y, self.x + self.width, self.y + self.height)
    
    def move_right(self):
        """Déplacer le vaisseau à droite."""
        if self.x + self.width < self.canvas.winfo_width():  # Empêche le vaisseau de sortir à droite
            self.x += self.speed
            self.canvas.coords(self.image, self.x, self.y, self.x + self.width, self.y + self.height)
    
    def shoot(self):
        """Créer un projectile."""
        return Projectile(self.canvas, self.x + self.width // 2, self.y)

