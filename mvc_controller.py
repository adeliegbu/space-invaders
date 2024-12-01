from random import choice

from mvc_model import Players, Aliens, Cooldown, Walls, Players_projectiles, Aliens_projectiles, Binds, P1_settings, Weapons
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)
        self.canvas = self.view.canvas

        self.refresh_rate = 25
        self.score = 0

        self.players_projectiles = Players_projectiles(self.view.canvas, self.refresh_rate, self.view.projectile_player_image_green)
        self.aliens_projectiles = Aliens_projectiles(self.view.canvas, self.refresh_rate, self.view.projectile_alien)

        self.players = Players(self.view.canvas, self.refresh_rate, self.players_projectiles)
        self.players_number = 1
        self.p1, self.p2 = None, None
        
        self.aliens = Aliens(self.view.canvas, self.refresh_rate, image=self.view.alien_image, bonus_image=self.view.alien_bonus_image, projectile_class=self.aliens_projectiles, aliens_projectile_image=self.view.projectile_alien)

        self.walls = Walls(self.view.canvas, self.refresh_rate, self.view.wall_image)

        self.binds = Binds(self.view.canvas)
        self.p1_settings = P1_settings(self.view)

        self.should_game_update = False
        self.should_menu_update = True
        self.stage_number = 0
    
    def game_update(self):
        if self.should_game_update:

            self.binds.execute_active_binds()

            self.aliens.move()
            self.aliens.shoot()

            self.players_projectiles.move()
            self.aliens_projectiles.move()

            collision, alien, _ = self.players_projectiles.collision(self.aliens)
            if collision and alien.dead(): # Evite qu'un alien donne du score  si il meurt à cause d'un mur
                self.score += 10 * alien.level
                if alien.doctor:
                    for players in self.players.objects_list:
                        players.new_life()

            self.players_projectiles.collision(self.walls)
            self.aliens_projectiles.collision(self.players)
            self.aliens_projectiles.collision(self.walls)
            self.aliens.collision(self.players)
            self.aliens.collision(self.walls)

            self.players.update_weapons()
            self.aliens.var_update()

            if self.p1 is not None:
                self.view.update(should_update_lives=True, should_update_score=False)

            if self.aliens.objects_dead():
                self.stage_update()

            if self.players.objects_dead():
                self.go_to_menu()
                    
            self.view.canvas.after(self.refresh_rate, self.game_update)

    def stage_update(self):
        if self.aliens_projectiles.objects_dead():  # Transition entre les stages
            self.aliens.reset()
            self.players_projectiles.reset()
            self.aliens_projectiles.reset()
            self.walls.reset()

            self.stage_number += 1

            self.aliens.create_objects_matrix(line=3, column=5)
            self.aliens.increase_aliens_level(self.stage_number, self.view.alien_images)
            self.aliens.increase_speed(self.stage_number - 1)
            self.walls.add_object(self.view.screen_height * 4 // 5, 2)
            self.players.reset_weapons()
            
    def menu_update(self):
        if self.should_menu_update:
            self.binds.execute_active_binds()
            
            self.view.canvas.after(self.refresh_rate, self.menu_update)
    
    def new_game(self):
        self.should_game_update = True
        self.should_menu_update = False
        self.players.add_object(self.view.screen_width // 2, self.view.screen_height * 28 // 30, self.view.player_machinegun_image_red, self.view.projectile_player_image_red, weapon_type="machine_gun") 
        self.p1 = self.players.define_player(1)
        self.p2 = self.players.define_player(2)

        self.stage_number = 0
        self.stage_update()

        self.default_game_binds()
        self.game_update()
    
    def go_to_menu(self):
        self.should_game_update = False
        self.should_menu_update = True
        self.stage_number = 0
        self.score = 0
        self.reset()
        self.aliens.reset_number_alien_killed()
        self.binds.reset_binds() 
        self.view.menu()
        self.menu_update()

    def default_game_binds(self):
        self.binds.add_bind((self.p1.move_left, True), "Left")
        self.binds.add_bind((self.p1.move_right, True), "Right")
        self.binds.add_bind((self.p1.shoot, True), "space")
        self.binds.add_bind((self.p1.weapon.reload, False), "r")
        self.binds.add_bind((self.go_to_menu, False), "Escape")

    def reset(self):
        self.aliens.reset()
        self.players.reset()
        self.players_projectiles.reset()
        self.aliens_projectiles.reset()
        self.walls.reset()
    
    def run(self):
        self.menu_update()
        self.go_to_menu()
        self.view.fenetre.mainloop()

if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()