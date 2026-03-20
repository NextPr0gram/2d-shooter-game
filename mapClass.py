import pygame
from settings import *
from wallClass import *
import random


class Map():
    def __init__(self):
        self.map_data = []

    def load_data(self):
        with open("map_settings.txt", "rt") as f:
            for line in f:
                self.map_data.append(line)

    def draw_wall(self):
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    wall = Wall(col, row, CORNER1)
                    wall_group.add(wall)
                if tile == "+":
                    wall = Wall(col, row, WALL_UP)
                    wall_group.add(wall)
                if tile == "3":
                    wall = Wall(col, row, CORNER3)
                    wall_group.add(wall)
                if tile == "-":
                    wall = Wall(col, row, WALL_SIDE)
                    wall_group.add(wall)
                if tile == "5":
                    wall = Wall(col, row, WALL5)
                    wall_group.add(wall)
                if tile == "7":
                    wall = Wall(col, row, CORNER7)
                    wall_group.add(wall)
                if tile == "9":
                    wall = Wall(col, row, CORNER9)
                    wall_group.add(wall)
                """if tile == ".":
                    if row % 4 == 0:
                        floor = Wall(col, row, random.choice(FLOORS2))
                    elif col % 8 == 0:
                        floor = Wall(col, row, random.choice(FLOORS2))
                    else:
                        floor = Wall(col, row, random.choice(FLOORS1))
                    floor_group.add(floor)"""

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, TILESIZE):
            pygame.draw.line(SCREEN, LIGHT_GRAY, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TILESIZE):
            pygame.draw.line(SCREEN, LIGHT_GRAY, (0, y), (SCREEN_WIDTH, y))


# map
map = Map()
map.load_data()
map.draw_wall()
def set_spawn(x, y):
    for wall in wall_group:
        wall.rect.y -= x
        wall.rect.x -= y
    for floor in floor_group:
        floor.rect.y -= x
        floor.rect.x -= y
set_spawn(0, 1600)