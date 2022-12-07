import math

import pygame
from enums import Rotation


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, texture_path, dx=200, dy=100, trajectory=None):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(texture_path)
        x, y, w, h = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (w // 5, h // 5))
        self.rect = self.image.get_rect(center=(200, 100))
        self.rect.x = dx
        self.rect.y = dy
        self.rect.width = w // 5
        self.rect.height = h // 5
        self.original_image = self.image
        self.moving_speed = 1
        self.angle = 0
        self.screen.blit(self.image, self.rect)
        self.rotation = Rotation.RIGHT.value
        if trajectory is not None:
            self.trajectory = trajectory.copy()
        else:
            self.trajectory = []
        self.shooting_speed_x = 5
        self.shooting_speed_y = 5
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.radius = 30

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        # self.__rotate()
        if self.rotation == Rotation.RIGHT.value:
            self.rect.x += self.moving_speed
        elif self.rotation == Rotation.LEFT.value:
            self.rect.x -= self.moving_speed
        elif self.rotation == Rotation.UP.value:
            self.rect.y -= self.moving_speed
        elif self.rotation == Rotation.DOWN.value:
            self.rect.y += self.moving_speed

    def reverse_move(self):
        if self.rotation == Rotation.RIGHT.value:
            self.rect.x -= self.moving_speed * 5
        elif self.rotation == Rotation.LEFT.value:
            self.rect.x += self.moving_speed * 5
        elif self.rotation == Rotation.UP.value:
            self.rect.y += self.moving_speed * 5
        elif self.rotation == Rotation.DOWN.value:
            self.rect.y -= self.moving_speed * 5

    def move_by_insert_ball(self, delta, bound_x=1100, bound_y=700):
        if self.rotation == Rotation.LEFT.value \
                or self.rotation == Rotation.RIGHT.value:
            if self.rect.x > bound_x - self.radius:
                old_x = self.rect.x
                self.rect.x = bound_x
                self.rect.y += (self.radius - (bound_x - old_x))
            else:
                self.rect.x += delta
        else:
            if self.rect.y > bound_y - self.radius:
                old_y = self.rect.y
                self.rect.y = bound_y
                self.rect.x -= (self.radius - (bound_y - old_y))
            else:
                self.rect.y += delta

    def __rotate(self):
        self.angle += 0.5
        self.image = pygame.transform.rotate(self.original_image,
                                             -self.angle % 360 - 90)

    def update(self):
        self.__shoot()

    def __shoot(self):
        dx = self.mouse_x - 520
        dy = self.mouse_y - 340
        angle = math.atan2(dy, dx)
        self.rect.x += self.shooting_speed_x * math.cos(angle)
        self.rect.y += self.shooting_speed_y * math.sin(angle)

    def check_critical_points(self):
        if not self.trajectory:
            return
        if self.rotation == Rotation.LEFT.value or \
                self.rotation == Rotation.RIGHT.value:
            if self.rect.x == self.trajectory[0][0]:
                self.rotation = self.trajectory[0][1]
                self.trajectory.pop(0)
        else:
            if self.rect.y == self.trajectory[0][0]:
                self.rotation = self.trajectory[0][1]
                self.trajectory.pop(0)
