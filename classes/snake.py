from __future__ import annotations

from .color import Color
from .direction import Direction
from .fruit import Fruit
from .postion import Position
from .segment import Segment


class Snake:
    def __init__(self, position: Position, speed: int = 30, color: Color = Color.BLUE):
        self.direction = Direction.STOP
        self.speed = speed
        self.color = color
        self.segments = [Segment(position, self.color, True)]

    def change_direction(self, direction: Direction):
        if not self.direction.is_opposite_or_same_to(direction):
            self.direction = direction

    def move(self):
        pass

    def eat(self, fruit: Fruit):
        self.segments.append(Segment.from_segment(self.segments[-1]))

    def have_bitten_itself(self) -> bool:
        pass

    def get_position(self) -> Position:
        return self.segments[0].position

    def is_in_snake(self, position: Position) -> bool:
        for segment in self.segments:
            if segment.position == position:
                return True
        return False
