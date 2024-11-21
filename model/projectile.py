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
    
    def get_postion(self):
        return self.x, self.y

class Projectile_player(Projectile):
    def __init__(self, x, y, speed=10):
        super().__init__(x, y, speed)
    
    def move(self):
        """Déplacer le projectile vers le haut."""
        self.y -= self.speed
        self.canvas.coords(self.image, self.x, self.y, self.x + self.height, self.y + self.width)


class Projectile_alien(Projectile):
    def __init__(self, x, y, speed=10):
        super().__init__(x, y, speed)
    
    def move(self):
        """Déplacer le projectile vers le haut."""
        self.y += self.speed

