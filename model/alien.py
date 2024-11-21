from model.ship import Ship

class Alien(Ship):
    def __init__(self, canvas, x, y, image, projectile_image):
        super().__init__(canvas, x, y, image=image, projectile_image=projectile_image)
        self.direction = 1
        self.life = 1
        self.speed = 3

    def move(self):
        """Déplacer l'alien."""
        self.x += self.direction * self.speed
        self.canvas.move(self.id, self.direction * self.speed, 0)
        if self.x < 0 or self.x > self.canvas.winfo_width():
            self.direction = -self.direction
            self.move_down()

    def move_down(self):
        """Déplacer le vaisseau vers le bas."""
        self.y += 30
        self.canvas.move(self.id, 0, 30)

    def shoot(self):
        return super().shoot(-1)