import random

import pygame.sprite

import assets
import configs
from objects.block import Block


class Ball(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.transform.scale(assets.get_sprite("ball"), (10, 10))
        self.rect = self.image.get_rect(center=(configs.CIRCLE_X, configs.CIRCLE_Y))
        self.mask = pygame.mask.from_surface(self.image)

        self.mx = 1
        self.my = 1

        super().__init__(*groups)

    def update(self):
        self.rect.x += self.mx
        self.rect.y += self.my

    def check_collision(self, sprites):
        x_sign = 0
        y_sign = 0
        for sprite in sprites:
            if ((type(sprite) is Block) and
                    sprite.mask.overlap(self.mask, (self.rect.x - sprite.rect.x, self.rect.y - sprite.rect.y))):
                if self.rect.x < configs.CIRCLE_X and self.rect.y < configs.CIRCLE_Y:
                    x_sign = 1
                    y_sign = 1
                elif self.rect.x > configs.CIRCLE_X and self.rect.y > configs.CIRCLE_Y:
                    x_sign = -1
                    y_sign = -1
                elif self.rect.x > configs.CIRCLE_X and self.rect.y < configs.CIRCLE_Y:
                    x_sign = -1
                    y_sign = 1
                elif self.rect.x < configs.CIRCLE_X and self.rect.y > configs.CIRCLE_Y:
                    x_sign = 1
                    y_sign = -1

                self.mx = random.uniform(1, 2) * x_sign
                self.my = random.uniform(1, 2) * y_sign
