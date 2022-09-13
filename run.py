from game.game import Game


class GameInitializer:
    def __init__(self, game: Game) -> None:
        self.game = game

    def __start_game(self) -> None:
        self.game.start()

    def run(self) -> None:
        self.__start_game()


game_initializer = GameInitializer(game=Game())
game_initializer.run()
