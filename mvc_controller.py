from mvc_model import Players, Aliens, Cooldown, Walls, Players_projectiles, Aliens_projectiles, Binds, Game_logic, P1_settings
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)

        self.score = 0
        self.keys_pressed = set()
        self.updating = False

        self.players_projectiles = Players_projectiles(self.view.canvas, self.view.projectile_player_image_green)
        self.aliens_projectiles = Aliens_projectiles(self.view.canvas, self.view.projectile_alien)

        self.players = Players(self.view.canvas)
        self.players_number = 1
        self.p1, self.p2 = None, None
        
        self.aliens = Aliens(self.view.canvas, image=self.view.alien_image, bonus_image=self.view.alien_bonus_image, cooldown=Cooldown(600))

        self.walls = Walls(self.view.canvas, self.view.wall_image)

        self.binds = Binds(self.view.canvas)
        self.p1_settings = P1_settings(self.view)

        self.refresh_rate = 25
 
        self.canvas = self.view.canvas
        self.game_refresh_rate = 25
        self.menu_refresh_rate = 200
        self.should_game_update = False
        self.should_menu_update = True
        self.stage_number = 1
    
    
    def game_update(self):
        if self.lost():
            self.should_game_update = False
            self.should_menu_update = True
            self.view.menu()

        if self.should_game_update:
            for active_bind in self.binds.active_binds:
                active_bind()
            
            self.aliens.move()
            self.aliens.shoot(self.aliens_projectiles)

            self.players_projectiles.move()
            self.aliens_projectiles.move()

            self.players_projectiles.collision(self.aliens, self.walls)
            self.aliens_projectiles.collision(self.players, self.walls)

            self.players.update_cooldown()
            self.aliens.var_update(self.view.alien_image)
            self.stage_update()
        
            if self.players.objects_dead():
                self.lost()

            self.view.canvas.after(self.refresh_rate, self.game_update)
    
    def menu_update(self):
        if self.should_menu_update:
            for active_bind in self.binds.active_binds:
                active_bind()
            
            self.view.canvas.after(self.menu_refresh_rate, self.menu_update)
    
    def new_game(self):
        self.should_game_update = True
        self.should_menu_update = False
        self.players.add_object(self.view.screen_width // 2, self.view.screen_height * 19 // 20, self.p1_settings.get_choiced_player1_image(), Cooldown(300), self.players_projectiles)
        self.p1 = self.players.define_player(1)
        self.p2 = self.players.define_player(2)
        self.aliens.create_objects_matrix(line=4, column=7)
        self.walls.add_object(self.view.screen_height * 4 // 5, 4)

        self.stage_number = 1
        self.default_game_binds()
        self.game_update()

    def stage_update(self):
        if self.aliens.objects_dead():
            temporary = self.stage_number
            self.reset()
            self.stage_number = temporary
            self.should_game_update = True
            self.should_menu_update = False

            self.aliens.create_objects_matrix(line=4, column=7)
            self.aliens.increase_speed(self.stage_number - 1)
            self.walls.add_object(self.view.screen_height * 4 // 5, 4)
            self.aliens.cooldown.reset()
            self.players.reset_cooldown()

            self.stage_number += 1
            
    def lost(self):     # à modifier pour afficher écran de fin de game
        return self.players.objects_dead()
    
    def reset(self):
        self.should_game_update = False
        self.should_menu_update = True
        self.stage_number = 1
        self.aliens.reset()
        self.players.reset()
        self.players_projectiles.reset()
        self.aliens_projectiles.reset()
        self.walls.reset()
    
    def default_game_binds(self):
        self.binds.game_binds_dico = {
            self.p1.move_left: "Left",
            self.p1.move_right: "Right",
            self.p1.shoot: "space",
            self.reset: "Escape"
        }
    
    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()

if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()