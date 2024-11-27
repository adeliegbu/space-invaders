from model.projectile import Projectile
from model.group_object import Group_object

class Projectiles(Group_object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.list = [[], []]

    def shot(self, x, y, type, height, image):
            super().create_objects(Projectile, x, y - type * height, 1, 1, 0, 0)
            self.objects_matrix.append(Projectile(self.canvas, x, y - type * height, image, type))
    
    def move(self):
        super().move()
        for row in self.list:
            for projectile in row:
                _, y_projectile = projectile.get_position()
                if y_projectile - projectile.height <= 0 or y_projectile + projectile.height >= self.canvas.winfo_height():
                    self.remove_projectile(projectile)
                    projectile.delete()

    def players_hit(self, players):
        for projectile in self.list[0]:
            for player in players.list:
                if projectile.collide(player):
                    projectile.delete()
                    self.remove_projectile(projectile)
                    players.got_hit(player)

    def aliens_hit(self, aliens):
        for projectile in self.list[1]:
            for row in aliens.matrix:
                for alien in row:
                    if projectile.collide(alien):
                        projectile.delete()
                        self.remove_projectile(projectile)
                        aliens.got_hit(alien)

    def wall_hit(self, wall):
        for row in self.list:
            for projectile in row:
                for row in wall.matrix:
                    for brick in row:
                        if projectile.collide(brick):
                            projectile.delete()
                            self.remove_projectile(projectile)
                            wall.got_hit(brick)
