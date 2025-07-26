from .room import Room
from typing import Dict, Tuple
from random import choice

class Map:
    def __init__(self):
        self._create_rooms()
        self._link_rooms()
        self._place_treasure()

    def _create_rooms(self):
        self.rooms: Dict[Tuple[int, int], Room] = {}
        for x in range(3):
            for y in range(3):
                self.rooms[(x, y)] = Room(x,y)
        print(self.rooms)

    def print_rooms(self):
        print("Map Layout:")
        for x in range(3):
            for y in range(3):
                room = self.rooms[(x, y)]
                print(f"Room ({x}, {y}): has_treasure={room.has_treasure}")

    def _link_rooms(self):
        for (x, y), room in self.rooms.items():
            # Link to north neighbour if it exists
            if y > 0:
                room.north = self.rooms[(x, y-1)]
            
            # Link to south neighbour if it exists  
            if y < 2:
                room.south = self.rooms[(x, y+1)]
                
            # Link to east neighbour if it exists
            if x < 2:
                room.east = self.rooms[(x+1, y)]
                
            # Link to west neighbour if it exists
            if x > 0:
                room.west = self.rooms[(x-1, y)]

    def _place_treasure(self):
        # Randomly select one room to place the treasure
        treasure_room = choice(list(self.rooms.values()))
        treasure_room.has_treasure = True
