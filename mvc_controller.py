from random import choice

from mvc_model import Players, Aliens, Cooldown, Walls, Players_projectiles, Aliens_projectiles, Binds, Game_logic, Options
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

        self.refresh_rate = 25
        self.game_logic = Game_logic(self.view, self.binds, self.players, self.aliens, self.players_projectiles, self.walls, self.refresh_rate)

    
    def new_game(self):
        self.game_logic.stage_number = 1
        self.game_logic.stage_update()
        self.game_logic.should_game_update = True
        self.game_logic.game_update()

    def in_menu(self):
        self.game_logic.should_game_update = False
        self.game_logic.should_menu_update = True
        self.game_logic.reset()
        self.game_logic.menu_update()
  # Appeler cette méthode à nouveau après 33 ms (environ 30fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()


if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()