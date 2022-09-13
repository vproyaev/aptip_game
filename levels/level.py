import random

import pygame.sprite

from common.imports import import_csv_layout
from common.imports import import_folder
from game.camera import YSortCameraGroup
from game.player import Player
from levels.tile import Tile
from settings import Screen


class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.render_map()

    def start(self) -> None:
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()

    def render_map(self) -> None:
        layouts = {
            'boundary': import_csv_layout('./src/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('./src/map/map_Grass.csv'),
            'object': import_csv_layout('./src/map/map_Objects.csv'),
        }
        graphics = {
            'grass': import_folder('./src/graphics/grass'),
            'objects': import_folder('./src/graphics/objects')
        }
        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != -1:
                        x = col_index * Screen.TILESIZE
                        y = row_index * Screen.TILESIZE
                        positions = (x, y)

                        if style == 'boundary':
                            Tile(positions, [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            Tile(positions, [self.visible_sprites], 'grass', random.choice(graphics[style]))
                        if style == 'object':
                            Tile(
                                positions,
                                [self.visible_sprites, self.obstacle_sprites],
                                'object',
                                graphics['objects'][col]
                            )

        self.player = Player((2000, 1430), [self.visible_sprites], self.obstacle_sprites)
