from enum import Enum

import pygame


class Color(Enum):
    RED = pygame.Color(250, 128, 114)
    GREEN = pygame.Color(154, 205, 50)
    BLUE = pygame.Color(70, 130, 180)
    ORANGE = pygame.Color(255, 165, 0)


class Rotation(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
