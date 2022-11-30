import sys
import pygame
from Background import Background
from Button import Button


class Level:
    def __init__(self, screen: pygame.Surface, back_menu):
        self.size = screen.get_size()
        self.pause_button = Button(120, 70, screen, pygame.Color(255, 165, 0))
        self.levels = {'back': [False, back_menu]}
        self.background = Background('src/backgrounds/math_mech_levels.jpg', [0, 0])

    def show(self, screen: pygame.Surface):
        while True:
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()