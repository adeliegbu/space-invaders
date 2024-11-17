"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
from tkinter import Button as tkB
from PIL import Image, ImageTk

# Boutons du menu
class Button:
    def __init__(self, canvas, text, command, x, y):
        self.button = tkB(canvas, text=text, command=command, height=2, width=20, font=("Helvetica", 12, "bold"), bg="yellow", fg="darkblue")
        self.canvas = canvas
        self.x = x
        self.y = y

    def hide(self):
        self.canvas.delete(self.canvas.create_window(self.x, self.y, anchor="center", window=self.button))

    def show(self):
        self.canvas.create_window(self.x, self.y, anchor="center", window=self.button)


def game():
    from mvc_view import canvas, x0, y0
    vaisseau_image = ImageTk.PhotoImage(Image.open("invaders.webp").resize((500, 200), Image.LANCZOS))
    canvas.create_image(x0, y0 // 5, image=vaisseau_image, anchor="n")