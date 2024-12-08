import tkinter as tk
from PIL import Image, ImageTk

from visuel.rules import rules_text

class View:
    def __init__(self, controller):
        self.controller = controller

        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x0, self.y0 = self.screen_width // 2, self.screen_height // 2

        self.canvas = tk.Canvas(self.root, width=self.screen_width, height=self.screen_height, highlightthickness=0, cursor="none")
        self.canvas.pack(fill="both", expand=True)

        self.bg_game_image = ImageTk.PhotoImage(Image.open("visuel/background_invader.jpg").resize((self.screen_width, self.screen_height), Image.LANCZOS))
        self.bg_menu_image = ImageTk.PhotoImage(Image.open("visuel/bg_menu.jpg").resize((self.screen_width, self.screen_height), Image.LANCZOS))

        self.bg_game_id = self.canvas.create_image(0, 0, image=self.bg_game_image, anchor="nw")
        self.bg_menu_id = self.canvas.create_image(0, 0, image=self.bg_menu_image, anchor="nw")

        self.logo_image = ImageTk.PhotoImage(Image.open("visuel/space_logo.png").resize((self.screen_width // 3, self.screen_height // 6), Image.LANCZOS))

        # Chargement des images des aliens
        self.alien_skins = {}
        types = ["assault", "rafale", "machine_gun", "sniper", "tank"]
        for type in types:
            self.alien_skins[type] = [ImageTk.PhotoImage(Image.open(f"visuel/alien_skins/alien_{type}_{i}.png").resize((self.screen_height // 20, self.screen_height // 22), Image.LANCZOS)) for i in range (1, 6)]
        self.alien_skins["basic"] = ImageTk.PhotoImage(Image.open(f"visuel/alien_skins/alien__basic.png").resize((self.screen_height // 13, self.screen_height // 13), Image.LANCZOS))
        self.alien_skins["doctor"] = ImageTk.PhotoImage(Image.open(f"visuel/alien_skins/alien__doctor.png").resize((self.screen_height // 19, self.screen_height // 22), Image.LANCZOS))
        self.alien_skins["bonus"] = ImageTk.PhotoImage(Image.open(f"visuel/alien_skins/alien__bonus.png").resize((self.screen_height // 11, self.screen_height // 18), Image.LANCZOS))
        self.alien_skins["projectile"] = ImageTk.PhotoImage(Image.open("visuel/fire_ball.png").resize((30, 50), Image.LANCZOS))

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

        self.button_active_image = ImageTk.PhotoImage(Image.open("visuel/button_active.png").resize((int(self.screen_width // 4.5), int(self.screen_height // 13)), Image.LANCZOS))
        self.button_inactive_image = ImageTk.PhotoImage(Image.open("visuel/button_inactive.png").resize((int(self.screen_width // 4.5), int(self.screen_height // 13)), Image.LANCZOS))

        self.wall_image = ImageTk.PhotoImage(Image.open("visuel/n_wall.webp").resize((20, 20), Image.LANCZOS))
        self.rules_label = tk.Label(self.canvas, text=str(rules_text), font=("Helvetica", 14), justify=tk.LEFT, bg="yellow", fg="darkblue", padx="30")

        self.button_new_game = tk.Button(self.canvas, text="Nouvelle Partie", command=self.new_game, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_rules = tk.Button(self.canvas, text="Règles", command=self.rules, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_quit = tk.Button(self.canvas, text="Quitter", command=self.quit, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_menu = tk.Button(self.canvas, text="Menu", command=self.menu, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_options = tk.Button(self.canvas, text="Options", command=self.show_options, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")

        # Chargement des images de la police
        self.font_images = {}
        characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-+"
        for char in characters:
            self.font_images[char] = [ImageTk.PhotoImage(Image.open(f"visuel/font/police_space_invaders-{char}.png").resize((size, size), Image.LANCZOS)) for size in [self.screen_height // 50, self.screen_height // 45, self.screen_height // 40, self.screen_height // 35, self.screen_height // 30, self.screen_height // 25]]
        self.font_images[":"] = [ImageTk.PhotoImage(Image.open(f"visuel/font/police_space_invaders-doublepoint.png").resize((size, size), Image.LANCZOS)) for size in [self.screen_height // 50, self.screen_height // 45, self.screen_height // 40, self.screen_height // 35, self.screen_height // 30, self.screen_height // 25]]

        self.upgrade_images = {}
        upgrades = ["cooldown", "cooldown_reload", "damage", "power", "rafale", "imprecision", "munitions", "speed", "life", "auto_reload"]
        upgrade_prices = [2, 1, 4, 2, 5, 2, 3, 1, 7, 3]
        upgrade_texts = ["-30 cooldown", "-50 cd recharge", "+1 degats", "+2 puissance", "+1 rafale", "+3 precision", "+3 munitions", "+1 vitesse", "+1 vie", "recharge auto"]
        i = 0
        for upgrade in upgrades:
            self.upgrade_images[upgrade] = [ImageTk.PhotoImage(Image.open(f"visuel/upgrade_cards/up_{upgrade}.png").resize((125, 200), Image.LANCZOS)), upgrade_prices[i], upgrade_texts[i]]
            i += 1

        self.lives_images_list = [None] * 5
        self.image_score = []
        self.image_stage = []
        self.image_upgrade_points = []
        self.image_upgrade_cards = []
        self.cards_choosing_index = 0
        self.upgrade_text = []
        self.binds_overlay = []
        self.menu_overlay = []
        self.menu_choosing_index = 0

    def new_game(self):
        self.overlay_reset()

        self.hide_image_list(self.menu_overlay)
        self.canvas.delete(self.logo_id)
        self.binds_overlay = self.display_font_text("menu:Echap\ncheats:c", alignment="right", size=1, pad_x=2, pad_y=10, x=self.screen_width - 20, y= 20)

        self.controller.new_game()
        self.update(should_update_lives=True, should_update_score=True, should_update_stage=True, should_update_skill_points=False)

    def rules(self):
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_quit.place_forget()
        self.button_menu.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.display_font_text(rules_text, alignment="left", size=0, pad_x=0, pad_y=10, x=0, y=self.y0 // 2)

    def menu(self):
        # self.button_new_game.place(x=self.x0, y=self.y0, anchor="center")
        # self.button_rules.place(x=self.x0, y=self.y0 + 100, anchor="center")
        # self.button_options.place(x=self.x0, y=self.y0 + 200, anchor="center")
        # self.button_quit.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.button_menu.place_forget()
        self.rules_label.place_forget()
        self.hide_image_list(self.lives_images_list)
        self.bg_menu_id = self.canvas.create_image(0, 0, image=self.bg_menu_image, anchor="nw")
        self.logo_id = self.canvas.create_image(self.x0, self.y0 // 2, image=self.logo_image, anchor="center")
        self.hide_image_list(self.binds_overlay)
        self.display_menu()

    def quit(self):
        self.root.quit()
        self.image_score.clear()

    def show_options(self):
        self.button_menu.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_quit.place_forget()
        self.button_options.place_forget()
    
    def hide_image_list(self, image_list):
        for i in range (len(image_list)):
            if isinstance(image_list[i], list):
                self.hide_image_list(image_list[i])
            elif image_list[i] is not None:
                self.canvas.delete(image_list[i])

    def show_image_list(self, image_list):
        for image_id in [item for sublist in image_list for item in sublist]:
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
    
    def update(self, should_update_lives, should_update_score, should_update_stage, should_update_skill_points):
        if should_update_lives:
            self.display_lives(self.controller.p1.life, self.controller.p1.x, self.controller.p1.y, difficulty=5)
        if should_update_score:
            if self.image_score:
                self.hide_image_list(self.image_score)
            self.image_score = self.display_font_text(f"Score:{self.controller.score}", alignment="left", size=2, pad_x=2, pad_y=0, x= 20, y=20)
        if should_update_stage:
            if self.image_stage:
                self.hide_image_list(self.image_stage)
            self.image_stage = self.display_font_text(f"Stage:{self.controller.stage_number}", alignment="center",size=2, pad_x=2, pad_y=0, x=self.x0, y=20)
        if should_update_skill_points:
            if self.image_upgrade_points:
                self.hide_image_list(self.image_upgrade_points)
            self.image_upgrade_points = self.display_font_text(f"sp:{self.controller.skill_points}", alignment="left", size=2, pad_x=2, pad_y=0, x=20, y=60)

    def display_font_text(self, text, alignment, size, pad_x, pad_y, x, y):
        text_ids = [[]]
        i = 0
        for c in text:
            if c == " ":
                text_ids[i].append(None)
            elif c == "\n":
                text_ids.append([])
                i += 1   
            elif c in self.font_images or c.upper() in self.font_images:
                c = c.upper()
                text_ids[i].append(self.font_images[c][size])
            else:
                raise ValueError(f"Caractère {c} non reconnu")

        for i in range(len(text_ids)):
            line_width = (self.screen_height // (50 - 5 * size) + pad_x) * (len(text_ids[i]) - 1)
            if alignment == "center":
                offset_x = x - line_width // 2
            elif alignment == "right":
                offset_x = x - line_width
            else:  # default to left alignment
                offset_x = x
            for j in range(len(text_ids[i])):
                if text_ids[i][j] is not None:
                    text_ids[i][j] = self.canvas.create_image(offset_x + ((self.screen_height // (50 - 5 * size) + pad_x) * j), y + ((self.screen_height // (50 - 5 * size) + pad_y) * i), image=text_ids[i][j], anchor="center")

        return text_ids

    def display_upgrade_stage(self):
        i = 0
        for upgrade in self.upgrade_images.values():
            self.image_upgrade_cards.append(self.canvas.create_image(self.screen_width // 6 * (i % 5 + 1), self.screen_height // 9 * ((i // 5 * 3) + 4) + 50, image=upgrade[0], anchor="center"))
            self.image_upgrade_cards.append(self.display_font_text(f"prix:{upgrade[1]}sp\n{upgrade[2]}", alignment="center", size=0, pad_x=2, pad_y=10, x=self.screen_width // 6 * (i % 5 + 1), y=self.screen_height * (((i // 5 * 3) + 4) / 9) - 80))
            i += 1
        self.canvas.move(self.image_upgrade_cards[0], 0, 30)
        self.upgrade_text = self.display_font_text("Choisissez une amelioration\nLeft - Right\nEntree pour valider\nEchap pour passer au next stage", alignment="center", size=3, pad_x=2, pad_y=10, x=self.x0, y=self.y0 // 4)
    
    def display_choosing_card(self):
        if self.cards_choosing_index != self.controller.upgrade_settings.get_choiced_index():
            self.canvas.move(self.image_upgrade_cards[self.cards_choosing_index * 2], 0, -30)
            self.cards_choosing_index = self.controller.upgrade_settings.get_choiced_index()
            self.canvas.move(self.image_upgrade_cards[self.cards_choosing_index * 2], 0, 30)
    
    def display_menu(self):
        self.menu_overlay = []
        self.menu_overlay.append([self.canvas.create_image(self.x0, self.screen_height // 8 * (4 + i), image=self.button_inactive_image, anchor="center") for i in range(4)])
        self.menu_overlay.append(self.display_font_text("New game\nRegles\nOptions\nQuitter", alignment="center", size=5, pad_x=2, pad_y=self.screen_height // 8 - self.screen_height // 25, x=self.x0, y=self.y0))
        self.canvas.itemconfig(self.menu_overlay[0][0], image=self.button_active_image)

    def dynamic_menu(self):
        if self.menu_choosing_index != self.controller.menu_settings.get_choiced_index():
            self.canvas.itemconfig(self.menu_overlay[0][self.menu_choosing_index], image=self.button_inactive_image)
            self.menu_choosing_index = self.controller.menu_settings.get_choiced_index()
            self.canvas.itemconfig(self.menu_overlay[0][self.menu_choosing_index], image=self.button_active_image)

