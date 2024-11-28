from model.cooldown import Cooldown

class Game_logic():
    def __init__(self, view, binds, options, players, aliens, players_projectiles, aliens_projectiles, walls, refresh_rate):
        self.view = view
        self.binds = binds
        self.options = options
        self.players = players
        self.aliens = aliens
        self.players_projectiles = players_projectiles
        self.aliens_projectiles = aliens_projectiles
        self.wall = walls
        self.game_refresh_rate = refresh_rate
        self.menu_refresh_rate = 100
        self.should_game_update = False
        self.should_menu_update = True
        self.stage_number = 1
    
    def game_update(self):
        if self.should_game_update:
            for active_bind in self.bind.active_binds:
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
            for active_bind in self.bind.active_binds:
                active_bind()
            
            self.view.canvas.after(self.menu_refresh_rate, self.menu_update)
    
    def stage_update(self):
        if self.aliens.objects_dead():
            self.reset()
            self.should_game_update = True

            self.aliens.create_objects_matrix(line=4, column=7)
            self.aliens.increase_speed(self.stage_number - 1)
            self.players.add_object(self.view.screen_width // 2, self.view.screen_height * 4 // 5, self.options.current_player_image, Cooldown(300))  
            self.walls.add_object(self.view.screen_height * 4 // 5, 4)
            self.aliens.cooldown.reset()
            self.players.reset_cooldown()

            self.stage_number += 1
            
    def lost(self):     # à modifier pour afficher écran de fin de game
        self.reset()
    
    def reset(self):
        self.stage_number = 1
        self.should_game_update = False
        self.aliens.reset()
        self.players.reset()
        self.players_projectiles.reset()
        self.aliens_projectiles.reset()
        self.walls.reset()
        
