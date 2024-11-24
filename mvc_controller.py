from random import choice

from mvc_model import Players, Aliens, Projectiles_shot, Cooldown
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)

        self.score = 0
        self.keys_pressed = set()
        self.updating = False

        self.players = Players(self.view.canvas, image=self.view.player_image)
        self.players_number = 1
        self.p1, self.p2 = None, None
        self.p1_cooldown, self.p2_cooldown = Cooldown(400), Cooldown(400)
        
        self.aliens = Aliens(self.view.canvas, line=5, column=9, number_alien_hit=0, image=self.view.alien_image)
        self.alien_cooldown = Cooldown(200)

        self.projectiles_shot = Projectiles_shot(self.view.canvas)

        self.view.canvas.bind("<KeyPress>", self.key_press)
        self.view.canvas.bind("<KeyRelease>", self.key_release)
        self.view.canvas.focus_set()
    
    def new_game(self):
        self.players.create_player(self.view.x0, 17 * self.view.y0 // 10)
        self.p1 = self.players.define_player(1)[1]
        self.p2 = self.players.define_player(2)[1]
        self.aliens.create_matrix(self.view.x0, self.view.y0 // 3) 

        self.updating = True
        self.update()

    def key_press(self, event):
        self.keys_pressed.add(event.keysym)  # Ajouter la touche enfoncée à l'ensemble

    def key_release(self, event):
        self.keys_pressed.discard(event.keysym)  # Retirer la touche relâchée de l'ensemble
    
    def stop_update(self):
        self.updating = False

    def update(self):
        if self.updating:
            if self.players.define_player(1)[0]:
                if "Left" in self.keys_pressed:
                    self.p1.move(-1, 0)
                if "Right" in self.keys_pressed:
                    self.p1.move(1, 0)
                if "space" in self.keys_pressed:
                    self.p1.shoot(self.p1_cooldown, self.projectiles_shot, self.view.projectile_image)

            if self.players.define_player(2)[0]:              
                if "q" in self.keys_pressed:
                    self.p2.move(-1, 0)
                if "d" in self.keys_pressed:
                    self.p2.move(1, 0)
                if "Return" in self.keys_pressed:
                    self.p2.shoot(self.p2_cooldown, self.projectiles_shot, self.view.projectile_image)

            self.aliens.move()
            self.projectiles_shot.move()

            self.projectiles_shot.players_hit(self.players)
            self.projectiles_shot.aliens_hit(self.aliens)

            self.aliens.shoot(self.alien_cooldown, self.projectiles_shot, self.view.projectile_image)

            self.p1_cooldown.update()
            self.p2_cooldown.update()

            if "Escape" in self.keys_pressed:
                self.view.menu()
            
            self.view.canvas.after(16, self.update)  # Appeler cette méthode à nouveau après 16 ms (environ 60 fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()


if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()