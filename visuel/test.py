import tkinter as tk
from PIL import Image, ImageTk

class Options:
    def __init__(self):
        # Charger les images comme tu l'as déjà fait
        self.player_image_green = ImageTk.PhotoImage(Image.open("visuel/players_green.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_green = ImageTk.PhotoImage(Image.open("visuel/projectile_green.png").rotate(90).resize((250, 250), Image.LANCZOS))

        self.player_image_blue = ImageTk.PhotoImage(Image.open("visuel/players_blue.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_blue = ImageTk.PhotoImage(Image.open("visuel/projectile_blue.png").rotate(90).resize((250, 250), Image.LANCZOS))

        self.player_image_red = ImageTk.PhotoImage(Image.open("visuel/players_red.png").resize((200, 200), Image.LANCZOS))
        self.projectile_player_image_red = ImageTk.PhotoImage(Image.open("visuel/projectile_red.png").rotate(90).resize((250, 250), Image.LANCZOS))

        # Liste des images
        self.player_images = [self.player_image_green, self.player_image_blue, self.player_image_red]
        self.projectile_images = [self.projectile_player_image_green, self.projectile_player_image_blue, self.projectile_player_image_red]
        
        # Par défaut, la couleur choisie est verte (index 0)
        self.current_player_image = self.player_image_green
        self.current_projectile_image = self.projectile_player_image_green
        self.current_index = 0  # L'index de la couleur actuelle (0 = vert)

    def set_player_color(self, index):
        """
        Change la couleur du joueur et du projectile en fonction de l'index choisi
        index : int - L'index de l'élément dans la liste des images (0: vert, 1: bleu, 2: rouge)
        """
        if index >= 0 and index < len(self.player_images):
            self.current_player_image = self.player_images[index]
            self.current_projectile_image = self.projectile_images[index]
            self.current_index = index  # Mettre à jour l'index
            print(f"Le joueur a choisi la couleur {['vert', 'bleu', 'rouge'][index]}")

    def get_player_image(self):
        """Retourne l'image actuelle du joueur"""
        return self.current_player_image

    def get_projectile_image(self):
        """Retourne l'image actuelle du projectile"""
        return self.current_projectile_image

    def next_color(self):
        """Passe à la couleur suivante"""
        new_index = (self.current_index + 1) % len(self.player_images)  # Passe à l'index suivant et boucle
        self.set_player_color(new_index)

    def prev_color(self):
        """Passe à la couleur précédente"""
        new_index = (self.current_index - 1) % len(self.player_images)  # Passe à l'index précédent et boucle
        self.set_player_color(new_index)


class GameWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.options = Options()  # Créer l'objet Options

        # Créer le canvas pour afficher l'image du joueur
        self.canvas = tk.Canvas(self, width=500, height=500)
        self.canvas.pack()

        # Afficher l'image du joueur (initialement verte)
        self.player_sprite = self.canvas.create_image(250, 250, image=self.options.get_player_image())

        # Créer les boutons de la souris pour changer la couleur
        self.button_left = tk.Button(self, text="←", command=self.prev_color)
        self.button_left.pack(side="left")

        self.button_right = tk.Button(self, text="→", command=self.next_color)
        self.button_right.pack(side="left")

        # Lier les événements clavier pour les flèches gauche/droite
        self.bind("<Left>", self.prev_color_event)
        self.bind("<Right>", self.next_color_event)

    def prev_color(self):
        """Changer la couleur à gauche (précédente)"""
        self.options.prev_color()
        self.update_player_image()

    def next_color(self):
        """Changer la couleur à droite (suivante)"""
        self.options.next_color()
        self.update_player_image()

    def prev_color_event(self, event):
        """Changer la couleur à gauche (précédente) via la flèche gauche"""
        self.prev_color()

    def next_color_event(self, event):
        """Changer la couleur à droite (suivante) via la flèche droite"""
        self.next_color()

    def update_player_image(self):
        """Met à jour l'image du joueur sur le canvas"""
        self.canvas.itemconfig(self.player_sprite, image=self.options.get_player_image())


# Lancer la fenêtre principale
if __name__ == "__main__":
    game_window = GameWindow()
    game_window.mainloop()
