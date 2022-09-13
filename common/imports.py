import os
from csv import reader

import pygame.image
from pygame import Surface


def import_csv_layout(path: str) -> list[list[int]]:
    imported_layout = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            imported_layout.append(list(map(int, row)))

    return imported_layout


def import_folder(path: str) -> list[Surface]:
    surfaces = []
    for _, __, image_files in os.walk(path):
        for image in sorted(image_files):
            full_path = f'{path}/{image}'
            surfaces.append(pygame.image.load(full_path).convert_alpha())

    return surfaces
