import sys
import pygame
from Background import Background
from Button import Button, print_text
from Menus.LevelsMenu import LevelsMenu
from Menus.SettingMenu import SettingsMenu
from enums import Color


class MainMenu:
    def __init__(self, screen: pygame.Surface):
        self.size = screen.get_size()
        self.background = Background('src/backgrounds/math_mech_menu.jpg',
                                     [0, 0])
        self.start_button = Button(130, 70, screen, Color.GREEN.value)
        self.settings_button = Button(200, 70, screen, Color.BLUE.value)
        self.quit_button = Button(100, 70, screen, Color.RED.value)
        self.widgets = {'start': [False, LevelsMenu(screen, self)],
                        'settings': [False, SettingsMenu(screen, self)],
                        'quit': [False, quit]}

    def show(self, screen: pygame.Surface):
        # pygame.mixer.music.load('src/music/start_music_cadillac.mp3')
        # pygame.mixer.music.play()
        while True:
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            print_text('Zuma',
                       self.size[0] / 2 - 60 * 5 / 2,
                       self.size[1] / 50, 150,
                       screen)
            print_text('MathMech Edition',
                       self.size[0] / 2 - 105 * 5 / 2,
                       self.size[1] / 5, 75,
                       screen, (255, 255, 255))

            self.widgets['start'][0] = self.start_button.draw_button(
                self.size[0] / 2 - 110 / 2,
                self.size[1] / 3,
                "Start", 50, [10, 10])
            self.widgets['settings'][0] = self.settings_button.draw_button(
                self.size[0] / 2 - 180 / 2,
                self.size[1] / 3 + 100,
                "Settings", 50, [10, 10])
            self.widgets['quit'][0] = self.quit_button.draw_button(
                self.size[0] / 2 - 75 / 2,
                self.size[1] / 3 + 200,
                "Quit", 50, [10, 10])

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()

            for button in self.widgets.keys():
                if self.widgets[button][0]:
                    return self.widgets[button][1]
