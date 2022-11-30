import pygame
from pygame.math import Vector2


class Frog(pygame.sprite.Sprite):
    def __init__(self, screen, texture_path):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(texture_path)
        x, y, w, h = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (w // 3, h // 3))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect(center=(600, 400))
        self.rect.x = 600 - 100
        self.rect.y = 400 - 100
        self.rect.width = w // 3
        self.rect.height = h // 3
        self.original_image = self.image
        self.screen.blit(self.image, self.rect)

    def blit(self):
        self.screen.blit(self.image, self.rect)

    def rotate(self):
        x, y, w, h = self.rect
        direction = pygame.mouse.get_pos() - Vector2(x + w // 2, y + h // 2)
        radius, angle = direction.as_polar()
        self.image = pygame.transform.rotate(self.original_image,  -angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)
