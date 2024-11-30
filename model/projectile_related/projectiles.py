from model.projectile_related.projectile import Projectile
from model.parents_class.group_object import Group_object

class Projectiles(Group_object):
    def __init__(self, canvas, refresh_rate):
        super().__init__(canvas, refresh_rate)

    def add_object(self, x, y, power, projectile_width, projectile_height, damage, projectile_image):
            super().add_object(Projectile(self.canvas, x, y, power, projectile_width, projectile_height, damage, projectile_image))
    
    def move(self, y_direction):
        super().move_objects_list(0, y_direction)
        self.projectiles_will_be_out_of_bounds(y_direction)
    
    def projectiles_will_be_out_of_bounds(self, y_direction):
        for projectile in self.objects_list:
            if projectile.will_be_out_of_bounds(0, y_direction):
                super().remove_object(projectile)
