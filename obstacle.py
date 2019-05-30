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

    def draw(self):
        self.display = pygame.display.get_surface()
        self.display.blit(self.obs1,0,0)
        self.display.blit(self.obs2,0,0)

    def do(self):
        self.draw()
