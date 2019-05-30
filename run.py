import pygame
import player
import interface
import coins

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

FPS = 60
g = player.Player()
i = interface.Interface()
c = coins.Coins()

class Game(object):
    def __init__(self):
        self.fps = 60
        self.size = (640, 960)
        self.done = True
        self.x = 0
        self.c = 0
        self.clock = pygame.time.Clock()

        pygame.init()
        self.screen = pygame.display.set_mode(self.size, 0, 32)
        pygame.display.set_caption("Flappy Drone")
        self.background = pygame.image.load('bg.jpg').convert()
        self.background = pygame.transform.scale(self.background, (3000, 960))
        self.podloga = pygame.image.load('podloga.jpg').convert()
        self.podloga = pygame.transform.scale(self.podloga, (3000, 210))
        i.game_intro()

        while self.done:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = False

            self.mapa()
            g.do()
            c.do()
            pygame.display.update()
            punkty = 0
            # pygame.time.delay(1000)
            punkty += 1
            i.scoreCounter(int(punkty))
            pygame.display.update()
            pygame.display.flip
            self.clock.tick(FPS)

    def tick(self):
        pass

    def mapa(self):
        self.screen.fill(WHITE)
        self.rel_x = self.x % self.background.get_rect().width
        self.screen.blit(self.background, (self.rel_x - self.background.get_rect().width, 0))
        if self.rel_x < 640:
            self.screen.blit(self.background, (self.rel_x, 0))
        self.x -= 1.0
        pygame.display.update()

        self.rel_c = self.x % self.podloga.get_rect().width
        self.screen.blit(self.podloga, (self.rel_c - self.podloga.get_rect().width, 750))
        if self.rel_c < 640:
            self.screen.blit(self.podloga, (self.rel_c, 0))
        self.c -= 1.0
        pygame.display.update()

if __name__ == "__main__":
    Game()