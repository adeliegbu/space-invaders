from random import choice

from mvc_model import Player, Cooldown, Alien
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)

        self.score = 0
        self.keys_pressed = set()
        self.updating = True

        self.player = Player(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, image=self.view.player_image, projectile_image=self.view.projectile_image)
        self.player_cooldown = Cooldown(500)

        self.aliens_matrix = [[Alien(self.view.canvas, self.view.x0 - j * 60, self.view.y0 // 3 - i * 40, image=self.view.alien_image, projectile_image=self.view.projectile_image) for i in range(-2, 3)] for j in range(-4, 5)] 
        self.alien_cooldown = Cooldown(1000)
        self.alien_direction = 1

        self.projectiles_player = []
        self.projectiles_alien = []

    def main(self):
        self.player = Player(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, image=self.view.player_image, projectile_image=self.view.projectile_image)
        self.aliens_matrix = [[Alien(self.view.canvas, self.view.x0 - j * 60, self.view.y0 // 3 - i * 40, image=self.view.alien_image, projectile_image=self.view.projectile_image) for i in range(-2, 3)] for j in range(-4, 5)] 
        self.projectiles = []
        self.view.canvas.bind("<KeyPress>", self.key_press)
        self.view.canvas.bind("<KeyRelease>", self.key_release)
        self.view.canvas.focus_set()
        self.updating = True
        self.update()

    def key_press(self, event):
        self.keys_pressed.add(event.keysym)  # Ajouter la touche enfoncée à l'ensemble

    def key_release(self, event):
        self.keys_pressed.discard(event.keysym)  # Retirer la touche relâchée de l'ensemble

    def shoot(self, type):
        if type == "player" and self.player_cooldown.cooldown_ended():
            projectile = self.player.shoot()
            self.projectiles_player.append(projectile)
            self.player_cooldown.cooldown_reset()

        if type == "alien" and self.aliens_matrix:
            non_empty_aliens_rows = [row for row in self.aliens_matrix if row]  # Filtrer les listes non vides
            alien_row_shooting = choice(non_empty_aliens_rows)
            alien_shooting = alien_row_shooting[0]
            if self.alien_cooldown.cooldown_ended():
                projectile = alien_shooting.shoot()
                self.projectiles_alien.append(projectile)
                self.alien_cooldown.cooldown_reset()
    
    def stop_update(self):
        self.updating = False
    
    def hit(self):
        for projectile in self.projectiles_alien:
            x_projectile, y_projectile = projectile.get_position()
            x_player, y_player = self.player.get_position()
 
            if x_projectile -30 <= x_player and x_player <= x_projectile + 30 and y_projectile - 10 <= y_player and y_player <= y_projectile + 45:
                self.player.life -= 1
                if self.player.life == 0:
                    self.player.dead()
                projectile.out_of_screen()
                self.projectiles_alien.remove(projectile)

        for projectile in self.projectiles_player:
            x_projectile, y_projectile = projectile.get_position()
            for alien_row in self.aliens_matrix:
                for alien in alien_row:
                    x_alien, y_alien = alien.get_position()
                    if x_projectile -25 <= x_alien and x_alien <= x_projectile + 25 and y_projectile -37 <= y_alien and y_alien <= y_projectile + 15:
                        alien.life -= 1
                        if alien.life == 0:
                            alien.dead()
                        projectile.out_of_screen()
                        alien_row.remove(alien)
                        self.projectiles_player.remove(projectile)
                        self.score += 10

    def update(self):
        if self.updating:
            if "Left" in self.keys_pressed:
                self.player.move_left()
            if "Right" in self.keys_pressed:
                self.player.move_right()
            
            for alien_row in self.aliens_matrix:
                for alien in alien_row:
                    alien.move(self.alien_direction)
                    if alien.border_hit():
                        for alien_row in self.aliens_matrix:
                            for alien in alien_row:
                                self.alien_direction = - self.alien_direction
                                alien.move_down()                       
 
            for projectile in self.projectiles_player:
                projectile.move()  
            for projectile in self.projectiles_alien:
                projectile.move()

            self.hit()

            self.player_cooldown.cooldown_update()
            self.alien_cooldown.cooldown_update()

            if "space" in self.keys_pressed:
                self.shoot("player")

            self.shoot("alien")
            
            self.view.canvas.after(16, self.update)  # Appeler cette méthode à nouveau après 16 ms (environ 60 fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()

if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()