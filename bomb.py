import pygame

from enums import Rotation


class Bomb(pygame.sprite.Sprite):
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
        self.radius = 30

    def move(self):
        if self.rotation == Rotation.RIGHT.value:
            self.rect.x += self.moving_speed
        elif self.rotation == Rotation.LEFT.value:
            self.rect.x -= self.moving_speed
        elif self.rotation == Rotation.UP.value:
            self.rect.y -= self.moving_speed
        elif self.rotation == Rotation.DOWN.value:
            self.rect.y += self.moving_speed

    def blit(self):
        self.screen.blit(self.image, self.rect)