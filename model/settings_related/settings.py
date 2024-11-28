
class Settings:
    def __init__(self, view):
        self.view = view
        self.choiced_index = 0

    def next_option(self):
        self.choiced_index = (self.choiced_index + 1) % len(self.view.player_images)

    def prev_option(self):
        self.choiced_index = (self.choiced_index - 1) % len(self.view.player_images)
    
    def reset_option(self):
        self.choiced_index = 0