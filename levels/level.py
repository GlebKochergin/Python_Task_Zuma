import sys
import pygame
from Background import Background
from Button import Button
from frog import Frog
from ball import Ball
from enums import Rotation


class Level:
    def __init__(self, screen: pygame.Surface, back_menu):
        self.size = screen.get_size()
        self.pause_button = Button(120, 70, screen, pygame.Color(255, 165, 0))
        self.levels = {'back': [False, back_menu]}

    def show(self, screen: pygame.Surface):
        raise NotImplementedError()


class Level1(Level):
    def __init__(self, screen: pygame.Surface, back_menu):
        super().__init__(screen, back_menu)
        self.background = Background('src/backgrounds/level_1_background.jpg', [0, 0])
        self.frog = Frog(screen, 'src/textures/ArseniyFrog1.png')
        self.ball = Ball(screen, 'src/textures/GlebBall.png')
        self.hole = pygame.image.load('src/textures/hole.png')
        self.hole = pygame.transform.scale(self.hole, (90, 90))
        self.clock = pygame.time.Clock()
        self.critical_points = [(1100, 100, Rotation.DOWN.value), (1100, 690, Rotation.LEFT.value),
                                (122, 690, Rotation.UP.value)]

    def show(self, screen: pygame.Surface):
        while True:
            self.clock.tick(600)
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            positions = [
                [(55, 90, 1160, 65), (0, 100, 140, 140)],
                [(55, 90, 65, 600), (1095, 165, 140, 140)],
                [(55, 90, 960, 65), (135, 700, 140, 140)],
                [(55, 90, 65, 300), (135, 400, 140, 140)]]
            for pos in positions:
                shape_surf = pygame.Surface(pygame.Rect(pos[0]).size,
                                            pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, (255, 255, 255, 127),
                                 shape_surf.get_rect())
                screen.blit(shape_surf, pos[1])
            self.__check_critical_points()
            self.ball.move()
            self.ball.blit()
            screen.blit(self.hole, (122, 350))
            self.frog.rotate()
            self.frog.blit()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()

    def __check_critical_points(self):
        if self.ball.rotation == Rotation.LEFT.value or \
                self.ball.rotation == Rotation.RIGHT.value:
            for point in self.critical_points:
                if self.ball.rect.x == point[0]:
                    self.ball.rotation = point[2]
                    break
        else:
            for point in self.critical_points:
                if self.ball.rect.y == point[1]:
                    self.ball.rotation = point[2]
                    break
        # print(self.ball.rect)
        # print(self.hole.get_rect())
        if self.ball.rect.y <= 350 and self.ball.rect.x >= 122:
            print('WIN')
            self.ball.remove()
        # if self.ball.rect.x == self.critical_points[0][0]:
        #     self.ball.rotation = self.critical_points[0][2]