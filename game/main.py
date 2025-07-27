from .player import Player
from .map import Map

def main():
    name: str = input("Enter your name: ")
    game_map = Map()
    player = Player(name, game_map)
    print(f"Welcome, {player.name}!")

    print("Game Map:", game_map)
    print("Rooms:", getattr(game_map, "rooms", "No rooms attribute"))
    print("Player:", player)
    print(f"Player's current room: ({player.current_room.x}, {player.current_room.y})")


if __name__ == "__main__":
    main()
# game/main.py