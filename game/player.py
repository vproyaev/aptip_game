from typing import Any

import pygame.sprite

from common.constants.collision import ConstantsCollision
from common.constants.player import ConstantsPlayer


class Player(pygame.sprite.Sprite):
    def __init__(
        self,
        positions: tuple[int, int],
        sprite_groups: list[pygame.sprite.Group],
        obstacle_sprites: pygame.sprite.Group
    ):
        super(Player, self).__init__(*sprite_groups)

        self.image = pygame.image.load('./src/graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=positions)
        self.hit_box = self.rect.inflate(*ConstantsPlayer.HITBOX)

        self.obstacle_sprites = obstacle_sprites

        self.direction = pygame.math.Vector2()
        self.speed: int = ConstantsPlayer.SPEED

    def update(self, *args: Any, **kwargs: Any) -> None:
        self.vertical_directions()
        self.horizontal_directions()
        self.move(self.speed)

    def move(self, speed: int) -> None:
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hit_box.x += self.direction.x * speed
        self.collision(ConstantsCollision.DIRECTION_HORIZONTAL)

        self.hit_box.y += self.direction.y * speed
        self.collision(ConstantsCollision.DIRECTION_VERTICAL)

        self.rect.center = self.hit_box.center

    def vertical_directions(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def horizontal_directions(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def collision(self, direction: str) -> None:
        if direction == ConstantsCollision.DIRECTION_HORIZONTAL:
            for sprite in self.obstacle_sprites:
                sprite: Player

                if sprite.hit_box.colliderect(self.hit_box):
                    if self.direction.x > 0:  # moving right
                        self.hit_box.right = sprite.hit_box.left
                    if self.direction.x < 0:  # moving left
                        self.hit_box.left = sprite.hit_box.right

        if direction == ConstantsCollision.DIRECTION_VERTICAL:
            for sprite in self.obstacle_sprites:
                sprite: Player

                if sprite.hit_box.colliderect(self.hit_box):
                    if self.direction.y > 0:  # moving down
                        self.hit_box.bottom = sprite.hit_box.top
                    if self.direction.y < 0:  # moving up
                        self.hit_box.top = sprite.hit_box.bottom
