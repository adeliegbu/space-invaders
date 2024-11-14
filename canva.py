import tkinter as tk

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

# Chargement de l'image de fond
background_image = Image.open("background_invader.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Création du canvas pour afficher l'image de fond
canvas = tk.Canvas(fenetre, width=fenetre.winfo_screenwidth(), height=fenetre.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="center")

# Cadre pour le bouton Quitter et le score
top_frame = tk.Frame(canvas)
top_frame.pack(side="top", fill="x")

# Bouton Quitter
bouton_quitter = tk.Button(top_frame, text="Quitter", command=quitter)
bouton_quitter.pack(side="right", padx=10, pady=10)  # Aligné en haut à droite

# Label pour le score
score_label = tk.Label(top_frame, text="Score: 0", font=("Helvetica", 16))
score_label.pack(side="left", padx=10, pady=10)  # Aligné en haut à gauche

# Initialisation du score
score = 0

# Liaison de la touche "Espace" à la fonction update_score
fenetre.bind("<space>", update_score)

fenetre.mainloop()