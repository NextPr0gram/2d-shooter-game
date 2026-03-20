import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, weapon_name, damage, accuracy, price, firerate):
        super().__init__()
        self.weapon_name = weapon_name
        self.damage = damage
        self.accuracy = accuracy
        self.firerate = firerate
        # self.top_texture = pygame.image.load(top_texture_path)
        # self.side_texture = pygame.image.load(side_texture_path)
        self.price = price


# weapons
weapons_group = pygame.sprite.Group()
rifle = Weapon("rifle", 10, 10, 1000, 200)
smg = Weapon("smg", 10, 20, 1000, 100)
lmg = Weapon("lmg", 10, 30, 1000, 400)
weapons_group.add(rifle, smg, lmg)
