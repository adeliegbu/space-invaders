from model.projectiles_shot import Projectiles_shot

class Ship:
    def __init__(self, canvas, x, y, life, x_speed, y_speed, width, height, image):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.life = life
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.width = width
        self.height = height
        self.image = image
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor="center")
    
    def get_position(self):
        return self.x, self.y
    
    def get_dimensions(self, width, height):
        return width, height
    
    def border_hit(self):
        return self.x - self.width // 2 <= 0 or self.x + self.width // 2 >= self.canvas.winfo_width()
    
    def move(self, x_direction, y_direction):
        if not self.border_hit():
            self.x += x_direction * self.x_speed
            self.y += y_direction * self.y_speed
            self.canvas.move(self.id, x_direction * self.x_speed, y_direction * self.y_speed)

    def shoot(self, projectile, type, height, projectile_image):
        projectile.shot(self.x, self.y, type, height, projectile_image)
    
    def got_hit(self):
        self.life -= 1
        if self.life == 0:
            self.dead()

    def dead(self):
        self.canvas.delete(self.id)
    

