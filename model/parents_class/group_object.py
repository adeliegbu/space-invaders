# This file is currently empty. You can start by defining the GroupObject class or any other relevant code for your Space Invaders project.

class Group_object:
    def __init__(self, canvas, refresh_rate):
        self.canvas = canvas
        self.refresh_rate = refresh_rate
        self.objects_list = []
        self.objects_matrix = []

    def create_objects_matrix(self, object_class, x, y, line, column, pad_x, pad_y, damage, image, **kwargs):
        for j in range(- column // 2 + 1, column // 2 + 1):
            row = []
            for i in range(line):
                temporary = object_class(self.canvas, 0, 0, image, **kwargs)
                new_object = object_class(self.canvas, x + j * (temporary.width + pad_x), y + i * (temporary.height + pad_y), image, **kwargs) 
                temporary.delete()
                row.append(new_object)
            self.objects_matrix.append(row)
    
    def add_object(self, object):
        self.objects_list.append(object)
    
    def move_objects_matrix(self, x_direction, y_direction):
        for row in self.objects_matrix:
            for object in row:
                object.move(x_direction, y_direction)
    
    def move_objects_list(self, x_direction, y_direction):
        for object in self.objects_list:
            object.move(x_direction, y_direction)
    
    def got_hit(self, object, damage):
        object.got_hit(damage)
        if object.dead():
            self.remove_object(object)
    
    def collision(self, targets):
        for object in self.objects_list:
            for target in targets.objects_list:
                if object.collide(target):
                    self.got_hit(object, target.damage)
                    targets.got_hit(target, object.damage)
                    return True
            for row in targets.objects_matrix:
                for target in row:
                    if object.collide(target):
                        self.got_hit(object, target.damage)
                        targets.got_hit(target, object.damage)
                        return True
        
        for row in self.objects_matrix:
            for object in row:
                for target in targets.objects_list:
                    if object.collide(target):
                        self.got_hit(object, target.damage)
                        targets.got_hit(target, object.damage)
                        return True
                for row_target in targets.objects_matrix:
                    for target in row_target:
                        if object.collide(target):
                            self.got_hit(object, target.damage)
                            targets.got_hit(target, object.damage)
                            return True
        return False

    def objects_dead(self):
        return not self.objects_list and all(not row for row in self.objects_matrix)

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