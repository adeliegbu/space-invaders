from random import choice

from mvc_model import Players, Aliens, Cooldown, Walls, Players_projectiles, Aliens_projectiles, Binds, Game_logic
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
        
        self.aliens = Aliens(self.view.canvas, image=self.view.alien_image, bonus_image=self.view.alien_bonus_image, cooldown=Cooldown(600))

        self.players_projectiles = Players_projectiles(self.view.canvas, self.view.projectile_player_image)
        self.aliens_projectiles = Aliens_projectiles(self.view.canvas, self.view.projectile_alien_image)

        self.walls = Walls(self.view.canvas, self.view.wall_image)

        self.binds = Binds(self.view.canvas)
        self.game_logic = Game_logic(self.view, self.binds, self.players, self.aliens, self.players_projectiles, self.walls, 33)
    
    def new_game(self):
        self.game_logic.stage_number = 1
        self.game_logic.stage_update()
        self.game_logic.should_game_update = True

    def key_press(self, event):
        self.keys_pressed.add(event.keysym)  # Ajouter la touche enfoncée à l'ensemble

    def key_release(self, event):
        self.keys_pressed.discard(event.keysym)  # Retirer la touche relâchée de l'ensemble
    
    def stop_update(self):
        self.updating = False

    def update(self):
        if self.updating:
            if self.players.is_player_dead(self.p1):
                if "Left" in self.keys_pressed:
                    self.p1.move(-1, 0)
                if "Right" in self.keys_pressed:
                    self.p1.move(1, 0)
                if "space" in self.keys_pressed:
                    self.p1.shoot(self.players_projectiles)

            if self.players.is_player_dead(self.p2):     
                if "q" in self.keys_pressed:
                    self.p2.move(-1, 0)
                if "d" in self.keys_pressed:
                    self.p2.move(1, 0)
                if "Return" in self.keys_pressed:
                    self.p2.shoot(self.players_projectiles)

            if "Escape" in self.keys_pressed:
                self.view.menu()
            
  # Appeler cette méthode à nouveau après 33 ms (environ 30fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()


if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()