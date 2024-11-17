"""
objectif : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""

class Alien:
    def __init__(self, x, y, speed=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1  # 1 pour droite, -1 pour gauche
    
    def move(self):
        """Déplacer l'alien en fonction de la direction."""
        self.x += self.speed * self.direction
        # Si l'alien atteint un bord, il change de direction et descend
        if self.x >= 770:  # Limite droite
            self.direction = -1
            self.y += 30  # L'alien descend d'une ligne
        elif self.x <= 0:  # Limite gauche
            self.direction = 1
            self.y += 30  # L'alien descend d'une ligne