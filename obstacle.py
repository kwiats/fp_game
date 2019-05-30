import pygame

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)

class Obstacle:
    def __init__(self):
        self.obs1 = pygame.image.load('walls2.png').convert()
        self.obs2 = pygame.image.load('walls3.png').convert()
