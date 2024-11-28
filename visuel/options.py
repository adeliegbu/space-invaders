from PIL import Image, ImageTk

class Options:
    def __init__(self):

        self.player_image_green = ImageTk.PhotoImage(Image.open("visuel/players_green.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_green = ImageTk.PhotoImage(Image.open("visuel/projectile_green.png").rotate(90).resize((250, 250), Image.LANCZOS))
        self.player_image_blue = ImageTk.PhotoImage(Image.open("visuel/players_blue.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_blue = ImageTk.PhotoImage(Image.open("visuel/projectile_blue.png").rotate(90).resize((250, 250), Image.LANCZOS))
        self.player_image_purple = ImageTk.PhotoImage(Image.open("visuel/players_purple.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_purple = ImageTk.PhotoImage(Image.open("visuel/projectile_purple.png").rotate(90).resize((250, 250), Image.LANCZOS))
        self.player_image_red = ImageTk.PhotoImage(Image.open("visuel/players_red.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_red = ImageTk.PhotoImage(Image.open("visuel/projectile_red.png").rotate(90).resize((250, 250), Image.LANCZOS))
        self.player_image_yellow = ImageTk.PhotoImage(Image.open("visuel/players_yellow.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_yellow = ImageTk.PhotoImage(Image.open("visuel/projectile_yellow.png").rotate(90).resize((250, 250), Image.LANCZOS))


        self.player_images = [self.player_image_green, self.player_image_blue, self.player_image_red, self.player_image_yellow, self.player_image_purple]
        self.projectile_player_images = [self.projectile_player_image_green, self.projectile_player_image_blue, self.projectile_player_image_red, self.projectile_player_image_yellow, self.projectile_player_image_purple]

        self.current_player_image = self.player_image_green
        self.current_projectile_image = self.projectile_player_image_green
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