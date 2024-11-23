from model.player_ship import Player_ship

class Players():
    def __init__(self, canvas):
        self.canvas = canvas
        self.list = []

    def create_player(self, x, y, image):
        self.list.append(Player_ship(self.canvas, x, y, image))
    
    def define_player(self, number):
        if number <= len(self.list):
            return True, self.list[number - 1]
        return False, None
    
    def got_hit(self, player):
        player.got_hit()
        self.remove_player(player)
    
    def remove_player(self, player):
        if player in self.list:
            self.list.remove(player)
    
    def delete(self):
        for player in self.list:
            player.dead()
        self.list = []
