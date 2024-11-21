"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
import tkinter as tk
from PIL import Image, ImageTk

from mvc_model import Vaisseau
from mvc_view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.score = 0
        self.life = 3
        self.player = Vaisseau(self.view.canvas, 9*self.view.x0 // 10, self.view.y0, "player")
        self.aliens = []
        self.projectiles = []
        self.player_image = self.canvas.create_image(self.x0, 9 * self.y0 // 10, image=self.view.player_image, anchor="center")
        self.update()

    def game(self):
        self.view.canvas.bind("<Left>", self.player.move_left)
        self.view.canvas.bind("<Right>", self.player.move_right)
        self.view.canvas.bind("<space>", self.player.shoot)
        self.view.canvas.focus_set()
        self.view.canvas.pack()
    






