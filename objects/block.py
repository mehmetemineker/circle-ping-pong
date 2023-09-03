import pygame.sprite

import assets
import configs


class Block(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.transform.scale(assets.get_sprite("block"), (configs.CIRCLE_RADIUS, configs.CIRCLE_RADIUS))
        self.rect = self.image.get_rect(center=(configs.CIRCLE_X, configs.CIRCLE_Y))
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        super().__init__(*groups)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.angle -= 10
        elif keys[pygame.K_RIGHT]:
            self.angle += 10

        self.image = pygame.transform.rotate(
            pygame.transform.scale(assets.get_sprite("block"), (configs.CIRCLE_RADIUS, configs.CIRCLE_RADIUS)),
            self.angle)
        self.rect = self.image.get_rect(center=(configs.CIRCLE_X, configs.CIRCLE_Y))
        self.mask = pygame.mask.from_surface(self.image)
