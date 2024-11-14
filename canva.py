import tkinter as tk
import main
from PIL import Image, ImageTk

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.attributes("-fullscreen", True)

# Fonction pour quitter l'application
def quitter():
    fenetre.destroy()

# Chargement et redimensionnement de l'image de fond
screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()
background_image = Image.open("background_invader.jpg")
background_image = background_image.resize((screen_width, screen_height), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Création du canvas pour afficher l'image de fond
canvas = tk.Canvas(fenetre, width=screen_width, height=screen_height, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Label pour le score
score_label = tk.Label(canvas, text=, font=("Helvetica", 16), bg="darkblue", fg="white")
canvas.create_window(10, 10, anchor="nw", window=score_label)  # Aligné en haut à gauche

logo_image = Image.open("space_logo.png")
logo_image = logo_image.resize((500, 200), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
canvas.create_image(screen_width // 2, screen_height // 10, image=logo_photo, anchor="n")

# Boutons du menu
button_font = ("Helvetica", 12, "bold")

bouton_new_game = tk.Button(canvas, text="Nouvelle Partie", command=main.new_game, height=2, width=20, font=button_font, bg="yellow", fg="darkblue")
canvas.create_window(screen_width // 2, screen_height // 2, anchor="center", window=bouton_new_game)  # Aligné en haut à droite

bouton_show_rules = tk.Button(canvas, text="Règles", command=main.show_rules, height=2, width=20, font=button_font, bg="yellow", fg="darkblue")
canvas.create_window(screen_width // 2, screen_height // 2 + 100, anchor="center", window=bouton_show_rules)  # Aligné en haut à droite

bouton_quitter = tk.Button(canvas, text="Quitter", command=quitter, height=2, width=20, font=button_font, bg="yellow", fg="darkblue")
canvas.create_window(screen_width // 2, screen_height // 2 + 200, anchor="center", window=bouton_quitter)  # Aligné en haut à droite




# Initialisation du score
score = 0

# Lancement de la boucle principale
fenetre.mainloop()