
"""
objectif : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""

class Projectile:
    def __init__(self, x, y, speed=10):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        """Déplacer le projectile vers le haut."""
        self.y -= self.speed
