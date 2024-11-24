from model.projectile import Projectile

class Projectiles_shot():
    def __init__(self, canvas):
        self.canvas = canvas
        self.by_players_list = []
        self.by_aliens_list = []

    def shot(self, x, y, type, height, image):
        if type == 1:
            self.by_players_list.append(Projectile(self.canvas, x, y - type * height, type, image))
        else:
            self.by_aliens_list.append(Projectile(self.canvas, x, y - type * height, type, image))
    
    def move(self):
        for projectile in self.by_players_list:
            projectile.move()
        for projectile in self.by_aliens_list:
            projectile.move()
    
    def players_hit(self, players):
        for projectile in self.by_aliens_list:
            x_projectile, y_projectile = projectile.get_position()
            for player in players.list:
                x_player, y_player = player.get_position()
                player_width, player_height = player.get_dimensions()
                if x_projectile - player_width // 2 <= x_player <= x_projectile + player_width // 2 and y_projectile - player_height <= y_player <= y_projectile + player_height:
                    projectile.out_of_screen()
                    self.remove_projectile(projectile)
                    players.got_hit(player)

    def aliens_hit(self, aliens):
        for projectile in self.by_players_list:
            x_projectile, y_projectile = projectile.get_position()
            for row in aliens.matrix:
                for alien in row:
                    x_alien, y_alien = alien.get_position()
                    alien_width, alien_height = alien.get_dimensions()
                    if x_projectile - alien_width // 2 <= x_alien <= x_projectile + alien_width // 2 and y_projectile - alien_height <= y_alien <= y_projectile + alien_height:
                        projectile.out_of_screen()
                        self.remove_projectile(projectile)
                        aliens.got_hit(alien)

    def remove_projectile(self, projectile):
        if projectile in self.by_players_list:
            self.by_players_list.remove(projectile)
        if projectile in self.by_aliens_list:
            self.by_aliens_list.remove(projectile)
    
    def delete(self):
        for projectile in self.by_players_list:
            projectile.out_of_screen()
        for projectile in self.by_aliens_list:
            projectile.out_of_screen()
        self.by_players_list = []
        self.by_aliens_list = []