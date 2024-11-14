"""
objectif : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
import projectile

class Player:
    def __init__(self, x, y, width=50, height=30, speed=20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move_left(self):
        """Déplacer le vaisseau à gauche."""
        self.x -= self.speed
    
    def move_right(self):
        """Déplacer le vaisseau à droite."""
        self.x += self.speed
    
    def shoot(self):
        """Créer un projectile."""
        return Projectile(self.x + self.width // 2, self.y)
