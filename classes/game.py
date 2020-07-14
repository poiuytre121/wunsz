from __future__ import annotations
from .snake import Snake


class Game:
    def __init__(self, window, number_of_players):
        self.window = window
        self.number_of_players = number_of_players
        self._init_snakes()

    def _init_snakes(self):
        self.snakes = []
        for player_number in range(self.number_of_players):
            self.snakes.append(Snake())

    def play(self):
        pass
