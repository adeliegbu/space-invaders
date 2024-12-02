import tkinter as tk
from PIL import Image, ImageTk

from visuel.rules import rules_text

class View:
    def __init__(self, controller):
        self.controller = controller

        self.fenetre = tk.Tk()
        self.fenetre.attributes("-fullscreen", True)

        self.screen_width = self.fenetre.winfo_screenwidth()
        self.screen_height = self.fenetre.winfo_screenheight()
        self.x0, self.y0 = self.screen_width // 2, self.screen_height // 2

        self.bg_game_image = Image.open("visuel/background_invader.jpg")
        self.bg_game_image = ImageTk.PhotoImage(self.bg_game_image.resize((self.screen_width, self.screen_height), Image.LANCZOS))

        self.bg_menu_image = Image.open("visuel/bg_menu.jpg")
        self.bg_menu_image = ImageTk.PhotoImage(self.bg_menu_image.resize((self.screen_width, self.screen_height), Image.LANCZOS))

        self.canvas = tk.Canvas(self.fenetre, width=self.screen_width, height=self.screen_height, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.bg_game_id = self.canvas.create_image(0, 0, image=self.bg_game_image, anchor="nw")
        self.bg_menu_id = self.canvas.create_image(0, 0, image=self.bg_menu_image, anchor="nw")

        self.logo_image = ImageTk.PhotoImage(Image.open("visuel/space_logo.png").resize((500, 200), Image.LANCZOS))

        self.alien_image = ImageTk.PhotoImage(Image.open("visuel/alien.png").resize((80, 80), Image.LANCZOS))
        self.alien_type0_image = ImageTk.PhotoImage(Image.open("visuel/alien_type0.png").resize((100, 60), Image.LANCZOS))
        self.alien_type2_image = ImageTk.PhotoImage(Image.open("visuel/alien_type2.png").resize((50, 40), Image.LANCZOS))
        self.alien_images = [self.alien_type0_image, self.alien_image, self.alien_type2_image]

        self.alien_bonus_image = ImageTk.PhotoImage(Image.open("visuel/alien_bonus.png").resize((80, 50), Image.LANCZOS))
        self.projectile_alien = ImageTk.PhotoImage(Image.open("visuel/fire_ball.png").resize((30, 50), Image.LANCZOS))

        self.player_image_green = ImageTk.PhotoImage(Image.open("visuel/player_rafale_green.png"), Image.LANCZOS)
        self.projectile_player_image_green = ImageTk.PhotoImage(Image.open("visuel/projectile_green.png").rotate(90).resize((250, 250), Image.LANCZOS))
        self.player_image_blue = ImageTk.PhotoImage(Image.open("visuel/players_blue.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_blue = ImageTk.PhotoImage(Image.open("visuel/projectile_blue.png").rotate(90).resize((250, 250), Image.LANCZOS))
        self.player_image_purple = ImageTk.PhotoImage(Image.open("visuel/players_purple.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_purple = ImageTk.PhotoImage(Image.open("visuel/projectile_purple.png").rotate(90).resize((250, 250), Image.LANCZOS))
        self.player_image_red = ImageTk.PhotoImage(Image.open("visuel/players_red.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_red = ImageTk.PhotoImage(Image.open("visuel/projectile_red.png").rotate(90).resize((250, 250), Image.LANCZOS))
        self.player_image_yellow = ImageTk.PhotoImage(Image.open("visuel/players_yellow.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_yellow = ImageTk.PhotoImage(Image.open("visuel/projectile_yellow.png").rotate(90).resize((250, 250), Image.LANCZOS))

        self.player_machinegun_image_red = ImageTk.PhotoImage(Image.open("visuel/player_machinegun_red.png"), Image.LANCZOS)

        self.player_images = [self.player_image_green, self.player_image_blue, self.player_image_red, self.player_image_yellow, self.player_image_purple]
        self.projectile_player_images = [self.projectile_player_image_green, self.projectile_player_image_blue, self.projectile_player_image_red, self.projectile_player_image_yellow, self.projectile_player_image_purple]

        self.heart_full_image = ImageTk.PhotoImage(Image.open("visuel/full_life.png").resize((30, 30), Image.LANCZOS))
        self.heart_semi_image = ImageTk.PhotoImage(Image.open("visuel/semi_life.png").resize((30, 30), Image.LANCZOS))
        self.heart_dead_image = ImageTk.PhotoImage(Image.open("visuel/no_life.png").resize((30, 30), Image.LANCZOS))

        self.wall_image = ImageTk.PhotoImage(Image.open("visuel/n_wall.webp").resize((20, 20), Image.LANCZOS))
        self.rules_label = tk.Label(self.canvas, text=str(rules_text), font=("Helvetica", 14), justify=tk.LEFT, bg="yellow", fg="darkblue", padx="30")

        self.button_new_game = tk.Button(self.canvas, text="Nouvelle Partie", command=self.new_game, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_rules = tk.Button(self.canvas, text="Règles", command=self.rules, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_leave = tk.Button(self.canvas, text="Quitter", command=self.leave, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_menu = tk.Button(self.canvas, text="Menu", command=self.menu, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_options = tk.Button(self.canvas, text="Options", command=self.show_options, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")

        # Chargement des images de la police
        self.font_images = {}
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-"
        for char in characters:
            self.font_images[char] = [ImageTk.PhotoImage(Image.open(f"visuel/font/police_space_invaders-{char}.png").resize((size, size), Image.LANCZOS)) for size in [15, 30, 45, 60, 75]]
        self.font_images[":"] = [ImageTk.PhotoImage(Image.open(f"visuel/font/police_space_invaders-doublepoint.png").resize((size, size), Image.LANCZOS)) for size in [15, 30, 45, 60, 75]]

        self.lives_images_list = [None] * 5
        self.image_score = []
        self.image_stage = []


    def new_game(self):
        self.overlay_reset()

        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_leave.place_forget()
        self.button_menu.place_forget()
        self.button_options.place_forget()

        self.controller.new_game()
        self.update(should_update_lives=True, should_update_score=True, should_update_stage=True)

    def rules(self):
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_leave.place_forget()
        self.button_menu.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.display_font_text(rules_text, size=15, pad_x=0, pad_y=10, x=0, y=self.y0)

    def menu(self):
        self.button_new_game.place(x=self.x0, y=self.y0, anchor="center")
        self.button_rules.place(x=self.x0, y=self.y0 + 100, anchor="center")
        self.button_options.place(x=self.x0, y=self.y0 + 200, anchor="center")
        self.button_leave.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.button_menu.place_forget()
        self.rules_label.place_forget()
        self.hide_image_list(self.lives_images_list)
        self.bg_menu_id = self.canvas.create_image(0, 0, image=self.bg_menu_image, anchor="nw")
        # self.logo_id = self.canvas.create_image(self.x0, self.y0 // 2.5, image=self.logo_image, anchor="center")
        self.logo_id = self.display_font_text("space invaders", size=75, pad_x=3, pad_y=10, x=self.x0 // 3 + 50, y=self.y0 // 2.5)

    def leave(self):
        self.fenetre.quit()
        self.image_score.clear()

    def show_options(self):
        self.button_menu.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_leave.place_forget()
        self.button_options.place_forget()
    
    def hide_image_list(self, image_list):
        for image_id in image_list:
            self.canvas.delete(image_id)
    
    def show_image_list(self, image_list):
        for image_id in image_list:
            self.canvas.itemconfigure(image_id, state="normal")
    
    def overlay_reset(self):
        # Supprimer tous les items sauf l'arrière-plan
        for item in self.canvas.find_all():
            if item != self.bg_game_id:
                self.canvas.delete(item)

    def display_lives(self, lives, x, y, difficulty):
        self.hide_image_list(self.lives_images_list)
        j = 0
        for i in range(- difficulty // 2 + 1, difficulty // 2 + 1):
            j += 1
            if j <= lives:
                self.lives_images_list[j-1] = self.canvas.create_image(x + i * 20, y + 45, image=self.heart_full_image, anchor="center")
            elif j - 0.5 == lives:
                self.lives_images_list[j-1] = self.canvas.create_image(x + i * 20, y + 45, image=self.heart_semi_image, anchor="center")
            else:
                self.lives_images_list[j-1] = self.canvas.create_image(x + i * 20, y + 45, image=self.heart_dead_image, anchor="center")
    
    def update(self, should_update_lives, should_update_score, should_update_stage):
        if should_update_lives:
            self.display_lives(self.controller.p1.life, self.controller.p1.x, self.controller.p1.y, difficulty=5)
        if should_update_score:
            if self.image_score:
                self.hide_image_list(self.image_score[0])
            self.image_score = self.display_font_text(f"Score : {self.controller.score}", size=30, pad_x=2, pad_y=0, x= 20, y=20)
        if should_update_stage:
            if self.image_stage:
                self.hide_image_list(self.image_stage[0])
            self.image_stage = self.display_font_text(f"Stage : {self.controller.stage_number}", size=30, pad_x=2, pad_y=0, x=self.x0 - 100, y=20)

    def display_font_text(self, text, size, pad_x, pad_y, x, y):
        text_ids = [[]]
        i = 0
        for c in text:
            if c == " ":
                text_ids[i].append(None)
            elif c == "\n":
                text_ids.append([])
                i += 1   
            else:
                c = c.upper()
                text_ids[i].append(self.font_images[c][size // 15 - 1])

        for i in range(len(text_ids)):
            for j in range(len(text_ids[i])):
                if text_ids[i][j] is not None:
                    text_ids[i][j] = self.canvas.create_image(x + ((size + pad_x) * j), y + ((size + pad_y) * i), image=text_ids[i][j], anchor="center")

        return text_ids