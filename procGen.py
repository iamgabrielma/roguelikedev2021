# This will house our Procedural Map Generator
from typing import Tuple
from game_map import GameMap
import tile_types


class RectangularRoom:
    def __init__(self, x: int, y: int, width: int, height: int):
        # Top Left Corner X, Y
        self.x1 = x
        self.y1 = y
        # Bottom Right Corner, computer from X Y + Width/Height
        self.x2 = x + width
        self.y2 = y + height

    @property
    def center(self) -> Tuple[int, int]:
        # This will act as read-only var, describes the center of the room
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)

        return center_x, center_y

    @property
    def inner(self) -> Tuple[slice, slice]:
        # Returns 2 slices, representing the inner area of the room, the part we're "digging out"
        # The +1 ensures that we'll always have a wide tile wall between rooms, unless we choose to overlap them
        """Returns the inner area of this room as a 2D array index."""
        return slice(self.x1 + 1, self.x2), slice(self.y1 + 1, self.y2)

def generate_dungeon(map_width, map_height) -> GameMap:

    dungeon = GameMap(map_width, map_height)

    room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
    room_2 = RectangularRoom(x=35, y=15, width=10, height=15)

    dungeon.tiles[room_1.inner] = tile_types.floor
    dungeon.tiles[room_2.inner] = tile_types.floor

    return dungeon