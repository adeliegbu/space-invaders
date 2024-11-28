"""
objectifs : réaliser le jeu Space Invaders.
date :  14 nov 2024
par : Loann CORDEL, Adélie GIBOU
codé en python
programme 
"""

from model.projectile_related.projectile import Projectile
from model.parents_class.ship import Ship
from model.player_related.player_ship import Player_ship
from model.alien_related.alien_ship import Alien_ship
from model.cooldown import Cooldown
from model.alien_related.aliens import Aliens
from model.player_related.players import Players
from model.projectile_related.projectiles import Projectiles
from model.projectile_related.players_projectiles import Players_projectiles
from model.projectile_related.aliens_projectiles import Aliens_projectiles
from model.wall_related.walls import Walls
from model.game_logic import Game_logic
from model.binds import Binds
from model.options import Options