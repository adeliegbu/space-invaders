"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""
import tkinter as tk
import random

class Alien:
    def __init__(self, canvas, x, y, speed=10):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = 1
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()        
        # Créer l'image de l'alien dans le canvas
        self.image = canvas.create_oval(x, y, x + 30, y + 30, fill="green")

    def move(self):
        """Déplace l'alien en fonction de la taille du canvas."""
        self.x += self.speed * self.direction
        self.canvas.coords(self.image, self.x, self.y, self.x + 30, self.y + 30)
        
        # Récupérer la largeur actuelle du canvas (en cas de redimensionnement)
        canvas_width = self.canvas.winfo_width()
        
        # Si l'alien atteint un bord du canvas, il change de direction et descend
        if self.x + 35 >= canvas_width:  # Limite droite
            self.direction = -1
            self.y += 30  # L'alien descend d'une ligne
        elif self.x <= 0:  # Limite gauche
            self.direction = 1
            self.y += 30  # L'alien descend d'une ligne