
def quitter(fenetre):
    fenetre.destroy()

def new_game():
    pass

def show_rules():
    pass

import tkinter as tk

from model.alien import Alien
from model.player import Player
from model.projectile import Projectile

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Space Invaders")

        # Créer un Canvas qui occupe toute la fenêtre
        self.canvas = tk.Canvas(self.master, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Créer le joueur
        self.player = Player(x=self.canvas.winfo_width() // 2 - 25, y=self.canvas.winfo_height() - 50)

        # Créer des aliens
        self.aliens = []
        for i in range(5):
            for j in range(3):
                alien = Alien(50 + i * 60, 50 + j * 60)
                self.aliens.append(alien)

        # Liste pour stocker les projectiles
        self.projectiles = []

        # Lancer la boucle du jeu
        self.update_game()

        # Associer les touches
        self.master.bind("<Left>", lambda event: self.move_player_left())
        self.master.bind("<Right>", lambda event: self.move_player_right())
        self.master.bind("<space>", lambda event: self.shoot())

    def move_player_left(self):
        """Déplacer le joueur vers la gauche"""
        self.player.move_left()

    def move_player_right(self):
        """Déplacer le joueur vers la droite"""
        self.player.move_right()

    def shoot(self):
        """Faire tirer un projectile"""
        projectile = self.player.shoot()
        self.projectiles.append(projectile)

    def update_game(self):
        """Met à jour les positions du joueur, des aliens et des projectiles."""
        
        # Mettre à jour les aliens
        for alien in self.aliens:
            alien.move()

        # Mettre à jour les projectiles
        for projectile in self.projectiles:
            projectile.move()

        # Rafraîchir l'affichage
        self.update_display()

        # Relancer la mise à jour du jeu après 50ms
        self.master.after(50, self.update_game)

    def update_display(self):
        """Met à jour l'affichage graphique."""
        # Effacer l'ancien contenu du Canvas
        self.canvas.delete("all")

        # Afficher le joueur
        self.canvas.create_rectangle(self.player.x, self.player.y,
                                     self.player.x + self.player.width,
                                     self.player.y + self.player.height, fill="blue")

        # Afficher les aliens
        for alien in self.aliens:
            self.canvas.create_oval(alien.x, alien.y, alien.x + 30, alien.y + 30, fill="green")

        # Afficher les projectiles
        for projectile in self.projectiles:
            self.canvas.create_rectangle(projectile.x - 2, projectile.y - 10,
                                         projectile.x + 2, projectile.y, fill="red")

def main():
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

if __name__ == "__main__":
    main()

