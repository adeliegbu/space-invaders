from model.alien import Alien
from model.player import Player
from model.projectile import Projectile

class Game:
    def __init__(self, canvas_width, canvas_height):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        
        # Initialiser le joueur et les aliens
        self.player = Player(x=canvas_width // 2, y=canvas_height - 50)
        self.aliens = [Alien(x=50 + i * 60, y=50 + j * 60) for i in range(5) for j in range(3)]
        self.projectiles = []

    def move_aliens(self):
        """Déplacer tous les aliens."""
        for alien in self.aliens:
            alien.move(self.canvas_width)

    def move_projectiles(self):
        """Déplacer les projectiles."""
        for projectile in self.projectiles:
            projectile.move()

    def shoot(self):
        """Faire tirer le joueur."""
        projectile = self.player.shoot()
        self.projectiles.append(projectile)

    def update_game(self):
        """Met à jour tous les éléments du jeu (mouvement des aliens et projectiles)."""
        self.move_aliens()
        self.move_projectiles()
