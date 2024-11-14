import tkinter as tk
from PIL import Image, ImageTk

# Initialisation de la fenêtre principale
fenetre = tk.Tk()
fenetre.attributes("-fullscreen", True)

# Fonction pour quitter l'application
def quitter():
    fenetre.destroy()

# Fonction pour mettre à jour le score
def update_score(event):
    global score
    score += 1
    score_label.config(text=f"Score: {score}")

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
score_label = tk.Label(canvas, text="Score: 0", font=("Helvetica", 16), bg="darkblue", fg="white")
canvas.create_window(10, 10, anchor="nw", window=score_label)  # Aligné en haut à gauche



# Boutons du menu
button_font = ("Helvetica", 12, "bold")

bouton_new_game = tk.Button(canvas, text="Nouvelle Partie", command=main.new_game, height=2, width=20, font=button_font, bg="yellow", fg="darkblue")
canvas.create_window(screen_width // 2, screen_height // 2, anchor="center", window=bouton_new_game)  # Aligné en haut à droite

bouton_show_rules = tk.Button(canvas, text="Règles", command=main.show_rules, height=2, width=20, font=button_font, bg="yellow", fg="darkblue")
canvas.create_window(screen_width // 2, screen_height // 2 + 100, anchor="center", window=bouton_show_rules)  # Aligné en haut à droite

bouton_quitter = tk.Button(canvas, text="Quitter", command=quitter, height=2, width=20, font=button_font, bg="yellow", fg="darkblue")
canvas.create_window(screen_width // 2, screen_height // 2 + 200, anchor="center", window=bouton_quitter)  # Aligné en haut à droite

# Chargement, redimensionnement, rotation et ajout de l'image supplémentaire
invaders_image = Image.open("invaders.webp").resize((100, 100), Image.LANCZOS).rotate(180)  # Redimensionner l'image à 100x100 pixels
invaders_photo = ImageTk.PhotoImage(invaders_image)
canvas.create_image(screen_width // 2, screen_height // 2, image=invaders_photo, anchor="center")

logo_image = Image.open("space_logo.png")
logo_image = logo_image.resize((500, 200), Image.LANCZOS)  # Redimensionner l'image
logo_photo = ImageTk.PhotoImage(logo_image)
canvas.create_image(screen_width // 2, screen_height // 10, image=logo_photo, anchor="n")

# Initialisation du score
score = 0

# Liaison de la touche "Espace" à la fonction update_score
fenetre.bind("<space>", update_score)

# Lancement de la boucle principale
fenetre.mainloop()