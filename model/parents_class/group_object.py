# This file is currently empty. You can start by defining the GroupObject class or any other relevant code for your Space Invaders project.

class Group_object:
    def __init__(self, canvas):
        self.canvas = canvas
        self.objects_list = []
        self.objects_matrix = []

    def create_objects_matrix(self, object_class, x, y, line, column, pad_x, pad_y, image):
        for j in range(- column // 2 + 1, column // 2 + 1):
            row = []
            for i in range(line):
                temporary = object_class(self.canvas, 0, 0, image)
                new_object = object_class(self.canvas, x + j * (temporary.width + pad_x), y + i * (temporary.height + pad_y), image) 
                temporary.delete()
                row.append(new_object)
            self.objects_matrix.append(row)
    
    def add_object(self, object):
        self.objects_list.append(object)
    
    def move_objects_matrix(self,x_direction, y_direction):
        for row in self.objects_matrix:
            for object in row:
                object.move(x_direction, y_direction)
    
    def move_objects_list(self, x_direction, y_direction):
        for object in self.objects_list:
            object.move(x_direction, y_direction)
    
    def got_hit(self, object):
        object.got_hit()
        if object.dead():
            self.remove_object(object)

    def remove_object(self, object):
        if object in self.objects_list:
            self.objects_list.remove(object)
            object.delete()
        for row in self.objects_matrix:
            if object in row:
                row.remove(object)
                object.delete()
                break

    def reset(self):
        for object in self.objects_list:
            object.delete()
        self.objects_list = []
        for row in self.objects_matrix:
            for object in row:
                object.delete()
        self.objects_matrix = []