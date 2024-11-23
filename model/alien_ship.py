from model.ship import Ship

class Alien_ship(Ship):
    def __init__(self, canvas, x, y, image, projectile_image):
        super().__init__(canvas, x, y, image, projectile_image)
        self.life = 1
        self.speed = 5
        self.height = 30

    def move(self, direction):
        self.x += direction * self.speed
        self.canvas.move(self.id, direction * self.speed, 0)
    
    def border_hit(self):
        return self.x -30 < 0 or self.x + 30 > self.canvas.winfo_width()

    def move_down(self):
        self.y += 30
        self.canvas.move(self.id, 0, 30)

    def shoot(self):
        return super().shoot(-1, self.height)