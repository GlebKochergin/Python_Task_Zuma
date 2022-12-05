import math

import pygame
from pygame.math import Vector2

from ball import Ball


class Frog(pygame.sprite.Sprite):
    def __init__(self, screen, texture_path):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(texture_path)
        x, y, w, h = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (w // 3, h // 3))
        self.image = pygame.transform.rotate(self.image, -110)
        self.rect = self.image.get_rect(center=(600, 400))
        self.rect.x = 600 - 100
        self.rect.y = 400 - 100
        self.rect.width = w // 3
        self.rect.height = h // 3
        self.original_image = self.image
        self.line = Vector2(538, 378)
        self.original_line = self.line
        self.screen.blit(self.image, self.rect)
        self.line_x = 538
        self.line_y = 378
        self.ball = Ball(self.screen, "src/textures/KostyaBall.png", 520, 340)
        self.orig_rect = pygame.Surface((200, 100))
        self.around_rect = self.orig_rect.get_rect()
        #
        # self.shape_surf = pygame.transform.rotate(self.shape_surf, -110)
        # pygame.draw.rect(self.shape_surf, (255, 255, 255, 127),
        #                  self.shape_surf.get_rect())

    # screen.blit(self.hole, (122, 350))

    def blit(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.ball.image, self.ball.rect)
        # self.screen.blit(self.shape_surf, (self.rect.x, self.rect.y))
        # self.screen.blit(self.around_rect, (self.around_rect.x, self.around_rect.y))
        # pygame.draw.circle(self.screen, (255, 0, 0), (600, 400), 62, 1)
        # pygame.draw.line(self.screen, (255, 0, 0), (600, 400), (self.line.x, self.line.y), 1)


    def rotate(self):
        x, y, w, h = self.rect
        direction = pygame.mouse.get_pos() - Vector2(x + w // 2, y + h // 2)
        radius, angle = direction.as_polar()
        # print(angle)
        self.image = pygame.transform.rotate(self.original_image,  -angle - 90)
        self.line = self.original_line.rotate(2*angle)
        # radius, angle = self.line.as_polar()
        # self.line = direction - self.line
        self.rect = self.image.get_rect(center=self.rect.center)

    # def change_line_points(self):
    #     self.line_x = self.line_x * math.cos(self.angle) + self.line_y * math.sin(self.angle)
    #     self.line_y = self.line_x * math.sin(self.angle) + self.line_y * math.cos(self.angle)
