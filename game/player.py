from random import choice
from .map import Map

class Player:
    def __init__(self, name: str, map: Map):
        self.name = name
        self.current_room = choice(list(map.rooms.values()))