from model.projectile import Projectile

class Projectiles_shot():
    def __init__(self, canvas):
        self.canvas = canvas
        self.list = []

    def shot(self, x, y, type, height, image):
        self.list.append(Projectile(self.canvas, x, y - type * height, type, image))
    
    def move(self):
        for projectile in self.list:
            projectile.move()
        
    def hit(self, targets):
        for projectile in self.list:
            x_projectile, y_projectile = projectile.get_position()

            # Aplatir la matrice de cibles si nécessaire
            if isinstance(targets.list[0], list):
                targets_list = [target for sublist in targets.list for target in sublist]
            else:
                targets_list = targets.list

            for target in targets_list:
                x_target, y_target = target.get_position()
                target_width, target_height = target.get_dimensions()

                if x_projectile - target_width // 2 <= x_target <= x_projectile + target_width // 2 and y_projectile - target_height // 2 <= y_target <= y_projectile + target_height // 2:
                    projectile.out_of_screen()
                    self.remove_projectile(projectile)
                    targets.got_hit(target)

    def remove_projectile(self, projectile):
        if projectile in self.list:
            self.list.remove(projectile)
    
    def delete(self):
        for projectile in self.list:
            projectile.out_of_screen()
        self.list = []