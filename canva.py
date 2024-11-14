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

# Bouton Quitter
bouton_quitter = tk.Button(canvas, text="Quitter", command=quitter)
canvas.create_window(screen_width - 10, 10, anchor="ne", window=bouton_quitter)  # Aligné en haut à droite

# Initialisation du score
score = 0

# Liaison de la touche "Espace" à la fonction update_score
fenetre.bind("<space>", update_score)

# Lancement de la boucle principale
fenetre.mainloop()