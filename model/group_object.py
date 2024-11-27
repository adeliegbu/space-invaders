# This file is currently empty. You can start by defining the GroupObject class or any other relevant code for your Space Invaders project.

class Group_object:
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.image = image
        self.objects_matrix = []

    def create_objects(self, object_class, x, y, line, column, pad_x, pad_y, **specific_args):
        for j in range(- column // 2 + 1, column // 2 + 1):
            row = []
            for i in range(- line // 2 + 1, line // 2 + 1):
                new_object = object_class(self.canvas, x + i * (object_class.width + pad_x), y + j * (object_class.height + pad_y), self.image, **specific_args) 
                row.append(new_object)
            self.objects_matrix.append(row)
    
    def got_hit(self, object):
        object.got_hit()
        if object.dead():
            self.remove_object(object)

    def remove_object(self, object):
        for row in self.objects_matrix:
            if object in row:
                row.remove(object)
                object.delete()
                break

    def move(self, x_direction, y_direction):
        for row in self.objects_matrix:
            for object in row:
                object.move(x_direction, y_direction)

    def reset(self):
        for row in self.objects_matrix:
            for object in row:
                object.delete()
        self.objects_matrix = []