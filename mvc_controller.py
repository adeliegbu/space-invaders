import json
import tkinter as tk

from mvc_model import Players, Aliens, Walls, Players_projectiles, Aliens_projectiles, Binds, Upgrade_settings, Menu_settings, Options_settings
from mvc_view import View

class Controller:
    def __init__(self):
        """
        Initialize the Controller class.
        """
        self.view = View(self)
        self.canvas = self.view.canvas

        self.refresh_rate = 24
        self.score = 0

        self.players_projectiles = Players_projectiles(self.view.canvas, self.refresh_rate)
        self.aliens_projectiles = Aliens_projectiles(self.view.canvas, self.refresh_rate)

        self.players = Players(self.view.canvas, self.refresh_rate, self.players_projectiles)
        self.players_number = 1
        
        self.aliens = Aliens(self.view.canvas, self.refresh_rate, self.view.alien_skins, projectile_class=self.aliens_projectiles)

        self.walls = Walls(self.view.canvas, self.refresh_rate, self.view.wall_image)

        self.upgrade_settings = Upgrade_settings()
        self.menu_settings = Menu_settings()
        self.options_settings = Options_settings()

        self.binds = Binds(self.view.canvas, self.options_settings)

        self.should_game_update = False
        self.should_menu_update = True
        self.should_stage_update = False
        self.stage_number = 0
        self.skill_points = 0

        self.entry = None

    def game_update(self):
        """
        Update the game state.
        """
        if self.should_game_update:

            self.aliens.move()
            self.aliens.shoot()

            self.players_projectiles.move()
            self.aliens_projectiles.move()
            
            should_update_score = False
            collision, alien, _ = self.players_projectiles.collision(self.aliens)
            if collision:   # Prevents an alien from giving score if it dies due to a wall
                if alien.dead():  
                    self.score += 15 * (alien.level + 1)
                    should_update_score = True
                    if alien.type == "doctor":
                        for players in self.players.objects_list:
                            players.upgrade_one_caracteristic("life")
                    if alien.type == "bonus":
                        self.skill_points += 1
                        self.view.update(None, None, None, should_update_skill_points=True)
                else:
                    if alien.type != "doctor":
                        alien.change_image(self.view.alien_skins[alien.weapon.type[0]][alien.life - 1])

            self.players_projectiles.collision(self.walls)
            self.aliens_projectiles.collision(self.players)
            self.aliens_projectiles.collision(self.walls)
            self.aliens.collision(self.players)
            self.aliens.collision(self.walls)

            self.players.update_weapons()
            self.aliens.var_update()

            if self.aliens.objects_dead():
                self.should_stage_update = True
                self.stage_update()

            if self.players.objects_dead():
                self.lost()
                    
            self.binds.execute_active_binds()

            if not self.players.objects_dead():
                self.view.update(should_update_lives=True, should_update_score=should_update_score, should_update_stage=False, should_update_skill_points=False)
            
            self.view.canvas.after(self.refresh_rate, self.game_update)

    def stage_update(self):
        """
        Update the stage.
        """
        if self.aliens_projectiles.objects_dead() and self.should_stage_update:  # Transition between stages
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
                    self.score += 100
                    self.binds.change_current_binds_dico(self.binds.upgrade_binds_dico)  # Change binds for upgrade
                    self.skill_points += 1
                    self.view.update(None, should_update_score=True, should_update_stage=None, should_update_skill_points=True)
                    self.view.display_upgrade_stage()
                    self.upgrade_settings.choosing = True
                else:
                    self.next_stage()

            if self.stage_number > 1:

                self.view.display_choosing_card()
                if self.upgrade_settings.choosing:
                    self.canvas.after(self.refresh_rate, self.stage_update)
                elif self.upgrade_settings.choosing is None:
                    self.next_stage()
                elif self.skill_points >= self.upgrade_settings.choiced_price():
                    self.skill_points -= self.upgrade_settings.choiced_price()
                    self.players.define_player(1).upgrade_one_caracteristic(self.upgrade_settings.get_choiced_option())
                    self.view.update(None, None, None, should_update_skill_points=True)
                    self.upgrade_settings.choosing = True
                    self.canvas.after(self.refresh_rate, self.stage_update)
                else:
                    self.upgrade_settings.choosing = True
                    self.canvas.after(self.refresh_rate, self.stage_update)

                self.binds.execute_active_binds()

    def next_stage(self):
        """
        Proceed to the next stage.
        """
        self.should_stage_update = False
        self.upgrade_settings.choosing = False
        self.upgrade_settings.reset_option()
        self.view.cards_choosing_index = 0
        self.view.hide_image_list(self.view.image_upgrade_cards)
        self.view.hide_image_list(self.view.upgrade_text)
        self.view.image_upgrade_cards = []
        difficulty = self.options_settings.get_choiced_sub_index(1)
        
        for player in self.players.objects_list:
            player.weapon.reset()
        self.aliens.create_objects_matrix(line=3, column=5 + difficulty)
        self.aliens.increase_aliens_level(self.stage_number, difficulty)
        self.aliens.increase_speed(self.stage_number // 2)
        self.walls.add_object(self.view.screen_height * 15 // 20, 3 - difficulty)
        self.should_game_update = True
        self.binds.change_current_binds_dico(self.binds.game_binds_dico)
        self.view.update(None, None, should_update_stage=True, should_update_skill_points=True)
        self.game_update()
        
    def menu_update(self):
        """
        Update the menu state.
        """
        if self.should_menu_update:
            self.binds.execute_active_binds()
            if self.options_settings.choosing:
                self.view.dynamic_options()
                
            elif self.menu_settings.choosing:
                self.view.dynamic_menu()

            else:
                if self.menu_settings.get_choiced_index() == 0:
                    self.should_menu_update = False
                    self.view.new_game()
                elif self.menu_settings.get_choiced_index() == 1:
                    self.view.rules()
                    self.menu_settings.choosing = True
                elif self.menu_settings.get_choiced_index() == 2:
                    self.options_settings.choosing = True
                    self.options_settings.reset_option()
                    self.binds.change_current_binds_dico(self.binds.options_binds_dico)
                    self.view.show_options()
                elif self.menu_settings.get_choiced_index() == 3:
                    self.view.quit()
            
            self.view.canvas.after(self.refresh_rate, self.menu_update)
    
    def new_game(self):
        """
        Start a new game.
        """
        self.should_game_update = True
        self.should_menu_update = False
        self.players.add_object(self.view.screen_width // 2, self.view.screen_height * 28 // 30, self.view.player_skins[self.options_settings.get_choiced_sub_option(2)][self.options_settings.get_choiced_sub_index(3)], self.view.projectile_skins[self.options_settings.get_choiced_sub_option(3)], weapon_type=self.options_settings.get_choiced_sub_option(2), difficulty=self.options_settings.get_choiced_sub_index(1)) 

        self.stage_number = 0
        self.should_stage_update = True
        self.game_binds()
        self.stage_update()
    
    def go_to_menu(self, event):
        """
        Return to the main menu.
        """
        self.canvas.focus_set()
        if self.entry:
            self.entry.destroy()
        self.should_game_update = False
        self.should_stage_update = False
        self.should_menu_update = True
        self.menu_settings.choosing = True
        self.options_settings.choosing = False
        self.stage_number = 0
        self.skill_points = 0
        self.score = 0
        self.reset()
        self.binds.change_current_binds_dico(self.binds.menu_binds_dico)
        self.aliens.reset_number_alien_killed()
        self.view.menu()
        self.menu_update()
        self.canvas.unbind("<Return>")
    
    def lost(self):
        """
        Handle a lost game.
        """
        self.should_game_update = False
        self.should_stage_update = False
        self.reset()
        self.binds.change_current_binds_dico(self.binds.menu_binds_dico)
        self.view.lost()

        pseudo = tk.StringVar()
        self.entry = tk.Entry(self.view.canvas, textvariable=pseudo, width=9, font=("Helvetica", 30), bg="orange", fg="black", justify="center")
        self.entry.place(x=self.view.screen_width / 4, y=self.view.screen_height / 50 * 36, anchor="center")
        self.entry.focus_set()
        self.entry.bind("<Return>", lambda event: self.save_score(pseudo.get(), self.score))
        self.entry.bind("<Escape>", self.go_to_menu)
    
    def save_score(self, pseudo, score):
        """
        Save the player's score.
        """
        with open("options.json", "r") as file:
            data = json.load(file)

        # Ensure all scores are integers
        data[1][pseudo] = score
        for key in data[1]:
            data[1][key] = int(data[1][key])

        # Sort the dictionary by score in descending order
        sorted_data = dict(sorted(data[1].items(), key=lambda item: item[1], reverse=True))
        data[1] = sorted_data

        with open("options.json", "w") as file:
            json.dump(data, file, indent=4)
        
        self.view.lost()

    def default_binds(self):
        """
        Set up the default key bindings.
        """
        self.binds.add_bind((self.upgrade_settings.next_option, False), "Right", self.binds.upgrade_binds_dico)
        self.binds.add_bind((self.upgrade_settings.prev_option, False), "Left", self.binds.upgrade_binds_dico)
        self.binds.add_bind((self.upgrade_settings.chose_option, False), "Return", self.binds.upgrade_binds_dico)
        self.binds.add_bind((self.upgrade_settings.chose_none, False), "BackSpace", self.binds.upgrade_binds_dico)

        self.binds.add_bind((self.menu_settings.next_option, False), "Down", self.binds.menu_binds_dico)
        self.binds.add_bind((self.menu_settings.prev_option, False), "Up", self.binds.menu_binds_dico)
        self.binds.add_bind((self.menu_settings.chose_option, False), "Return", self.binds.menu_binds_dico)

        self.binds.add_bind((self.options_settings.next_option, False), "Down", self.binds.options_binds_dico)
        self.binds.add_bind((self.options_settings.prev_option, False), "Up", self.binds.options_binds_dico)
        self.binds.add_bind((self.options_settings.next_sub_option, False), "Right", self.binds.options_binds_dico)
        self.binds.add_bind((self.options_settings.prev_sub_option, False), "Left", self.binds.options_binds_dico)
        self.binds.add_bind((self.binds.start_getting_new_key, False), "Return", self.binds.options_binds_dico)

        self.canvas.bind("<Escape>", self.go_to_menu)

    def game_binds(self):
        """
        Set up the game key bindings.
        """
        self.binds.reset_game_binds()
        
        with open("options.json", "r") as file:
            data_binds = json.load(file)
        for i in range(len(self.players.objects_list)):
            player = self.players.define_player(i)
            for str_command in data_binds[i]:
                if str_command == "reload":
                    command = getattr(player.weapon, str_command)
                    self.binds.add_bind((command, True), data_binds[i][str_command], self.binds.game_binds_dico)
                else:
                    command = getattr(player, str_command)
                    self.binds.add_bind((command, True), data_binds[i][str_command], self.binds.game_binds_dico)

        self.binds.add_bind((self.cheat_next_stage, False), "n", self.binds.game_binds_dico)
        self.binds.add_bind((self.cheat_lost, False), "l", self.binds.game_binds_dico)
    
    def cheat_next_stage(self):
        """
        Cheat to skip to the next stage.
        """
        self.players_projectiles.reset()
        self.aliens_projectiles.reset()
        self.aliens.reset()
    
    def cheat_lost(self):
        """
        Cheat to lose the game.
        """
        for player in self.players.objects_list:
            self.players.remove_object(player)
    
    def reset(self):
        """
        Reset the game state.
        """
        self.aliens.reset()
        self.players.reset()
        self.players_projectiles.reset()
        self.aliens_projectiles.reset()
        self.walls.reset()
    
    def run(self):
        """
        Run the main loop of the application.
        """
        self.go_to_menu(None)
        self.default_binds()
        self.view.root.mainloop()