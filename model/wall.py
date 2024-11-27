from model.brick import Brick
from model.group_object import Group_object

class Wall(Group_object):
    def __init__(self, canvas, image):
        super().__init__(canvas)
        self.canvas = canvas
        self.image = image
        self.matrix = []

    def create_wall(self, x,line, column, pad_x, pad_y):
        for j in range(-1, 2):
            for i in range(-2, 3):
                super().create_objects(Brick, x, 7 * self.canvas.winfo_height() // 10, line, column, pad_x, pad_y)
        brick_left = Brick(self.canvas, x - 3 * (Brick.width + pad_x), 7 * self.canvas.winfo_height() // 10, self.image)
        brick_rigth = Brick(self.canvas, x + 3 * (Brick.width + pad_x), 7 * self.canvas.winfo_height() // 10, self.image)
        self.matrix.append(brick_left)
        self.matrix.append(brick_rigth)

    def got_hit(self, brick):
        brick.delete()
        self.remove_brick(brick)
    
    def remove_brick(self, brick):
        for row in self.matrix:
            if brick in row:
                row.remove(brick)
                break   
    
