from abc import ABC, abstractmethod
import pygame
from Background import Background
from Button import Button


class Level(ABC):
    def __init__(self, screen: pygame.Surface, back_menu):
        self.size = screen.get_size()
        self.pause_button = Button(120, 70, screen, pygame.Color(255, 165, 0))
        self.levels = {'back': [False, back_menu]}
        self.background = Background('src/backgrounds/math_mech_levels.jpg', [0, 0])

        for i in range(5):
            self.levels[f'level {i+1}'] = [False, lambda: print(f'{i+1} level was selected')]

    @abstractmethod
    def show(self, screen: pygame.Surface):
        pass