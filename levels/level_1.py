import random
import sys
import pygame
from Background import Background
from levels.level_abstract import Level
from frog import Frog
from ball import Ball
from enums import Rotation


class Level1(Level):
    def __init__(self, screen: pygame.Surface, back_menu):
        super().__init__(screen, back_menu)
        self.background = Background('src/backgrounds/level_1_background.jpg',
                                     [0, 0])
        self.frog = Frog(screen, 'src/textures/ArseniyFrog1.png')
        self.hole = pygame.image.load('src/textures/hole.png')
        self.hole = pygame.transform.scale(self.hole, (90, 90))
        self.critical_points = [(1100, Rotation.DOWN.value),
                                (700, Rotation.LEFT.value),
                                (135, Rotation.UP.value)]
        self.balls = [Ball(screen, random.choice(self.balls_textures), i,
                           trajectory=self.critical_points)
                      for i in range(10, 371, 60)]
        self.kill_balls = pygame.sprite.Group()
        self.frog_sound = pygame.mixer.Sound('src/sounds/frog_sound.mp3')

    def show(self, screen: pygame.Surface):
        while True:
            self.clock.tick(60)
            screen.fill([255, 255, 255])
            screen.blit(self.background.image, self.background.rect)
            routes = [
                [(55, 90, 1160, 65), (0, 100, 140, 140)],
                [(55, 90, 65, 600), (1095, 165, 140, 140)],
                [(55, 90, 960, 65), (135, 700, 140, 140)],
                [(55, 90, 65, 300), (135, 400, 140, 140)]]
            for pos in routes:
                shape_surf = pygame.Surface(pygame.Rect(pos[0]).size,
                                            pygame.SRCALPHA)
                pygame.draw.rect(shape_surf, (255, 255, 255, 127),
                                 shape_surf.get_rect())
                screen.blit(shape_surf, pos[1])
            screen.blit(self.hole, (122, 350))
            for ball in self.balls:
                ball.blit()
                ball.check_critical_points()
                ball.move()
            self.frog.blit()
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if i.type == pygame.MOUSEBUTTONUP:
                    self.frog_sound.play()
                    if len(self.kill_balls) == 0:
                        kill_ball = Ball(screen,
                                         random.choice(self.balls_textures),
                                         520, 340)
                        self.kill_balls.add(kill_ball)
                    if len(self.kill_balls) > 0:
                        last_sprite = self.kill_balls.sprites()[-1]
                        if (last_sprite.rect.x < -60
                                or last_sprite.rect.x > 1260
                                or last_sprite.rect.y < -60
                                or last_sprite.rect.y > 860):
                            kill_ball = Ball(screen,
                                             random.choice(
                                                 self.balls_textures),
                                             520, 340)
                            self.kill_balls.add(kill_ball)
            if len(self.kill_balls) > 0:
                curr_ball = self.kill_balls.sprites()[-1]
                if curr_ball.rect.x <= 1100 and curr_ball.rect.y <= 155:
                    if abs(curr_ball.rect.x - self.balls[0].rect.x) <= 60 \
                            and abs(curr_ball.rect.y - self.balls[0].rect.y)\
                            <= 60:
                        x, y = self.balls[0].rect.x, self.balls[0].rect.y
                        trajectory = self.balls[0].trajectory
                        curr_ball.trajectory = trajectory.copy()
                        curr_ball.rect.x = x - 60
                        curr_ball.rect.y = y
                        # self.balls[0].move_by_insert_ball(30)
                        self.balls.insert(0, curr_ball)
                        self.kill_balls.remove(curr_ball)
                        continue
                    if abs(curr_ball.rect.x - self.balls[-1].rect.x) <= 60 \
                            and abs(
                        curr_ball.rect.y - self.balls[-1].rect.y) <= 60:
                        x, y = self.balls[-1].rect.x, self.balls[-1].rect.y
                        trajectory = self.balls[-1].trajectory
                        curr_ball.trajectory = trajectory.copy()
                        curr_ball.rect.x = x + 60
                        curr_ball.rect.y = y
                        # self.balls[0].move_by_insert_ball(30)
                        self.balls.append(curr_ball)
                        self.kill_balls.remove(curr_ball)
                        continue
                    for i in range(0, len(self.balls) - 1):
                        ball1 = self.balls[i]
                        ball2 = self.balls[i + 1]
                        if ball1.rect.x <= curr_ball.rect.x <= ball2.rect.x \
                                and ball1.rect.y <= curr_ball.rect.y <= ball2.rect.y:
                            x, y = ball2.rect.x, ball2.rect.y
                            trajectory = ball2.trajectory
                            for j in range(len(self.balls)):
                                if j <= i:
                                    self.balls[j].move_by_insert_ball(-30)
                                else:
                                    self.balls[j].move_by_insert_ball(30)
                            curr_ball.rect.x = x - 30
                            curr_ball.rect.y = y
                            curr_ball.trajectory = trajectory.copy()
                            self.balls.insert(i + 1, curr_ball)
                            self.kill_balls.remove(curr_ball)
                            break
            self.kill_balls.update()
            self.kill_balls.draw(screen)
            pygame.display.update()
