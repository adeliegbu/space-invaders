from random import choice

from mvc_model import Players, Aliens, Cooldown, Walls, Players_projectiles, Aliens_projectiles
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)

        self.score = 0
        self.keys_pressed = set()
        self.updating = False

        self.players = Players(self.view.canvas)
        self.players_number = 1
        self.p1, self.p2 = None, None
        
        self.aliens = Aliens(self.view.canvas, image=self.view.alien_image, cooldown=Cooldown(600))

        self.players_projectiles = Players_projectiles(self.view.canvas, self.view.projectile_player_image)
        self.aliens_projectiles = Aliens_projectiles(self.view.canvas, self.view.projectile_alien_image)

        self.walls = Walls(self.view.canvas, self.view.wall_image)

        self.view.canvas.bind("<KeyPress>", self.key_press)
        self.view.canvas.bind("<KeyRelease>", self.key_release)
        self.view.canvas.focus_set()
    
    def start_stage(self):
        self.players.add_object(self.view.x0, self.view.screen_height * 19 // 20, self.view.player_image, Cooldown(400))
        self.p1 = self.players.define_player(1)
        self.p2 = self.players.define_player(2)
        self.aliens.create_objects_matrix(line=4, column=7)
        self.walls.add_object(self.view.screen_height * 4 // 5, 4)

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
            if self.p1:
                if "Left" in self.keys_pressed:
                    self.p1.move(-1, 0)
                if "Right" in self.keys_pressed:
                    self.p1.move(1, 0)
                if "space" in self.keys_pressed:
                    self.p1.shoot(self.players_projectiles)

            if self.p2:              
                if "q" in self.keys_pressed:
                    self.p2.move(-1, 0)
                if "d" in self.keys_pressed:
                    self.p2.move(1, 0)
                if "Return" in self.keys_pressed:
                    self.p2.shoot(self.players_projectiles)

            self.aliens.move()
            self.aliens.shoot(self.aliens_projectiles)

            self.players_projectiles.move()
            self.aliens_projectiles.move()

            self.players_projectiles.collision(self.aliens, self.walls)
            self.aliens_projectiles.collision(self.players, self.walls)

            self.players.update_cooldown()
            self.aliens.var_update(self.view.alien_image)

            if "Escape" in self.keys_pressed:
                self.view.menu()
            
            self.view.canvas.after(25, self.update)  # Appeler cette méthode à nouveau après 33 ms (environ 30fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()


if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()