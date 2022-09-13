from typing import Any

import pygame.sprite
from pygame import Surface

from common.constants.visible_objects import ConstantsTile
from settings import Screen


class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        positions: tuple[int, int],
        sprite_groups: list[pygame.sprite.Group],
        sprite_type: Any,
        surface: Surface = pygame.Surface((Screen.TILESIZE, Screen.TILESIZE))
    ) -> None:
        super(Tile, self).__init__(*sprite_groups)
        self.sprite_type = sprite_type
        self.image = surface

        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(positions[0], positions[1] - Screen.TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=positions)
        self.hit_box = self.rect.inflate(*ConstantsTile.HITBOX)
