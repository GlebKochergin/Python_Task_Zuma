import pygame
from Button import Button


class Level:
    def __init__(self, screen: pygame.Surface, back_menu):
        self.size = screen.get_size()
        self.pause_button = Button(120, 70, screen, pygame.Color(255, 165, 0))
        self.levels = {'back': [False, back_menu]}
        self.clock = pygame.time.Clock()
        self.balls_textures = ['src/textures/GlebBall.png',
                               'src/textures/IlyaBall.png',
                               'src/textures/KolyaBall.png',
                               'src/textures/KostyaBall.png',
                               'src/textures/StepaBall.png',
                               'src/textures/VovaBall.png']

    def show(self, screen: pygame.Surface):
        raise NotImplementedError()
