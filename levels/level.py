import random
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
        self.critical_points = [(1100,Rotation.DOWN.value), (700, Rotation.LEFT.value),
                                (135, Rotation.UP.value)]
        self.balls_textures = ['src/textures/GlebBall.png',
                       'src/textures/IlyaBall.png',
                       'src/textures/KolyaBall.png',
                       'src/textures/KostyaBall.png',
                       'src/textures/StepaBall.png',
                       'src/textures/VovaBall.png']
        self.balls = [Ball(screen, random.choice(self.balls_textures), i, trajectory=self.critical_points)
                    for i in range(-600, 1, 60)]
        self.kill_balls = pygame.sprite.Group()

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
            screen.blit(self.hole, (122, 350))
            for ball in self.balls:
                ball.blit()
                self.__check_critical_points(ball)
                ball.move()
                if ball.rect.y <= 365 and not ball.trajectory:
                    ball.remove()
                    self.balls.remove(ball)
            self.frog.rotate()
            self.frog.blit()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if i.type == pygame.MOUSEBUTTONUP:
                    kill_ball = Ball(screen,
                                     random.choice(self.balls_textures),
                                     520, 340)
                    # kill_ball.find_path()
                    self.kill_balls.add(kill_ball)
            self.kill_balls.update()
            self.kill_balls.draw(screen)
            pygame.display.update()

    def __check_critical_points(self, ball):
        if not ball.trajectory:
            return
        if ball.rotation == Rotation.LEFT.value or \
                ball.rotation == Rotation.RIGHT.value:
            if ball.rect.x == ball.trajectory[0][0]:
                # print("Rotatin - LEFT/RIGHT")
                # print(f'x: {ball.rect.x}, y: {ball.rect.y}')
                ball.rotation = ball.trajectory[0][1]
                ball.trajectory.pop(0)            
        else:
            if ball.rect.y == ball.trajectory[0][0]:
                # print("Rotation - UP/DOWN")
                # print(f'x: {ball.rect.x}, y: {ball.rect.y}')
                ball.rotation = ball.trajectory[0][1]
                ball.trajectory.pop(0)
                # print(self.ball.rect)
        # print(self.hole.get_rect())
        # if ball.rect.y <= 350 and ball.rect.x >= 122:
        #     print('WIN')
        #     ball.remove()
        # if ball.rect.x == self.critical_points[0][0]:
        #     ball.rotation = self.critical_points[0][2]