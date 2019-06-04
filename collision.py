import pygame
import coins
import obstacle
import player

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)

p = player.Player()
c = coins.Coins()
o = obstacle.Obstacle()

class Collisions:
    def __init__(self):
        pass
    def test(self):
        if player.is_collision_with(obstacle):
            return done = False
        if player.is_collision_with(coins):
            return 5
        while not player.is_collision_with(obstacle):
            return 1
        pass
