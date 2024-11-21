"""
objectif : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
import tkinter as tk
from PIL import Image, ImageTk

from mvc_model import Player, Alien, Projectile
from mvc_view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.score = 0
        self.life = 3

    def game(self):
        self.view.canvas.bind("<Left>", self.move_left)
        self.view.canvas.bind("<Right>", self.move_right)
        self.view.canvas.bind("<space>", self.shoot)
        self.view.canvas.focus_set()
        self.view.canvas.create_window(self.view.x0, self.view.y0 + 50, anchor="center", window=self.view.button_menu)
        self.view.canvas.create_window(self.view.x0, self.view.y0 + 150, anchor="center", window=self.view.button_leave)

    def alien_hit(self):
        self.score += 10

    def player_hit(self):
        self.life -= 1
    
    def shoot():
        tk.Entry()






def game():
    from mvc_view import canvas, x0, y0
    vaisseau_image = ImageTk.PhotoImage(Image.open("invaders.webp").resize((500, 200), Image.LANCZOS))
    canvas.create_image(x0, y0 // 5, image=vaisseau_image, anchor="n")

