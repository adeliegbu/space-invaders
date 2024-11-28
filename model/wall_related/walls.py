from model.wall_related.brick import Brick
from model.parents_class.group_object import Group_object

class Walls(Group_object):
    def __init__(self, canvas, image):
        super().__init__(canvas)
        self.image = image

    def create_objects_matrix(self, x, y):
        super().create_objects_matrix(Brick, x, y, line=3, column=5, pad_x=0, pad_y=0, image=self.image)
        temporary = Brick(self.canvas, 0, 0, image=self.image)
        border_bricks = [Brick(self.canvas, x - 3 * temporary.width, y + temporary.height, image=self.image),
                        Brick(self.canvas, x + 3 * temporary.width, y + temporary.height, image=self.image)]
        temporary.delete()
        self.objects_matrix.append(border_bricks)
    
    def add_object(self, y, number):
        for i in range(number):
            self.create_objects_matrix(self.canvas.winfo_screenwidth() * (i + 1) // (number + 1), y)