from typing import Optional

class Room:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.north: Optional["Room"] = None
        self.south: Optional["Room"] = None
        self.east: Optional["Room"] = None
        self.west: Optional["Room"] = None
        self.has_treasure: bool = False