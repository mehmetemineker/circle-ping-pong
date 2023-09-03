import os.path

import pygame.image

sprites = {}


def load_sprites():
    path = os.path.join("assets", "sprites")
    for file_name in os.listdir(path):
        sprites[file_name.split('.')[0]] = pygame.image.load(os.path.join(path, file_name))


def get_sprite(name):
    return sprites[name]
