from model.projectile import Projectile

class Ship:
    def __init__(self, canvas, x, y, image, projectile_image):
        self.canvas = canvas
        self.width = 60
        self.height = 30
        self.x = x
        self.y = y
        self.image = image
        self.projectile_image = projectile_image
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor="center")
    
    def get_position(self):
        return self.x, self.y

    def shoot(self,type):
        """Créer un projectile."""
        return Projectile(self.canvas, self.x, self.y - self.height, type, self.projectile_image)
    
    def dead(self):
        self.canvas.delete(self.id)