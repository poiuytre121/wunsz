from __future__ import annotations
from .color import Color
from .postion import Position


class Segment:
    def __init__(self, position: Position, color: Color):
        self.color = color
        self.position = position
