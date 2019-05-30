import pygame
from pygame.math import Vector2

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)

class Player():
    def __init__(self ):
        self.speed = 0.7
        self.gravity = 1.9
        self.vel = Vector2(0, 0)
        self.position = Vector2(15, 300)
        self. acc = Vector2(0, 0)
        self.clock = pygame.time.Clock()

    def keys(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            self.acc = Vector2(0, -self.speed * 5)



    def move(self):
        self.vel *= 0.8
        self.vel -= Vector2(0, -self.gravity)
        self.vel += self.acc
        self.position += self.vel
        self.acc *= 0

    def draw(self):
        self.drone = pygame.image.load('drone.gif').convert()
        display = pygame.display.get_surface()
        display.blit(self.drone, (self.position.x, self.position.y))
        pygame.display.update()

    def text_objects(self, text, font , color):
        self.textSurface = font.render(text, True, color)
        return self.textSurface, self.textSurface.get_rect()

    def gameover(self):
        if self.position.y > 650:
            self.duzyTekst = pygame.font.Font('freesansbold.ttf', 50)
            textSurf, textRect = self.text_objects("GAME OVER",self.duzyTekst,  WHITE)
            textRect.center = ((640 / 2), (960 / 2))
            display = pygame.display.get_surface()
            display.blit(textSurf,textRect)
            print('Game over - gra skonczona')
            pygame.display.update()

    def nosignal(self):
        if self.position.y < -150:
            self.duzyTekst = pygame.font.Font('freesansbold.ttf', 50)
            textSurf, textRect = self.text_objects("NO SIGNAL",self.duzyTekst,  WHITE)
            textRect.center = ((640 / 2), (960 / 2))
            display = pygame.display.get_surface()
            display.blit(textSurf,textRect)
            print("No signal - brak sygnału")
            pygame.display.update()

    def do(self):
        self.clock.tick(30)
        self.keys()
        self.move()
        self.draw()
        self.gameover()
        self.nosignal()
