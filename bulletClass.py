import pygame
import math
from settings import *
from wallClass import *
import random


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, angle):
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.angle = angle
        sign = [1, -1]
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.dir = (mouse_x - x, mouse_y - y)
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        self.angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))
        self.image = pygame.Surface((10, 2)).convert_alpha()
        self.image.fill(RED)
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.speed = BULLET_SPEED
        self.rect = self.image.get_rect()

    def bullet_colliding(self, bullet):
        return pygame.sprite.spritecollide(bullet, wall_group, False)

    def update(self):
        self.pos_x = self.pos_x + self.dir[0] * self.speed
        self.pos_y = self.pos_y + self.dir[1] * self.speed
        self.rect.x, self.rect.y = self.pos_x, self.pos_y

    def draw(self, surf):
        self.bullet_rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        surf.blit(self.image, self.bullet_rect)
    def get_angle(self):
        return self.angle

bullets_group = pygame.sprite.Group()
