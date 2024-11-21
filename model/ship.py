from model.projectile import Projectile

class Ship:
    def __init__(self, canvas, x, y, type, image, projectile_image):
        self.canvas = canvas
        self.width = 60
        self.height = 30
        self.x = x
        self.y = y
        self.image = image
        self.projectile_image = projectile_image
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor="center")

        if type == "player":
            self.type = 1
            self.speed = 5
            self.life = 3

        elif type == "alien":
            self.type = -1
            self.speed = 3
            self.life = 1

    def move_left(self):
        """Déplacer le vaisseau à gauche."""
        if self.x > 0:  # Empêche le vaisseau de sortir à gauche
            self.x -= self.speed
            self.canvas.move(self.id, -self.speed, 0)
        
    def move_right(self):
        """Déplacer le vaisseau à droite."""
        if self.x + self.width < self.canvas.winfo_width():  # Empêche le vaisseau de sortir à droite
            self.x += self.speed
            self.canvas.move(self.id, self.speed, 0)

    def shoot(self):
        """Créer un projectile."""
        return Projectile(self.canvas, self.x, self.y - self.height, self.type, self.projectile_image)
    
    def hit(self):
        proj_x, proj_y = Projectile.get_position()
        return proj_x -25 <= self.x and self.x <= proj_x + 25 and proj_y -50 <= self.y and self.y <= proj_y + 15
    
    def dead(self):
        self.canvas.delete(self.id)