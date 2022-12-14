import sys
import pygame
from Background import Background
from Button import Button, print_text
from enums import Color


class SettingsMenu:
    def __init__(self, screen: pygame.Surface, back_menu):
        self.size = screen.get_size()
        self.back_button = Button(115, 70, screen, Color.ORANGE.value)
        self.background = Background(
            'src/backgrounds/math_mech_settings.jpg', [0, 0])
        self.add_vlm_button = Button(50, 50, screen)
        self.lower_vlm_button = Button(50, 50, screen)
        self.off_music_button = Button(90, 50, screen)
        self.widget = self.levels = {'back': [False, back_menu],
                                     'add_vlm': [False, self.add_vlm],
                                     'lower_vlm': [False, self.lower_vlm],
                                     'off_music': [False, self.off_music]}
        self.volume = 500

    def add_vlm(self):
        if self.volume < 500:
            self.volume += 25

    def lower_vlm(self):
        if self.volume > 0:
            self.volume -= 25

    def off_music(self):
        self.volume = 0

    def show(self, screen: pygame.Surface):
        while True:
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            pygame.draw.rect(screen, (64, 64, 64),
                             (350, 150, 500, 50))
            pygame.draw.rect(screen, (30, 200, 60),
                             (350, 150, self.volume, 50))
            print_text('Volume', 525, 100, 50, screen)
            self.widget['lower_vlm'][0] = self.lower_vlm_button.draw_button(
                290, 150, 'M', 50, [8, 5])
            self.widget['add_vlm'][0] = self.add_vlm_button.draw_button(
                860, 150, 'P', 50, [15, 5])
            self.widget['off_music'][0] = self.off_music_button.draw_button(
                920, 150, 'OFF', 50, [10, 5])
            self.widget['back'][0] = self.back_button.draw_button(
                self.size[0] / 2 - 110 / 2,
                700,
                'Back', 50, [10, 10]
            )

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()

            for button in self.widget.keys():
                if self.widget[button][0]:
                    return self.widget[button][1]
