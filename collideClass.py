import pygame
from settings import *


class Collider(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.Surface((width, height))
        self.image.set_alpha(128)
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# player colliders
collider_group = pygame.sprite.Group()
c_up = Collider(50, 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 20)
c_down = Collider(50, 20, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 20)
c_left = Collider(20, 50, SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2)
c_right = Collider(20, 50, SCREEN_WIDTH / 2 + 20, SCREEN_HEIGHT / 2)
collider_group.add(c_up, c_down, c_left, c_right)
