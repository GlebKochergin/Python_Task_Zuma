import sys
import pygame
from Background import Background
from levels.level_abstract import Level
from frog import Frog


class Level3(Level):
    def __init__(self, screen: pygame.Surface, back_menu):
        super().__init__(screen, back_menu)
        self.background = Background('src/backgrounds/level_3_snow.jpg',
                                     [-130, -10])
        self.frog = Frog(screen, 'src/textures/ArseniyFrog1.png')
        self.hole = pygame.image.load('src/textures/hole.png')
        self.hole = pygame.transform.scale(self.hole, (90, 90))

    def show(self, screen: pygame.Surface):
        while True:
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            self.frog.blit()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()