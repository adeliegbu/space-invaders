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

        self.bg_image = Image.open("visuel/background_invader.jpg")
        self.bg_image = ImageTk.PhotoImage(self.bg_image.resize((self.screen_width, self.screen_height), Image.LANCZOS))

        self.canvas = tk.Canvas(self.fenetre, width=self.screen_width, height=self.screen_height, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.logo_image = ImageTk.PhotoImage(Image.open("visuel/space_logo.png").resize((500, 200), Image.LANCZOS))

        self.alien_image = ImageTk.PhotoImage(Image.open("visuel/alien.png").resize((80, 80), Image.LANCZOS))
        self.alien_type0_image = ImageTk.PhotoImage(Image.open("visuel/alien_type0.png").resize((70, 40), Image.LANCZOS))
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

        self.wall_image = ImageTk.PhotoImage(Image.open("visuel/wall.jpg").resize((20, 20), Image.LANCZOS))
        self.rules_label = tk.Label(self.canvas, text=str(rules_text), font=("Helvetica", 14), justify=tk.LEFT, bg="yellow", fg="darkblue", padx="30")

        self.button_new_game = tk.Button(self.canvas, text="Nouvelle Partie", command=self.new_game, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_rules = tk.Button(self.canvas, text="Règles", command=self.rules, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_leave = tk.Button(self.canvas, text="Quitter", command=self.leave, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_menu = tk.Button(self.canvas, text="Menu", command=self.menu, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_options = tk.Button(self.canvas, text="Options", command=self.show_options, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")

    def new_game(self):
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_leave.place_forget()
        self.button_menu.place_forget()
        self.button_options.place_forget()
        self.canvas.delete(self.logo_id)

        self.controller.new_game()

    def rules(self):
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_leave.place_forget()
        self.button_menu.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.rules_label.place(x=self.x0, y=self.y0 + 50, anchor="center")

    def menu(self):
        self.button_new_game.place(x=self.x0, y=self.y0, anchor="center")
        self.button_rules.place(x=self.x0, y=self.y0 + 100, anchor="center")
        self.button_options.place(x=self.x0, y=self.y0 + 200, anchor="center")
        self.button_leave.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.button_menu.place_forget()
        self.rules_label.place_forget()
        self.logo_id = self.canvas.create_image(self.x0, self.y0 // 2.5, image=self.logo_image, anchor="center")

    def leave(self):
        self.fenetre.quit()

    def show_options(self):
        self.button_menu.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_leave.place_forget()
        self.button_options.place_forget()


