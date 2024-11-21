from random import uniform

from mvc_model import Player, Alien
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)
        self.score = 0
        self.keys_pressed = set()
        self.can_shoot = True
        self.shoot_cooldown = 500
        self.updating = True
        self.alien_direction = 1
        self.player = Player(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, image=self.view.player_image, projectile_image=self.view.projectile_image)
        self.aliens = [Alien(self.view.canvas, self.view.x0 - i * 60, self.view.y0 // 3, image=self.view.alien_image, projectile_image=self.view.projectile_image) for i in range(-4, 5)]
        self.projectiles = []

    def main(self):
        self.player = Player(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, image=self.view.player_image, projectile_image=self.view.projectile_image)
        self.aliens = [Alien(self.view.canvas, self.view.x0 - i * 60, self.view.y0 // 3, image=self.view.alien_image, projectile_image=self.view.projectile_image) for i in range(-4, 5)]
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

    def reset_shoot(self):
        self.can_shoot = True

    def shoot(self):
        if self.can_shoot:
            projectile = self.player.shoot()
            self.projectiles.append(projectile)
            self.can_shoot = False
            self.view.canvas.after(self.shoot_cooldown, self.reset_shoot)
    
    def stop_update(self):
        self.updating = False
    
    def hit(self):
        for alien in self.aliens:
            for projectile in self.projectiles:
                x_alien, y_alien = alien.get_position()
                x_projectile, y_projectile = projectile.get_position()

                if x_projectile -25 <= x_alien and x_alien <= x_projectile + 25 and y_projectile -37 <= y_alien and y_alien <= y_projectile + 15:
                    alien.life -= 1
                    if alien.life == 0:
                        alien.dead()
                    projectile.out_of_screen()
                    self.aliens.remove(alien)
                    self.projectiles.remove(projectile)
                    self.score += 10

    def update(self):
        if self.updating:
            if "Left" in self.keys_pressed:
                self.player.move_left()
            if "Right" in self.keys_pressed:
                self.player.move_right()
            if "space" in self.keys_pressed:
                self.shoot()

            for alien in self.aliens:
                if alien.move():
                    for alien in self.aliens:
                        alien.direction = - alien.direction
                        alien.move_down()
                    break
            for projectile in self.projectiles:
                projectile.move()

            self.hit()
            
            self.view.canvas.after(16, self.update)  # Appeler cette méthode à nouveau après 16 ms (environ 60 fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()

if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()