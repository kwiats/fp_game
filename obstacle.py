import pygame
import random

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)

class Obstacle:
    def __init__(self):
        self.x = 0

        for yCord in range(1,15):
            self.yCords = random.randrange(50,350,50)

    def draw(self):
        self.obs1 = pygame.image.load('walls2.png').convert_alpha()
        self.obs1 = pygame.transform.scale(self.obs1, (500, 200))
        self.obs2 = pygame.image.load('walls3.png').convert_alpha()
        self.obs2 = pygame.transform.scale(self.obs2, (500, 200))
        self.display = pygame.display.get_surface()
        self.positionx = self.x % self.display.get_rect().width
        self.display.blit(self.obs1, ((self.positionx - self.display.get_rect().width), 600))
        self.display.blit(self.obs2, ((self.positionx - self.display.get_rect().width), 0))
        if self.positionx < 640:
            self.display.blit(self.obs1, (self.positionx,600))
            self.display.blit(self.obs2, (self.positionx,0))
        self.x -= 4.0


    def do(self):
        self.draw()
