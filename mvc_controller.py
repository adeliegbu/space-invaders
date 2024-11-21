"""
objectif : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
import tkinter as tk
from PIL import Image, ImageTk

from mvc_model import Ship, Projectile
from mvc_view import View


class Controller:
    def __init__(self):
        self.view = View()
        self.score = 0

    def game(self):
        self.player = Ship(self.view.canvas, self.view.x0, 9 * self.view.y0 // 10, type="player",id=self.view.player_image)
        self.aliens = []
        self.projectiles = []
        self.view.canvas.bind("<Left>", self.player.move_left)
        self.view.canvas.bind("<Right>", self.player.move_right)
        self.view.canvas.bind("<space>", self.player.shoot)
        self.view.canvas.focus_set()
        self.view.canvas.pack()
    
    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()

if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()






