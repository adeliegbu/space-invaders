"""
objectif : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""

class Score:
    def __init__(self,score=0):
        self.score=score

    def __str__(self):
        return self.score 
        
