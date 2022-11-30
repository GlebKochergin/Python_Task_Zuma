import types

import pygame
from MainMenu import MainMenu

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Zuma')


def scene():
    curr_scene = MainMenu(screen)
    while True:
        result = curr_scene.show(screen)
        if result == quit:
            result()
            continue
        if isinstance(result, types.MethodType):
            result()
            continue
        if result != curr_scene:
            curr_scene = result


if __name__ == '__main__':
    scene()