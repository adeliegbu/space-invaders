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
    
    def will_hit_border(self, x_future, y_future):
        return x_future - self.width // 2 <= 0 or x_future + self.width // 2 >= self.canvas.winfo_width() or y_future - self.height // 2 <= 0 or y_future + self.height // 2 >= self.canvas.winfo_height()
    
    def move(self, x_direction, y_direction):
        x_future = self.x + x_direction * self.x_speed
        y_future = self.y + y_direction * self.y_speed
        if not self.will_hit_border(x_future, y_future):
            self.x += x_direction * self.x_speed
            self.y += y_direction * self.y_speed
            self.canvas.move(self.id, x_direction * self.x_speed, y_direction * self.y_speed)

    def shoot(self, cooldown, projectile, type, height, projectile_image):
        if cooldown.ended():
            projectile.shot(self.x, self.y, type, height, projectile_image)
            cooldown.reset()
        else:
            cooldown.update()
    
    def got_hit(self):
        self.life -= 1
        if self.life == 0:
            self.dead()

    def dead(self):
        self.canvas.delete(self.id)
    

