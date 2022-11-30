import sys
import pygame
from Background import Background
from Button import Button
from enums import Color
from levels.level import Level


class LevelsMenu:
    def __init__(self, screen: pygame.Surface, back_menu):
        self.size = screen.get_size()
        self.back_button = Button(115, 70, screen, Color.ORANGE.value)
        self.levels = {'back': [False, back_menu]}
        self.level_buttons = [Button(160, 70, screen) for _ in range(5)]
        self.background = Background('src/backgrounds/math_mech_levels.jpg', [0, 0])

        for i in range(5):
            self.levels[f'level {i+1}'] = [False, Level(screen, self)]

    def show(self, screen: pygame.Surface):
        while True:
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            for i in range(5):
                self.levels[f'level {i + 1}'][0] = \
                    self.level_buttons[i].draw_button(
                        self.size[0] / 2 - 170 / 2,
                        self.size[1] / 6 + i * 100,
                        f'Level {i+1}', 50, [10, 10])
            self.levels['back'][0] = self.back_button.draw_button(
                self.size[0] / 2 - 110 / 2,
                700,
                'Back', 50, [10, 10]
            )

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()

            for button in self.levels.keys():
                if self.levels[button][0]:
                    return self.levels[button][1]