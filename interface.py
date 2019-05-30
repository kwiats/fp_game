import pygame

BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
BLUE=(0, 0, 255)

class Interface():
    def __init__(self):
        self.clock = pygame.time.Clock()

    def text_objects(self, text, font , color):
        self.textSurface = font.render(text, True , color)
        return self.textSurface, self.textSurface.get_rect()

    def game_intro(self):
        self.intro = True
        self.scoring = False

        while self.intro:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.intro = False
                    self.scoring = True
                    self.score = 0

            self.display = pygame.display.get_surface()
            self.display.fill(WHITE)
            self.duzyTekst = pygame.font.Font('freesansbold.ttf', 50)
            self.sredniTekst = pygame.font.Font('freesansbold.ttf', 25)
            self.malyTekst = pygame.font.Font('freesansbold.ttf', 15)
            self.TextSurf, self.TextRect = self.text_objects("Kliknij, aby wystartować!", self.sredniTekst, BLACK)
            self.TextSurf2, self.TextRect2 = self.text_objects("FLAPPY DRONE", self.duzyTekst , BLACK)
            self.TextSurf3, self.TextRect3 = self.text_objects("Instrukcja", self.sredniTekst, BLACK)
            self.TextSurf4, self.TextRect4 = self.text_objects("Naciskaj  SPACJE  , aby latać dronem", self.malyTekst, BLACK)
            self.TextRect.center = ((640/2), (960 / 2))
            self.TextRect2.center = ((640/2), (410))
            self.TextRect3.center = ((640/2), (600))
            self.TextRect4.center = ((640/2), (620))
            self.display.blit(self.TextSurf, self.TextRect)
            self.display.blit(self.TextSurf2, self.TextRect2)
            self.display.blit(self.TextSurf3, self.TextRect3)
            self.display.blit(self.TextSurf4, self.TextRect4)
            pygame.display.update()
            self.clock.tick(15)

    def scoreCounter(self,score_2):
            self.score += score_2

            self.malyTekst = pygame.font.Font('freesansbold.ttf', 15)
            self.TextSurf5, self.TextRect5 = self.text_objects("Wynik: "+str(self.score), self.malyTekst, WHITE)
            self.TextRect5.center = ((640 / 2), 20)
            self.display.blit(self.TextSurf5, self.TextRect5)
            pygame.display.update()




    def do(self):
        self.game_intro()