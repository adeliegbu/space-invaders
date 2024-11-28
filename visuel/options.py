from PIL import Image, ImageTk

class Options:
    def __init__(self, view):
        self.view = view

        self.player_images = [self.view.player_image_green, self.view.player_image_blue, self.view.player_image_red, self.view.player_image_yellow, self.view.player_image_purple]
        self.projectile_player_images = [self.view.projectile_player_image_green, self.view.projectile_player_image_blue, self.view.projectile_player_image_red, self.view.projectile_player_image_yellow, self.view.projectile_player_image_purple]

        self.current_player_image = self.player_images[0]
        self.current_projectile_image = self.projectile_player_images[0]
        self.current_index = 0

    def set_player_color(self, index):
        if index >= 0 and index < len(self.player_images):
            self.current_player_image = self.player_images[index]
            self.current_projectile_image = self.projectile_images[index]
            self.current_index = index 

    def set_player_color(self):
        return self.current_player_image
    
    def set_projectile_color(self):
        return self.current_projectile_image
    
    def next_color(self):
        new_index = (self.current_index + 1) % len(self.player_images)
        self.set_player_color(new_index)

    def prev_color(self):
        new_index = (self.current_index - 1) % len(self.player_images)
        self.set_player_color(new_index)