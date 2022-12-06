import math

import pygame
from pygame.math import Vector2
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
        self.speed = 1
        self.angle = 0
        self.screen.blit(self.image, self.rect)
        self.rotation = Rotation.RIGHT.value
        if trajectory is not None:
            self.trajectory = trajectory.copy()
        else:
            self.trajectory = []
        self.speed_x = 5
        self.speed_y = 5
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()


    def blit(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        self.__rotate()
        if self.rotation == Rotation.RIGHT.value:
            self.rect.x += self.speed
        elif self.rotation == Rotation.LEFT.value:
            self.rect.x -= self.speed
        elif self.rotation == Rotation.UP.value:
            self.rect.y -= self.speed
        elif self.rotation == Rotation.DOWN.value:
            self.rect.y += self.speed
        
    def move_by_insert_ball(self, delta, bound_x=1100, bound_y=700):
        if self.rotation == Rotation.LEFT.value or self.rotation == Rotation.RIGHT.value:
            if self.rect.x > bound_x - 30:
                hui = self.rect.x
                self.rect.x = bound_x
                self.rect.y += (30 - (bound_x - hui))
            else:
                self.rect.x += delta
        else:
            if self.rect.y > bound_y - 30:
                hui = self.rect.y
                self.rect.y = bound_y
                self.rect.x -= (30 - (bound_y - hui))
            else:
                self.rect.y += delta

    def __rotate(self):
        x, y, w, h = self.rect
        self.angle += 0.5
        self.image = pygame.transform.rotate(self.original_image,
                                             -self.angle % 360 - 90)
        # self.rect = pygame.rect()
        # self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.__strike()

    def __strike(self):
        dx = self.mouse_x - 520
        dy = self.mouse_y - 340
        angle = math.atan2(dy, dx)
        self.rect.x += 5 * math.cos(angle)
        self.rect.y += 5 * math.sin(angle)

    def find_path(self):
        dx = self.mouse_x - self.rect.x
        dy = self.mouse_y - self.rect.y
        angle = math.atan2(dy, dx)
        self.speed_x += 5 * math.cos(angle)
        self.speed_y += 5 * math.sin(angle)
        # k = abs(self.mouse_y - self.rect.y) // abs(self.mouse_x - self.rect.x)
        # if self.rect.x < self.mouse_x:
        #     delta_x = self.mouse_x - self.rect.x
        #     delta_x = max(delta_x, 300)
        #     self.speed_x = delta_x // 95
        # else:
        #     delta_x = self.rect.x - self.mouse_x
        #     delta_x = max(delta_x, 300)
        #     self.speed_x = -delta_x // 95
        # print(self.speed_x)
        # if self.rect.y < self.mouse_y:
        #     delta_y = self.mouse_y - self.rect.y
        #     delta_y = max(delta_y, 300*k)
        #     self.speed_y = delta_y // 95
        # else:
        #     delta_y = self.rect.y - self.mouse_y
        #     delta_y = max(delta_y, 300*k)
        #     self.speed_y = -delta_y // 95
        # print(self.speed_y)



