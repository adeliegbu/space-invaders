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
        self.player_image = ImageTk.PhotoImage(Image.open("visuel/invaders.webp").resize((100, 100), Image.LANCZOS))
        self.alien_image = ImageTk.PhotoImage(Image.open("visuel/alien.jpg").resize((50, 35), Image.LANCZOS))
        self.projectile_image = ImageTk.PhotoImage(Image.open("visuel/projectile.png").rotate(90).resize((150, 70), Image.LANCZOS))
        self.wall_image = ImageTk.PhotoImage(Image.open("visuel/wall.jpg").resize((50, 50), Image.LANCZOS))
        self.rules_label = tk.Label(self.canvas, text=str(rules_text), font=("Helvetica", 14), justify=tk.LEFT, bg="yellow", fg="darkblue", padx="30")

        self.button_new_game = tk.Button(self.canvas, text="Nouvelle Partie", command=self.new_game, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_rules = tk.Button(self.canvas, text="Règles", command=self.rules, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_leave = tk.Button(self.canvas, text="Quitter", command=self.leave, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")
        self.button_menu = tk.Button(self.canvas, text="Menu", command=self.menu, font=("Helvetica", 12, "bold"), height=2, width=10, bg="yellow", fg="darkblue", padx="30")

    def new_game(self):
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_leave.place_forget()
        self.button_menu.place(x=2 * self.x0 - 10, y=10, anchor="ne")
        self.canvas.delete(self.logo_id)
        self.controller.main()

    def rules(self):
        self.button_new_game.place_forget()
        self.button_rules.place_forget()
        self.button_leave.place_forget()
        self.button_menu.place(x=self.x0, y=self.y0 + 300, anchor="center")
        self.rules_label.place(x=self.x0, y=self.y0 + 50, anchor="center")

    def menu(self):
        self.button_new_game.place(x=self.x0, y=self.y0, anchor="center")
        self.button_rules.place(x=self.x0, y=self.y0 + 100, anchor="center")
        self.button_leave.place(x=self.x0, y=self.y0 + 200, anchor="center")
        self.button_menu.place_forget()
        self.rules_label.place_forget()
        self.logo_id = self.canvas.create_image(self.x0, self.y0 // 2.5, image=self.logo_image, anchor="center")
        self.controller.stop_update()
        self.controller.player.dead()
        for alien in self.controller.aliens:
            alien.dead()
        for projectile in self.controller.projectiles:
            projectile.out_of_screen()


    def leave(self):
        self.fenetre.quit()