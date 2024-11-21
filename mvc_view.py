"""
objectif : Mettre en place l'interface visuel de Space Invaders.
date :  15 nov 2024
par : Loann CORDEL, Adélie GIBOU
"""

import tkinter as tk
from PIL import Image, ImageTk
from visuel.regles import rules_text

class View:
    def __init__(self):
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
        self.alien_image = ImageTk.PhotoImage(Image.open("visuel/alien.jpg").resize((50,35), Image.LANCZOS))
        self.projectile_image = ImageTk.PhotoImage(Image.open("visuel/projectile.png").rotate(90).resize((150,70), Image.LANCZOS))

        self.rules_window = tk.Label(self.canvas, text=str(rules_text),font=("Helvetica", 14), justify=tk.LEFT, bg="yellow", fg="darkblue", padx="30")

        self.button_new_game = Button(self.canvas, "Nouvelle Partie", self.new_game, self.x0, self.y0)
        self.button_rules = Button(self.canvas, "Règles", self.rules, self.x0, self.y0 + 100)
        self.button_leave = Button(self.canvas, "Quitter", self.leave, self.x0, self.y0 + 200)
        self.button_menu = Button(self.canvas, "Menu", self.menu, self.x0, self.y0 + 280)

        self.menu()

    def new_game(self):
        self.button_new_game.hide()
        self.button_rules.hide()
        self.button_leave.hide()
        self.canvas.delete(self.canvas.create_image(self.x0, self.y0 // 5, image=self.logo_image, anchor="n"))
        self.game()

    def rules(self):
        self.button_new_game.hide()
        self.button_rules.hide()
        self.button_leave.hide()
        self.button_menu.show()
        self.canvas.create_window(self.x0, self.y0 + 50, anchor="center", window=self.rules_window)

    def menu(self):
        self.button_new_game.show()
        self.button_rules.show()
        self.button_leave.show()
        self.button_menu.hide()
        self.canvas.delete(self.canvas.create_window(self.x0, self.y0 + 50, anchor="center", window=self.rules_window))
        self.canvas.create_image(self.x0, self.y0 // 5, image=self.logo_image, anchor="n")
        # self.canvas.create_image(self.x0, self.y0 // 10, image=self.alien_image, anchor="n")
        # self.canvas.create_image(self.x0, self.y0 // 10, image=self.projectile_image, anchor="n")

    def leave(self):
        self.fenetre.destroy()

    def run(self):
        self.fenetre.mainloop()



if __name__ == "__main__":
    app = View()
    app.run()
