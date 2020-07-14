from __future__ import annotations
from .color import Color
from .postion import Position


class Segment:
    def __init__(self, position: Position, color: Color, is_head: bool = False, previous: Segment = None):
        self.color = color
        self.position = position
        self.is_head = is_head
        self.previous = previous

    @classmethod
    def from_segment(cls, segment: Segment) -> Segment:
        return Segment(segment.position, segment.color, previous=segment)

    def draw(self):
        pass