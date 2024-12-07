from mvc_model import Players, Aliens, Walls, Players_projectiles, Aliens_projectiles, Binds, Upgrade_settings
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)
        self.canvas = self.view.canvas

        self.refresh_rate = 25
        self.score = 0

        self.players_projectiles = Players_projectiles(self.view.canvas, self.refresh_rate)
        self.aliens_projectiles = Aliens_projectiles(self.view.canvas, self.refresh_rate)

        self.players = Players(self.view.canvas, self.refresh_rate, self.players_projectiles)
        self.players_number = 1
        self.p1, self.p2 = None, None
        
        self.aliens = Aliens(self.view.canvas, self.refresh_rate, self.view.alien_skins, projectile_class=self.aliens_projectiles)

        self.walls = Walls(self.view.canvas, self.refresh_rate, self.view.wall_image)

        self.binds = Binds(self.view.canvas)

        self.upgrade_settings = Upgrade_settings()

        self.should_game_update = False
        self.should_menu_update = True
        self.should_stage_update = False
        self.stage_number = 0
        self.skill_points = 0

    def game_update(self):
        if self.should_game_update:

            self.binds.execute_active_binds()

            self.aliens.move()
            self.aliens.shoot()

            self.players_projectiles.move()
            self.aliens_projectiles.move()
            
            should_update_score = False
            collision, alien, _ = self.players_projectiles.collision(self.aliens)
            if collision and alien.dead(): # Evite qu'un alien donne du score si il meurt à cause d'un mur
                self.score += 15 * alien.level
                should_update_score = True
                if alien.type == "doctor":
                    for players in self.players.objects_list:
                        players.upgrade_one_caracteristic("life")
                if alien.type == "bonus":
                    self.skill_points += 1
                    self.view.update(None, None, None, should_update_skill_points=True)

            self.players_projectiles.collision(self.walls)
            self.aliens_projectiles.collision(self.players)
            self.aliens_projectiles.collision(self.walls)
            self.aliens.collision(self.players)
            self.aliens.collision(self.walls)

            self.players.update_weapons()
            self.aliens.var_update()

            if self.p1 is not None:
                self.view.update(should_update_lives=True, should_update_score=should_update_score, should_update_stage=False, should_update_skill_points=False)

            if self.aliens.objects_dead():
                self.should_stage_update = True
                self.stage_update()

            if self.players.objects_dead():
                self.go_to_menu()
                    
            self.view.canvas.after(self.refresh_rate, self.game_update)

    def stage_update(self):
        if self.aliens_projectiles.objects_dead() and self.should_stage_update:  # Transition entre les stages
            self.should_game_update = False
            if self.upgrade_settings.choosing is False and self.upgrade_settings.choosing is not None:
                self.aliens.reset()
                self.players_projectiles.reset()
                self.aliens_projectiles.reset()
                self.walls.reset()
                self.players.reset_weapons()

                self.stage_number += 1

                self.view.update(None, None, should_update_stage=True, should_update_skill_points=None)

                if self.stage_number > 1:
                    self.binds.change_current_binds_dico(self.binds.upgrade_binds_dico) # Change les binds pour les binds de l'upgrade
                    self.skill_points += 1
                    self.view.update(None, None, None, should_update_skill_points=True)
                    self.view.display_upgrade_stage()
                    self.upgrade_settings.choosing = True
                else:
                    self.next_stage()

            if self.stage_number > 1:
                self.binds.execute_active_binds()
                self.view.display_choosing_card()

                if self.upgrade_settings.choosing:
                    self.canvas.after(self.refresh_rate, self.stage_update)
                elif self.upgrade_settings.choosing is None:
                    self.next_stage()
                elif self.skill_points >= self.upgrade_settings.choiced_price():
                    self.skill_points -= self.upgrade_settings.choiced_price()
                    self.p1.upgrade_one_caracteristic(self.upgrade_settings.get_choiced_option())
                    self.view.update(None, None, None, should_update_skill_points=True)
                    self.upgrade_settings.choosing = True
                    self.canvas.after(self.refresh_rate, self.stage_update)
                else:
                    self.upgrade_settings.choosing = True
                    self.canvas.after(self.refresh_rate, self.stage_update)

    def next_stage(self):
        self.should_stage_update = False
        self.upgrade_settings.choosing = False
        self.upgrade_settings.reset_option()
        self.view.cards_choosing_index = 0
        self.view.hide_image_list(self.view.image_upgrade_cards)
        self.view.hide_image_list(self.view.upgrade_text)
        self.view.image_upgrade_cards = []
        
        self.p1.weapon.reset()
        self.aliens.create_objects_matrix(line=3, column=5)
        self.aliens.increase_aliens_level(self.stage_number)
        self.aliens.increase_speed(self.stage_number // 2)
        self.walls.add_object(self.view.screen_height * 15 // 20, 2)
        self.should_game_update = True
        self.binds.change_current_binds_dico(self.binds.game_binds_dico)
        self.view.update(None, None, should_update_stage=True, should_update_skill_points=True)
        self.game_update()
        
    def menu_update(self):
        if self.should_menu_update:
            self.binds.execute_active_binds()
            
            self.view.canvas.after(self.refresh_rate, self.menu_update)
    
    def new_game(self):
        self.should_game_update = True
        self.should_menu_update = False
        self.players.add_object(self.view.screen_width // 2, self.view.screen_height * 28 // 30, self.view.player_image_green, self.view.projectile_player_image_red, weapon_type="rafale") 
        self.p1 = self.players.define_player(1)
        self.p2 = self.players.define_player(2)

        self.stage_number = 0
        self.should_stage_update = True
        self.game_binds()
        self.stage_update()
    
    def go_to_menu(self):
        self.should_game_update = False
        self.should_stage_update = False
        self.should_menu_update = True
        self.stage_number = 0
        self.skill_points = 0
        self.score = 0
        self.reset()
        self.binds.reset_binds()
        self.binds.change_current_binds_dico(self.binds.menu_binds_dico)
        self.aliens.reset_number_alien_killed()
        self.view.menu()
        self.menu_update()

    def default_binds(self):
        self.binds.add_bind((self.upgrade_settings.next_option, False), "Right", self.binds.upgrade_binds_dico)
        self.binds.add_bind((self.upgrade_settings.prev_option, False), "Left", self.binds.upgrade_binds_dico)
        self.binds.add_bind((self.upgrade_settings.chose_option, False), "Return", self.binds.upgrade_binds_dico)
        self.binds.add_bind((self.upgrade_settings.chose_none, False), "Escape", self.binds.upgrade_binds_dico)

    def game_binds(self):
        self.binds.add_bind((self.p1.move_left, True), "q", self.binds.game_binds_dico)
        self.binds.add_bind((self.p1.move_right, True), "d", self.binds.game_binds_dico)
        self.binds.add_bind((self.p1.shoot, True), "space", self.binds.game_binds_dico)
        self.binds.add_bind((self.p1.weapon.reload, False), "r", self.binds.game_binds_dico)
        self.binds.add_bind((self.go_to_menu, False), "Escape", self.binds.game_binds_dico)
        self.binds.add_bind((self.cheat_next_stage, False), "n", self.binds.game_binds_dico)
    
    def cheat_next_stage(self):
        self.players_projectiles.reset()
        self.aliens_projectiles.reset()
        self.aliens.reset()
    
    def reset(self):
        self.aliens.reset()
        self.players.reset()
        self.players_projectiles.reset()
        self.aliens_projectiles.reset()
        self.walls.reset()
    
    def run(self):
        self.menu_update()
        self.go_to_menu()
        self.default_binds()
        self.view.root.mainloop()