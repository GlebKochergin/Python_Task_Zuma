import sys
import pygame
from Background import Background
from Button import Button
from frog import Frog


class Level:
    def __init__(self, screen: pygame.Surface, back_menu):
        self.size = screen.get_size()
        self.pause_button = Button(120, 70, screen, pygame.Color(255, 165, 0))
        self.levels = {'back': [False, back_menu]}

    def show(self, screen: pygame.Surface):
        raise NotImplementedError()


class Level1(Level):
    def __init__(self, screen: pygame.Surface, back_menu):
        super().__init__(screen, back_menu)
        self.background = Background('src/backgrounds/level_1_background.jpg', [0, 0])
        self.frog = Frog(screen, 'src/textures/ArseniyFrog1.png')
        self.ball = pygame.image.load('src/textures/GlebBall.png')
        self.ball = pygame.transform.scale(self.ball, (60, 60))
        self.hole = pygame.image.load('src/textures/hole.png')
        self.hole = pygame.transform.scale(self.hole, (90, 90))

    def show(self, screen: pygame.Surface):
        while True:
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            positions = [
                [(55, 90, 1160, 65), (0, 100, 140, 140)],
                [(55, 90, 65, 600), (1095, 165, 140, 140)],
                [(55, 90, 960, 65), (135, 700, 140, 140)],
                [(55, 90, 65, 300), (135, 400, 140, 140)]]
            for pos in positions:
                shape_surf = pygame.Surface(pygame.Rect(pos[0]).size,
                                            pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, (255, 255, 255, 127),
                                 shape_surf.get_rect())
                screen.blit(shape_surf, pos[1])
            screen.blit(self.ball, (200, 100))
            screen.blit(self.hole, (122, 350))
            self.frog.rotate()
            self.frog.blit()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()