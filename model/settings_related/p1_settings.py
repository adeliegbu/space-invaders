from model.settings_related.settings import Settings

class P1_settings(Settings):
    def __init__(self, view):
        super().__init__(view)

    def get_choiced_player1_image(self):
        return self.view.player_images[self.choiced_index]

    def get_choiced_player1_projectile_image(self):
        return self.view.projectile_player_images[self.choiced_index]

