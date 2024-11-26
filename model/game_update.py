class Game_update():
    def __init__(self, players, aliens, projectiles, wall):
        self.players = players
        self.aliens = aliens
        self.projectiles = projectiles
        self.wall = wall
    
    def update(self):
        self.aliens.move()
        self.projectiles.move()
