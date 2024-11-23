from random import choice

from mvc_model import Player, Cooldown, Alien_matrix
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)

        self.score = 0
        self.keys_pressed = set()
        self.updating = False

        self.players_cooldown = Cooldown(400)
        self.players = Player(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, image=self.view.player_image, projectile_image=self.view.projectile_image)
        
        self.alien_cooldown = Cooldown(200)
        self.aliens_matrix = Alien_matrix(self.view.canvas, self.view.x0, self.view.y0 // 3 ,image=self.view.alien_image, projectile_image=self.view.projectile_image, line=5, column=9)

        self.projectiles_player = []
        self.projectiles_alien = []

        self.view.canvas.bind("<KeyPress>", self.key_press)
        self.view.canvas.bind("<KeyRelease>", self.key_release)
        self.view.canvas.focus_set()
    
    def main(self):
        self.players.create_player()
        self.aliens_matrix.create_matrix() 

        self.updating = True
        self.update()

    def key_press(self, event):
        self.keys_pressed.add(event.keysym)  # Ajouter la touche enfoncée à l'ensemble

    def key_release(self, event):
        self.keys_pressed.discard(event.keysym)  # Retirer la touche relâchée de l'ensemble

    def shoot(self, type):
        if type == "player 1" and self.players_cooldown.cooldown_ended() and self.players.define_player(1)[0]:
            projectile = self.players.define_player(1)[1].shoot()
            self.projectiles_player.append(projectile)
            self.players_cooldown.cooldown_reset()

        if type == "alien" and self.aliens_matrix and self.alien_cooldown.cooldown_ended():
            alien_shooting = self.aliens_matrix.alien_shooting()
            projectile = alien_shooting.shoot()
            self.projectiles_alien.append(projectile)
            self.alien_cooldown.cooldown_reset()
    
    def stop_update(self):
        self.updating = False
    
    def hit(self):
        for projectile in self.projectiles_alien:
            x_projectile, y_projectile = projectile.get_position()
            for player in self.players.player:
                x_player, y_player = player.get_position()

                if x_projectile - 30 <= x_player <= x_projectile + 30 and y_projectile - 10 <= y_player <= y_projectile + 45:
                    player.life -= 1
                    if player.life == 0:
                        self.players.remove_player(player)
                    projectile.out_of_screen()
                    self.projectiles_alien.remove(projectile)

        for projectile in self.projectiles_player:
            x_projectile, y_projectile = projectile.get_position()
            for row in self.aliens_matrix.alien_matrix:
                for alien in row:
                    x_alien, y_alien = alien.get_position()
                    if x_projectile - 25 <= x_alien <= x_projectile + 25 and y_projectile - 37 <= y_alien <= y_projectile + 15:
                        alien.dead()
                        projectile.out_of_screen()
                        self.aliens_matrix.remove_alien(alien)
                        self.projectiles_player.remove(projectile)
                        self.score += 100

    def update(self):
        if self.updating:
            if "Left" in self.keys_pressed and self.players.define_player(1)[0]:
                self.players.define_player(1)[1].move_left()
            if "Right" in self.keys_pressed and self.players.define_player(1)[0]:
                self.players.define_player(1)[1].move_right()
            
            if "q" in self.keys_pressed and self.players.define_player(2)[0]:
                self.players.define_player(2)[1].move_left()
            if "d" in self.keys_pressed and self.players.define_player(2)[0]:
                self.players.define_player(2)[1].move_right()
            
            self.aliens_matrix.move()
 
            for projectile in self.projectiles_player:
                projectile.move()  
            for projectile in self.projectiles_alien:
                projectile.move()

            self.hit()

            self.players_cooldown.cooldown_update()
            self.alien_cooldown.cooldown_update()

            if "space" in self.keys_pressed:
                self.shoot("player 1")

            self.shoot("alien")
            
            if "Escape" in self.keys_pressed:
                self.stop_update()
                self.view.menu()
            
            self.view.canvas.after(16, self.update)  # Appeler cette méthode à nouveau après 16 ms (environ 60 fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()


if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()