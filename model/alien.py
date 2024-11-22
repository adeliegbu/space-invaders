from model.ship import Ship

class Alien(Ship):
    def __init__(self, canvas, x, y, image, projectile_image):
        super().__init__(canvas, x, y, image=image, projectile_image=projectile_image)
        self.life = 1
        self.speed = 5
        self.height = 30

    def move(self, direction):
        self.x += direction * self.speed
        if direction == 0:
            self.y += self.height
        self.canvas.move(self.id, direction * self.speed, (1 - abs(direction)) * self.height)
    
    def border_hit(self):
        return self.x -25 < 0 or self.x + 25 > self.canvas.winfo_width()

    def move_down(self):
        """Déplacer le vaisseau vers le bas."""
        self.y += 30
        self.canvas.move(self.id, 0, 30)

    def shoot(self):
        return super().shoot(-1, self.height)