# model/projectile.py
class Projectile:
    def __init__(self, canvas, x, y, type, image):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.type = type
        self.image = image
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor="center")
        self.speed = - self.type * 10

    def get_position(self):
        return self.x, self.y
    
    def move(self):
        """Déplacer le projectile."""
        self.y += self.speed
        self.canvas.move(self.id, 0, self.speed)
        if self.y < 0 or self.y > self.canvas.winfo_height():
            self.out_of_screen
    
    def out_of_screen(self):
        self.canvas.delete(self.id)