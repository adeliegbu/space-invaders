from model.brick import Brick

class Wall():
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.image = image
        self.matrix = []

    def create_wall(self, x):
        for j in range(- 1, 2):
            row = []
            for i in range(- 3, 4):
                brick = Brick(self.canvas, x + i * 15, 8 * self.canvas.winfo_height() // 10 + j * 15, self.image)
                row.append(brick)
            if not j:
                brick_left = Brick(self.canvas, x - 4 * 15, 8 * self.canvas.winfo_height() // 10, self.image)
                brick_right = Brick(self.canvas, x+- 4 * 15, 8 * self.canvas.winfo_height() // 10, self.image)
                row.append(brick_left)
                row.append(brick_right)

            self.matrix.append(row)
    
    def got_hit(self, brick):
        brick.delete()
        self.remove_brick(brick)
    
    def remove_brick(self, brick):
        for row in self.matrix:
            if brick in row:
                row.remove(brick)
                break   
    
