import random
import sys
import pygame
from Background import Background
from Button import Button
from levels.level_abstract import Level
from frog import Frog
from ball import Ball
from enums import Rotation, Color


class Level2(Level):
    def __init__(self, screen: pygame.Surface, back_menu):
        super().__init__(screen, back_menu)
        self.background = Background('src/backgrounds/level_2_disco.jpg',
                                     [-130, -10])
        self.frog = Frog(screen, 'src/textures/DiscoFrog.png')
        self.hole = pygame.image.load('src/textures/hole.png')
        self.hole = pygame.transform.scale(self.hole, (90, 90))
        self.critical_points = [(1100, Rotation.DOWN.value),
                                (700, Rotation.LEFT.value),
                                (135, Rotation.UP.value)]
        self.back_button = Button(115, 70, screen, Color.ORANGE.value)
        self.widget = self.levels = {'back': [False, back_menu]}
        self.balls = [Ball(screen, random.choice(self.balls_textures), i,
                           trajectory=self.critical_points)
                      for i in range(10, 371, 60)]
        self.kill_balls = pygame.sprite.Group()
        self.mixer = pygame.mixer.music

    def show(self, screen: pygame.Surface):
        self.mixer.load('src/music/deti_ikra.mp3')
        self.mixer.play(-1)
        while True:
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            self.widget['back'][0] = self.back_button.draw_button(
                10, 10, 'Back', 50, [10, 10])
            self.frog.blit()
            self.frog.rotate()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()

            for button in self.widget.keys():
                if self.widget[button][0]:
                    self.mixer.stop()
                    return self.widget[button][1]