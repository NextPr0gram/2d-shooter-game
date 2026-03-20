"""
#factorial
def fact(num):
    if num == 1:
        return 1
    else:
        return num*fact(num-1)


print(fact(13))
list = ["t", "h", "e", "q", "u", "i", "c", "k", "b", "r", "o", "w", "n", "f", "o", "x"]


def search(l, lst, x):
    if lst == []:
        return -1
    elif lst[0] == 1:
        return x;
    else:
        return search(l, lst[1:], x + 1)


l = "e"
print(search(l, list, 0))

import pygame, sys
pygame.init()

vec = pygame.math.Vector2
HEIGHT = 350
WIDTH = 700
SPEED = 0.3
FPS = 60
FPS_CLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player_Sprite_R.png")
        self.rect = self.image.get_rect()
        self.angle = 0
        self.pos = vec((340, 240))
        self.speed = 2

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_a]:
            self.pos.x -= self.speed
        if pressed_keys[pygame.K_d]:
            self.pos.x += self.speed
        if pressed_keys[pygame.K_w]:
            self.pos.y -= self.speed
        if pressed_keys[pygame.K_s]:
            self.pos.y += self.speed
        self.rect.center = self.pos
        if pressed_keys[pygame.K_RIGHT]:
            pygame.
            self.rect = new_image.get_rect()
        if pressed_keys[pygame.K_LEFT]:
            pass
player = Player()

while True:

    for event in pygame.event.get():
        # Will run when the close window button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    displaysurface.fill(WHITE)
    player.move()
    displaysurface.blit(player.image, player.rect)
    pygame.display.flip()
    FPS_CLOCK.tick(FPS)



"""
import os


#for x in range(0, 6):
#    exec(open('main.py').read())