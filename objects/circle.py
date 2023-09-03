import pygame.sprite

import assets
import configs


class Circle(pygame.sprite.Sprite):
    def __init__(self, *groups):
        self.image = pygame.transform.scale(assets.get_sprite("circle"), (configs.CIRCLE_RADIUS, configs.CIRCLE_RADIUS))
        self.image.set_alpha(175)
        self.rect = self.image.get_rect(center=(configs.CIRCLE_X, configs.CIRCLE_Y))
        super().__init__(*groups)
