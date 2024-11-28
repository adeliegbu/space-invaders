from model.player_related.player_ship import Player_ship
from model.parents_class.group_object import Group_object

class Players(Group_object):
    def __init__(self, canvas):
        super().__init__(canvas)

    def add_object(self, x, y, image, cooldown):
        super().add_object(Player_ship(self.canvas, x, y, image, cooldown))
    
    def define_player(self, player_number):
        if player_number <= len(self.objects_list):
            return self.objects_list[player_number - 1]
        return None
    
    def is_player_dead(self, player):
        return player in self.objects_list

    def update_cooldown(self):
        for player in self.objects_list:
            player.update_cooldown()
    
    def reset_cooldown(self):
        for player in self.objects_list:
            player.cooldown.reset()
