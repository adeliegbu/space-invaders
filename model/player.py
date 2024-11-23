from model.player_ship import Player_ship

class Player():
    def __init__(self, canvas, x, y, image, projectile_image):
        self.canvas = canvas   
        self.x = x
        self.y = y
        self.image = image
        self.projectile_image = projectile_image
        self.player = []

    def create_player(self):
        self.x = self.canvas.winfo_width() // 2
        self.player.append(Player_ship(self.canvas, self.x, self.y, image=self.image, projectile_image=self.projectile_image))
    
    def define_player(self, number):
        if number <= len(self.player):
            return True, self.player[number - 1]
        return False, None
    
    def remove_player(self, player):
        if player in self.player:
            player.dead()
            self.player.remove(player)
    
    def delete(self):
        for player in self.player:
            player.dead()
        self.player = []
