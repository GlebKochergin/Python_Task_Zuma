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
        self.image = pygame.transform.rotate(self.image, -90)
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


    def blit(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        # self.__rotate()
        if self.rotation == Rotation.RIGHT.value:
            self.rect.x += self.speed
        elif self.rotation == Rotation.LEFT.value:
            self.rect.x -= self.speed
        elif self.rotation == Rotation.UP.value:
            self.rect.y -= self.speed
        elif self.rotation == Rotation.DOWN.value:
            self.rect.y += self.speed

    def __rotate(self):
        x, y, w, h = self.rect
        self.angle += 0.5
        self.image = pygame.transform.rotate(self.original_image,
                                             -self.angle % 360 - 90)
        # self.rect = pygame.rect()
        # self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        self.rect.x += 5
