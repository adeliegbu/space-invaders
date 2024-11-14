import tkinter as tk
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
INVADER_WIDTH = 40
INVADER_HEIGHT = 30
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
PLAYER_SPEED = 20
INVADER_SPEED = 5
BULLET_SPEED = 10

class SpaceInvadersGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Space Invaders")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()
        
        self.player = self.canvas.create_rectangle(WINDOW_WIDTH//2 - PLAYER_WIDTH//2, WINDOW_HEIGHT - PLAYER_HEIGHT - 10,
                                                   WINDOW_WIDTH//2 + PLAYER_WIDTH//2, WINDOW_HEIGHT - 10, fill="blue")
        
        self.invaders = []
        self.bullets = []
        self.create_invaders()
        
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.shoot)
        
        self.update_game()
    
    def create_invaders(self):
        for i in range(5):
            for j in range(10):
                x = j * (INVADER_WIDTH + 10) + 50
                y = i * (INVADER_HEIGHT + 10) + 50
                invader = self.canvas.create_rectangle(x, y, x + INVADER_WIDTH, y + INVADER_HEIGHT, fill="red")
                self.invaders.append(invader)
    
    def move_left(self, event):
        self.canvas.move(self.player, -PLAYER_SPEED, 0)
    
    def move_right(self, event):
        self.canvas.move(self.player, PLAYER_SPEED, 0)
    
    def shoot(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_rectangle((x1 + x2)//2 - BULLET_WIDTH//2, y1 - BULLET_HEIGHT,
                                              (x1 + x2)//2 + BULLET_WIDTH//2, y1, fill="yellow")
        self.bullets.append(bullet)
    
    def update_game(self):
        self.move_invaders()
        self.move_bullets()
        self.check_collisions()
        self.root.after(50, self.update_game)
    
    def move_invaders(self):
        global INVADER_SPEED
        for invader in self.invaders:
            self.canvas.move(invader, INVADER_SPEED, 0)
            x1, y1, x2, y2 = self.canvas.coords(invader)
            if x2 >= WINDOW_WIDTH or x1 <= 0:
                INVADER_SPEED = -INVADER_SPEED
                for inv in self.invaders:
                    self.canvas.move(inv, 0, INVADER_HEIGHT)
                break
    
    def move_bullets(self):
        for bullet in self.bullets:
            self.canvas.move(bullet, 0, -BULLET_SPEED)
            x1, y1, x2, y2 = self.canvas.coords(bullet)
            if y2 <= 0:
                self.canvas.delete(bullet)
                self.bullets.remove(bullet)
    
    def check_collisions(self):
        for bullet in self.bullets:
            x1, y1, x2, y2 = self.canvas.coords(bullet)
            for invader in self.invaders:
                ix1, iy1, ix2, iy2 = self.canvas.coords(invader)
                if x1 < ix2 and x2 > ix1 and y1 < iy2 and y2 > iy1:
                    self.canvas.delete(bullet)
                    self.canvas.delete(invader)
                    self.bullets.remove(bullet)
                    self.invaders.remove(invader)
                    break

if __name__ == "__main__":
    root = tk.Tk()
    game = SpaceInvadersGame(root)
    root.mainloop()