from model.player_related.player_ship import Player_ship
from model.parents_class.group_object import Group_object
from model.weapon_related.weapons import Weapons

class Players(Group_object):
    def __init__(self, canvas, refresh_rate, projectille_class):
        super().__init__(canvas, refresh_rate)
        self.projectille_class = projectille_class

    def add_object(self, x, y, image, projectile_image, weapon_type):
        new_player = Player_ship(self.canvas, x, y, image, self.refresh_rate, self.projectille_class, projectile_image)
        new_player.weapon = Weapons(new_player, (weapon_type, "player"), self.projectille_class, projectile_image)
        super().add_object(new_player)
    
    def define_player(self, player_number):
        if player_number <= len(self.objects_list):
            return self.objects_list[player_number - 1]
        return None

    def update_weapons(self):
        for player in self.objects_list:
            player.weapon.update()
    
    def reset_weapons(self):
        for player in self.objects_list:
            player.weapon.reset()
