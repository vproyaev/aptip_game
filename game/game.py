import sys

import pygame as pygame

from levels.level import Level
from settings import Screen


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen_resolution: tuple[int, int] = (Screen.WIDTH, Screen.HEIGHT)
        self.screen = pygame.display.set_mode(self.screen_resolution)

        self.__initialize_screen()

        self.clock = pygame.time.Clock()

        self.level = Level()

    @staticmethod
    def __initialize_screen() -> None:
        pygame.display.set_caption('Trash King')

    def start(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.start()
            pygame.display.update()
            self.clock.tick(Screen.FPS)
