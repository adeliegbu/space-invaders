import tkinter as tk
from PIL import Image, ImageTk
from mvc_model import Ship
from mvc_view import View

class Controller:
    def __init__(self):
        self.view = View(self)
        self.score = 0
        self.moving_left = False
        self.moving_right = False
        self.player = Ship(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, type="player", image=self.view.player_image)
        self.aliens = []
        self.projectiles = []

    def main(self):
        self.player = Ship(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, type="player", image=self.view.player_image)
        self.aliens = []
        self.projectiles = []
        self.view.canvas.bind("<KeyPress-Left>", self.start_move_left)
        self.view.canvas.bind("<KeyRelease-Left>", self.stop_move_left)
        self.view.canvas.bind("<KeyPress-Right>", self.start_move_right)
        self.view.canvas.bind("<KeyRelease-Right>", self.stop_move_right)
        self.view.canvas.bind("<space>", self.shoot)
        self.view.canvas.focus_set()
        self.update(True)

    def start_move_left(self, event):
        self.moving_left = True

    def stop_move_left(self, event):
        self.moving_left = False

    def start_move_right(self, event):
        self.moving_right = True

    def stop_move_right(self, event):
        self.moving_right = False

    def shoot(self, event):
        self.player.shoot()

    def update(self,loop):
        if loop:
            if self.moving_left:
                self.player.move_left()
            if self.moving_right:
                self.player.move_right()
            self.view.canvas.after(16, self.update(True))  # Appeler cette méthode à nouveau après 16 ms (environ 60 fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()

if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()