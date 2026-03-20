import math
from settings import *
from weaponClass import *
from bulletClass import *
from collideClass import *
from wallClass import *


class Player(pygame.sprite.Sprite):
    def __init__(self,player_number, picture_path, pos_x, pos_y, speed, weapon, other_group, is_other):
        super().__init__()
        self.player_number = player_number
        self.original_image = pygame.image.load(picture_path)
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.speed = speed
        self.angle = 0
        self.weapon = weapon
        self.player_x = pos_x
        self.player_y = pos_y
        self.other_group = other_group
        self.is_other = is_other
        self.health = 100

    def update(self):
        if self.is_other == False:
            self.mouse_x = pygame.mouse.get_pos()[0]
            self.mouse_y = pygame.mouse.get_pos()[1]
            self.angle = math.atan2(self.mouse_y - self.rect.centery, self.mouse_x - self.rect.centerx)
            self.angle = -90 + (self.angle * (180 / math.pi)) * -1
            self.angle = round(self.angle)
        self.image, self.rect = self.rotate()
    def get_damage(self, damage):
        self.health -= damage
    def get_player_pos(self):
        return self.player_x, self.player_y

    def moveLeft(self):
        self.player_x -= self.speed
        for wall in wall_group:
            wall.rect.x += self.speed
        for floor in floor_group:
            floor.rect.x += self.speed
        for player in self.other_group:
            player.rect.x += self.speed
        for bullet in bullets_group:
            bullet.pos_x += self.speed

        # Now you have updated the position you need to send a message to the server to tell them what you have done (e.g. move left) or tell the server your new position (self.x,self.y)
        # This is so the server can tell the "other" connection that the non-controlled player needs to move and where to move them to.

    def moveRight(self):
        self.player_x += self.speed
        for wall in wall_group:
            wall.rect.x -= self.speed
        for floor in floor_group:
            floor.rect.x -= self.speed
        for player in self.other_group:
            player.rect.x -= self.speed
        for bullet in bullets_group:
            bullet.pos_x -= self.speed

    def moveUp(self):
        self.player_y -= self.speed
        for wall in wall_group:
            wall.rect.y += self.speed
        for floor in floor_group:
            floor.rect.y += self.speed
        for player in self.other_group:
            player.rect.y += self.speed
        for bullet in bullets_group:
            bullet.pos_y += self.speed

    def moveDown(self):
        self.player_y += self.speed
        for wall in wall_group:
            wall.rect.y -= self.speed
        for floor in floor_group:
            floor.rect.y -= self.speed
        for player in self.other_group:
            player.rect.y -= self.speed
        for bullet in bullets_group:
            bullet.pos_y -= self.speed

    def rotate(self):
        rotated_image = pygame.transform.rotozoom(self.original_image, self.angle, 1)
        rotated_rect = rotated_image.get_rect(center=(self.rect.center))
        return rotated_image, rotated_rect

    def collide_with_walls_top(self, ):
        return pygame.sprite.spritecollide(c_up, wall_group, False)

    def collide_with_walls_bottom(self, ):
        return pygame.sprite.spritecollide(c_down, wall_group, False)

    def collide_with_walls_left(self, ):
        return pygame.sprite.spritecollide(c_left, wall_group, False)

    def collide_with_walls_right(self, ):
        return pygame.sprite.spritecollide(c_right, wall_group, False)

    def shoot(self):
        # pygame.draw.line(SCREEN, ORANGE, self.rect.center, (self.mouse_x, self.mouse_y), 6)
        # pygame.draw.line(SCREEN, RED, self.rect.center, (self.mouse_x, self.mouse_y), 2)
        bullets_group.add(Bullet(self.rect.centerx, self.rect.centery, 0))



# players


"""def swap_players(client_id):
    if client_id == 0:
        p1 = Player(PLAYER_TEXTURE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, smg)
        p2 = Player(PLAYER_TEXTURE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle)
    elif client_id == 1:
        p1 = Player(PLAYER_TEXTURE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, rifle)
        p2 = Player(PLAYER_TEXTURE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_SPEED, smg)"""
