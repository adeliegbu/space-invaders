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
        self.player = Ship(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, type="player", image=self.view.player_image, projectile_image=self.view.projectile_image)
        self.aliens = []
        self.projectiles = []
        self.shoot_cooldown = True, 300

    def main(self):
        self.player = Ship(self.view.canvas, self.view.x0, 17 * self.view.y0 // 10, type="player", image=self.view.player_image, projectile_image=self.view.projectile_image)
        self.aliens = []
        self.projectiles = []
        self.view.canvas.bind("<KeyPress-Left>", self.start_move_left)
        self.view.canvas.bind("<KeyRelease-Left>", self.stop_move_left)
        self.view.canvas.bind("<KeyPress-Right>", self.start_move_right)
        self.view.canvas.bind("<KeyRelease-Right>", self.stop_move_right)
        self.view.canvas.bind("<space>", self.shoot)
        self.view.canvas.focus_set()
        self.update()

    def start_move_left(self, event):
        self.moving_left = True

    def stop_move_left(self, event):
        self.moving_left = False

    def start_move_right(self, event):
        self.moving_right = True

    def stop_move_right(self, event):
        self.moving_right = False

    def shoot(self, event):
        if self.shoot_cooldown[0]:
            self.projectiles.append(self.player.shoot())
            self.shoot_cooldown = False, 300
            self.view.canvas.after(self.shoot_cooldown[1])
            self.shoot_cooldown = True, 300

    def update(self):
        for alien in self.aliens:
            alien.move()
        for projectile in self.projectiles:
            projectile.move()
        if self.moving_left:
            self.player.move_left()
        if self.moving_right:
            self.player.move_right()
        self.view.canvas.after(16, self.update)  # Appeler cette méthode à nouveau après 16 ms (environ 60 fois par seconde)

    def run(self):
        self.view.menu()
        self.view.fenetre.mainloop()

if __name__ == "__main__":
    space_invaders = Controller()
    space_invaders.run()