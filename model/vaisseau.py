"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""

from model.projectile import Projectile, Projectile_player, Projectile_alien

class Vaisseau:
    def __init__(self, canvas, x, y, speed):
        self.canvas = canvas
        self.width = 50
        self.height = 30
        self.x = x
        self.y = y
        self.speed = speed
    
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
    
    def hit(self):
        alien_x, alien_y = Projectile.get_position()
        return alien_x -25 <= self.x and self.x <= alien_x + 25 and alien_y -50 <= self.y and self.y <= alien_y + 15
    
    def shoot(self):
        """Créer un projectile."""
        return Projectile_player(self.canvas, self.x, self.y)
    
    

class Player(Vaisseau):
    def __init__(self, canvas, x, y, speed=10):
        super().__init__(canvas, x, y, speed)
        self.life = 3

    def shoot(self):
        """Créer un projectile."""
        return Projectile(self.canvas, self.x, self.y)



class Alien(Vaisseau):
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
    
    def hit(self):
        alien_x, alien_y = Projectile.get_position()
        return alien_x -25 <= self.x and self.x <= alien_x + 25 and alien_y -50 <= self.y and self.y <= alien_y + 15