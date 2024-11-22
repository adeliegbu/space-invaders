from model.ship import Ship

class Player(Ship):
    def __init__(self, canvas, x, y, image, projectile_image):
        super().__init__(canvas, x, y, image=image, projectile_image=projectile_image)
        self.life = 3
        self.speed = 8

    def move_left(self):
        """Déplacer le vaisseau à gauche."""
        if self.x - 30 > 0:  # Empêche le vaisseau de sortir à gauche
            self.x -= self.speed
            self.canvas.move(self.id, -self.speed, 0)
        
    def move_right(self):
        """Déplacer le vaisseau à droite."""
        if self.x + 30 < self.canvas.winfo_width():  # Empêche le vaisseau de sortir à droite
            self.x += self.speed
            self.canvas.move(self.id, self.speed, 0)
            
    def shoot(self):
        return super().shoot(1)