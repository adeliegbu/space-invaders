class Object:
    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, life, image):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.width = width
        self.height = height
        self.life = life
        self.image = image
        self.id = self.canvas.create_image(self.x, self.y, image=self.image, anchor="center")
    
    def get_position(self):
        return self.x, self.y
    
    def get_dimensions(self):
        return self.width, self.height
    
    def collide(self, object):
        x1, y1 = self.get_position()
        x2, y2 = object.get_position()
        w1, h1 = self.get_dimensions()
        w2, h2 = object.get_dimensions()
        return x1 - w1 // 2 <= x2 + w2 // 2 and x1 + w1 // 2 >= x2 - w2 // 2 and y1 - h1 // 2 <= y2 + h2 // 2 and y1 + h1 // 2 >= y2 - h2 // 2
    
    def will_be_out_of_bounds(self, x_direction, y_direction):
        x_future = self.x + x_direction * self.x_speed
        y_future = self.y + y_direction * self.y_speed
        return x_future - self.width // 2 <= 0 or x_future + self.width // 2 >= self.canvas.winfo_width() or y_future - self.height // 2 <= 0 or y_future + self.height // 2 >= self.canvas.winfo_height()
    
    def move(self, x_direction, y_direction):
        if not self.will_be_out_of_bounds(x_direction, y_direction):
            self.x += x_direction * self.x_speed
            self.y += y_direction * self.y_speed
            self.canvas.move(self.id, x_direction * self.x_speed, y_direction * self.y_speed)
    
    def got_hit(self):
        self.life -= 1
        
    def dead(self):
        return self.life == 0
    
    def delete(self):
        self.canvas.delete(self.id)