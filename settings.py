import pygame

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (40, 40, 40)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 220, 152)

# game settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.HWACCEL)
CLOCK = pygame.time.Clock()
TILESIZE = 32
GRID_WIDTH = SCREEN_WIDTH / TILESIZE
GRID_HEIGHT = SCREEN_HEIGHT / TILESIZE
FPS = 60

# player settings
PLAYER_SPEED = 3
BULLET_SPEED = 10
PLAYER_TEXTURE_1 = "textures\player1.png"
PLAYER_TEXTURE_2 = "textures\player2.png"
PLAYER_TEXTURE_3 = "textures\player3.png"
PLAYER_TEXTURE_4 = "textures\player4.png"
PLAYER_TEXTURE_5 = "textures\player5.png"
PLAYER_TEXTURE_6 = "textures\player6.png"

# wall settings
CORNER1 = "textures\corner1.png"
WALL_UP = "textures\wall_up.png"
CORNER3 = "textures\corner3.png"
WALL_SIDE = "textures\wall_side.png"
WALL5 = "textures\wall5.png"
CORNER7 = "textures\corner7.png"
CORNER9 = "textures\corner9.png"
BG = "textures\BG.png"
FLOOR = "textures\cfloor.png"
FLOOR1 = "textures\cfloor1.png"
FLOOR2 = "textures\cfloor2.png"
FLOOR3 = "textures\cfloor3.png"
FLOOR_GRAY1 = "textures\cfloor_gray1.png"
FLOOR_GRAY2 = "textures\cfloor_gray2.png"
FLOOR_GRAY3 = "textures\cfloor_gray3.png"
FLOOR_GRAY4 = "textures\cfloor_gray4.png"
FLOORS1 = [FLOOR_GRAY2, FLOOR_GRAY3]
FLOORS2 = [FLOOR_GRAY1,FLOOR_GRAY1, FLOOR_GRAY1, FLOOR_GRAY2]

