from .player import Player
from game.map import Map

def main():
    name: str = input("Enter your name: ")
    player = Player(name)
    print(f"Welcome, {player.name}!")


if __name__ == "__main__":
    main()

map_instance = Map() # remove
map_instance.print_rooms() # remove