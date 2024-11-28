from model.projectile_related.projectile import Projectile
from model.parents_class.group_object import Group_object

class Projectiles(Group_object):
    def __init__(self, canvas):
        super().__init__(canvas)

    def add_object(self, x, y, image):
            super().add_object(Projectile(self.canvas, x, y, image))
    
    def move(self, y_direction):
        super().move_objects_list(0, y_direction)
        self.projectiles_will_be_out_of_bounds(y_direction)
    
    def projectiles_will_be_out_of_bounds(self, y_direction):
        for projectile in self.objects_list:
            if projectile.will_be_out_of_bounds(0, y_direction):
                super().remove_object(projectile)
    
    def collision(self, targets):
        for projectile in self.objects_list:
            for target in targets.objects_list:
                if projectile.collide(target):
                    super().remove_object(projectile)
                    targets.got_hit(target)
                    break
            for row in targets.objects_matrix:
                for target in row:
                    if projectile.collide(target):
                        super().remove_object(projectile)
                        targets.got_hit(target)
                        break
