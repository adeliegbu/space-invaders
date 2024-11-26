# This file is currently empty. You can start by defining the GroupObject class or any other relevant code for your Space Invaders project.

class Group_object:
    def __init__(self, canvas):
        self.canvas = canvas
        self.objects_matrix = []

    def create_objects(self, object, x, y, line, column, pad_x, pad_y):
        for j in range(- column // 2 + 1, column // 2+ 1):
            row = []
            for i in range(- line // 2 + 1, line // 2 + 1):
                new_object = object(self.canvas, x + i * (object.width + pad_x), y + j * (object.height + pad_y), image=object.image)
                row.append(new_object)
            self.objects_matrix.append(row)
        self.objects_matrix.append(object)

    def remove_object(self, object):
        for row in self.objects_matrix:
            if object in row:
                row.remove(object)
                object.delete()
                break

    def move(self, x_direction, y_direction):
        for object in self.objects_matrix:
            object.move(x_direction, y_direction)

    def reset(self):
        for object in self.objects_matrix:
            object.delete()
        self.objects_matrix = []