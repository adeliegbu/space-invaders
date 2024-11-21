"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
import tkinter as tk
from PIL import Image, ImageTk


class Controller:
    def __init__(self):
        self.width = 
        self.score = 0
        self.life = 3

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


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_image, anchor="nw")
    root.mainloop()