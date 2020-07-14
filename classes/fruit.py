from __future__ import annotations

from .postion import Position


class Fruit:
    def __init__(self, position: Position, is_eaten: bool = False):
        self.position = position
        self.is_eaten = is_eaten

    def eat(self):
        self.is_eaten = True

    def get_position(self) -> Position:
        return self.position
