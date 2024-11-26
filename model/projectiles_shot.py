from model.projectile import Projectile

class Projectiles_shot():
    def __init__(self, canvas):
        self.canvas = canvas
        self.by_players_list = []
        self.by_aliens_list = []

    def shot(self, x, y, type, height, image):
        if type == 1:
            self.by_players_list.append(Projectile(self.canvas, x, y - type * height, image, type))
        else:
            self.by_aliens_list.append(Projectile(self.canvas, x, y - type * height, image, type))
    
    def move(self):
        if self.by_aliens_list:
            pass
            # print(self.by_aliens_list[0].y_speed)
        for projectile in self.by_players_list:
            projectile.move()
            _, y_projectile = projectile.get_position()
            if y_projectile  - projectile.height <= 0:
                self.remove_projectile(projectile)
                projectile.delete()
        for projectile in self.by_aliens_list:
            projectile.move()
            _, y_projectile = projectile.get_position()
            if y_projectile + projectile.height >= self.canvas.winfo_height():
                self.remove_projectile(projectile)
                projectile.delete()

    def players_hit(self, players):
        for projectile in self.by_aliens_list:
            for player in players.list:
                if projectile.collide(player):
                    print(projectile.y_speed)

                    projectile.delete()
                    self.remove_projectile(projectile)
                    players.got_hit(player)

    def aliens_hit(self, aliens):
        for projectile in self.by_players_list:
            for row in aliens.matrix:
                for alien in row:
                    if projectile.collide(alien):
                        projectile.delete()
                        self.remove_projectile(projectile)
                        aliens.got_hit(alien)

    def remove_projectile(self, projectile):
        if projectile in self.by_players_list:
            self.by_players_list.remove(projectile)
        if projectile in self.by_aliens_list:
            self.by_aliens_list.remove(projectile)
    
    def delete(self):
        for projectile in self.by_players_list:
            projectile.delete()
        for projectile in self.by_aliens_list:
            projectile.delete()
        self.by_players_list = []
        self.by_aliens_list = []