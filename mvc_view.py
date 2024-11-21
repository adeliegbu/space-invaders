"""
objectif : Mettre en place l'interface visuel de Space Invaders.
date :  15 nov 2024
par : Loann CORDEL, Adélie GIBOU
"""

import tkinter as tk
from PIL import Image, ImageTk
from mvc_controller import Button

from visuel.regles import rules_text


# Création de la fenêtre
fenetre = tk.Tk()
fenetre.attributes("-fullscreen", True)

#variables concernant les dimensions de l'écran
screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()
x0, y0 = screen_width // 2, screen_height // 2

#Image de fond
bg_image = Image.open("tp-space-invaders-cordel-gibou/visuel/background_invader.jpg")
bg_image = ImageTk.PhotoImage(bg_image.resize((screen_width, screen_height), Image.LANCZOS))

#création du canvas
canvas = tk.Canvas(fenetre, width=screen_width, height=screen_height, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")


'''
# Label pour le score
score_label = tk.Label(canvas, text=str(Score), font=("Helvetica", 16), bg="darkblue", fg="white")
canvas.create_window(10, 10, anchor="nw", window=score_label)  # Aligné en haut à gauche
'''

#image du logo
logo_image = ImageTk.PhotoImage(Image.open("tp-space-invaders-cordel-gibou/visuel/space_logo.png").resize((500, 200), Image.LANCZOS))

#fenêtre des règles
rules_window = tk.Label(canvas, text=str(rules_text),font=("Helvetica", 14), justify=tk.LEFT, bg="yellow", fg="darkblue", padx="30")


#Fonctions d'update de l'affichage
def new_game():
    button_new_game.hide()
    button_rules.hide()
    button_leave.hide()
    canvas.delete(canvas.create_image(x0, y0 // 5, image=logo_image, anchor="n"))
    game()

def rules():
    button_new_game.hide()
    button_rules.hide()
    button_leave.hide()
    button_menu.show()
    canvas.create_window(x0, y0 + 50, anchor="center", window=rules_window)

def menu():
    button_new_game.show()
    button_rules.show()
    button_leave.show()
    button_menu.hide()
    canvas.delete(canvas.create_window(x0, y0 + 50, anchor="center", window=rules_window))
    canvas.create_image(x0, y0 // 5, image=logo_image, anchor="n")

def leave():
    fenetre.destroy()

button_new_game = Button(canvas, "Nouvelle Partie", new_game, x0, y0)
button_rules = Button(canvas, "Règles", rules, x0, y0 + 100)
button_leave = Button(canvas, "Quitter", leave, x0, y0 + 200)
button_menu = Button(canvas, "Menu", menu, x0, y0 + 280)


# Lancement de la boucle principale
menu()
fenetre.mainloop()