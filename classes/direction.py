from __future__ import annotations
from enum import Enum


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
    STOP = 'stop'

    def is_opposite_or_same_to(self, direction: Direction) -> bool:
        _opposites = {
            self.UP: self.DOWN,
            self.DOWN: self.UP,
            self.LEFT: self.RIGHT,
            self.RIGHT: self.LEFT
        }
        if direction == self:
            return True
        elif _opposites.get(direction) == self:
            return True
        else:
            return False
