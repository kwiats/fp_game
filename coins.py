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

    positionx = 0
    ilosc_coins = 0
    koszk = []
    y = None
    i = 0

    def __init__(self):
        self.ilosc_coins = 255
        self.x = 0
        self.koszyk = []
        self.distance = 640
        self.clock = pygame.time.Clock()

    def yRandCord(self):
        self.randPosition = []
        for yCord in range(1, 3):
            self.randPosition.append(random.randint(10, 750))
            print(self.randPosition)


    def draw(self):
        self.coin = pygame.image.load('coin.png').convert()
        self.coin = pygame.transform.scale(self.coin, (50, 50))
        self.display = pygame.display.get_surface()
        self.positionx = self.x % self.display.get_rect().width
        self.yRandCord()
        self.positiony = random.choice(self.randPosition)
        #self.sleep(7)
        self.display.blit(self.coin,((self.positionx - self.display.get_rect().width),self.positiony))
        print(self.positiony)
        if self.positionx < 640:
            self.positiony = random.choice(self.randPosition)
            #self.sleep(7)
            self.display.blit(self.coin, (self.positionx, self.positiony))
            self.randPosition.clear()
        self.x -= 4.0

    def do(self):
        self.draw()