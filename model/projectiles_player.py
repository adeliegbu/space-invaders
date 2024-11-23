from model.projectile import Projectile

class Projectile_player(Projectile):
    def __init__(self, canvas, x, y, image):
        super().__init__(canvas, x, y, type=1, image=image)
        self.projectiles_player = []
        self.type = 1

    def shot(self):
        self.projectiles_player.append(Projectile(self.canvas, self.x, self.y, self.image))
    
    def move(self):
        for projectile in self.projectiles_player:
            projectile.move()
            if projectile.y < 0 or projectile.y > self.canvas.winfo_height():
                self.projectiles_player.remove(projectile)
                projectile.out_of_screen()
