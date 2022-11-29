import pygame
from Background import Background
from MainMenu import MainMenu

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)
a = screen.get_size()
background = Background('src/math_mech_menu.jpg', [0, 0])
pygame.display.set_caption('Zuma')


def scene():
    curr_scene = MainMenu(screen)
    while True:
        result = curr_scene.show(screen, background)
        if result != curr_scene:
            curr_scene = result


if __name__ == '__main__':
    scene()