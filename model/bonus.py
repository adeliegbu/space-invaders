from model.object import group_object

class Bonus(group_object):
    def __init__(self, canvas, x, y, x_speed, y_speed, width, height, image):
        super().__init__(canvas, x, y, x_speed, y_speed, width, height, image)
    
    def move(self):
        self.y += self.y_speed
        self.canvas.move(self.image, 0, self.y_speed)
        if self.y > self.canvas.winfo_height():
            self.delete()
    
    def get_position(self):
        return self.x, self.y