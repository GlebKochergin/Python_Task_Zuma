import sys
import pygame
from Background import Background
from Button import Button
from enums import Color
from levels.level_1 import Level1
from levels.level_2 import Level2
from levels.level_3 import Level3


class LevelsMenu:
    def __init__(self, screen: pygame.Surface, back_menu):
        self.size = screen.get_size()
        self.back_button = Button(115, 70, screen, Color.ORANGE.value)
        self.levels = {'back': [False, back_menu]}
        self.level_buttons = [Button(290, 70, screen),
                              Button(290, 70, screen, (204, 153, 255), (153, 51, 255)),
                              Button(320, 70, screen, (0, 102, 102), (0, 102, 0))]
        self.background = Background('src/backgrounds/math_mech_levels.jpg',
                                     [0, 0])
        self.levels['Default Level'] = [False, Level1(screen, self)]
        self.levels['Disco Level'] = [False, Level2(screen, self)]
        self.levels['New Year Level'] = [False, Level3(screen, self)]

    def show(self, screen: pygame.Surface):
        # pygame.mixer.music.load('src/music/morgen_levels.mp3')
        # pygame.mixer.music.play(-1)
        while True:
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            self.levels['Default Level'][0] = \
                self.level_buttons[0].draw_button(
                    self.size[0] / 2 - 280 / 2,
                    self.size[1] / 6,
                    'Default Level', 50, [10, 10])
            self.levels['Disco Level'][0] = \
                self.level_buttons[1].draw_button(
                    self.size[0] / 2 - 280 / 2,
                    self.size[1] / 6 + 100,
                    'Disco Level', 50, [35, 10])
            self.levels['New Year Level'][0] = \
                self.level_buttons[2].draw_button(
                    self.size[0] / 2 - 155,
                    self.size[1] / 6 + 200,
                    'New Year Level', 50, [9, 10])

            self.levels['back'][0] = self.back_button.draw_button(
                self.size[0] / 2 - 110 / 2,
                700,
                'Back', 50, [10, 10])

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()

            for button in self.levels.keys():
                if self.levels[button][0]:
                    return self.levels[button][1]