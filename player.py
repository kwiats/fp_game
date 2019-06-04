import pygame
from pygame.math import Vector2

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self ):
        self.speed = 0.7
        self.gravity = 1.9
        self.vel = Vector2(0, 0)
        self.position = Vector2(15, 300)
        self. acc = Vector2(0, 0)
        self.clock = pygame.time.Clock()

        super(Player, self).__init__()

        self.images = []
        self.images.append(pygame.image.load('sprite/drone (1).png'))
        self.images.append(pygame.image.load('sprite/drone (2).png'))
        self.images.append(pygame.image.load('sprite/drone (3).png'))
        self.images.append(pygame.image.load('sprite/drone (4).png'))
        self.images.append(pygame.image.load('sprite/drone (5).png'))
        self.images.append(pygame.image.load('sprite/drone (6).png'))
        self.images.append(pygame.image.load('sprite/drone (7).png'))
        self.images.append(pygame.image.load('sprite/drone (8).png'))
        self.images.append(pygame.image.load('sprite/drone (9).png'))
        self.images.append(pygame.image.load('sprite/drone (10).png'))
        self.images.append(pygame.image.load('sprite/drone (11).png'))
        self.images.append(pygame.image.load('sprite/drone (12).png'))
        self.images.append(pygame.image.load('sprite/drone (13).png'))
        self.images.append(pygame.image.load('sprite/drone (14).png'))
        self.images.append(pygame.image.load('sprite/drone (15).png'))
        self.images.append(pygame.image.load('sprite/drone (16).png'))
        self.images.append(pygame.image.load('sprite/drone (17).png'))
        self.images.append(pygame.image.load('sprite/drone (18).png'))
        self.images.append(pygame.image.load('sprite/drone (19).png'))
        self.images.append(pygame.image.load('sprite/drone (20).png'))
        self.images.append(pygame.image.load('sprite/drone (21).png'))
        self.images.append(pygame.image.load('sprite/drone (22).png'))
        self.images.append(pygame.image.load('sprite/drone (23).png'))
        self.images.append(pygame.image.load('sprite/drone (24).png'))



        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(5, 5, 150, 198)


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
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]
        display = pygame.display.get_surface()
        display.blit(self.image, (self.position.x, self.position.y))
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
