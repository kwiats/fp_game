import pygame
import random

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)

class Coins():

    coin = None
    display = None
    randPosition = []
    positionx = 0
    ilosc_coins = 0
    koszk = []
    y = None
    myPosition = random.randint(10, 750)

    def __init__(self):
        self.ilosc_coins = 255
        self.x = 0
        self.koszyk = []
        self.i = 1

    def draw(self):
        self.coin = pygame.image.load('coin.png').convert()
        self.coin = pygame.transform.scale(self.coin, (50, 50))
        self.display = pygame.display.get_surface()
        self.randPosition.append(self.myPosition)
        self.positionx = self.x % self.display.get_rect().width
        self.display.blit(self.coin,(self.positionx - self.display.get_rect().width,self.randPosition[0]))
        if self.positionx < 640:
            self.display.blit(self.coin, (self.positionx, self.randPosition[0]))
        self.randPosition.clear()
        self.x -= 4.0

    def do(self):
        self.draw()