from __future__ import annotations
import tcod
import random
from typing import Tuple, Iterator, List, TYPE_CHECKING
from game_map import GameMap
import tile_types

if TYPE_CHECKING:
    from entity import Entity

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

    def intersects(self, other: RectangularRoom) -> bool:
        """Returns True if this room overlaps with another RectangularRoom"""
        return(
            self.x1 <= other.x2
            and self.x2 >= other.x1
            and self.y1 >= other.y2
            and self.y2 >= other.y1
        )

# def generate_dungeon(map_width, map_height) -> GameMap:
#
#     dungeon = GameMap(map_width, map_height)
#
#     room_1 = RectangularRoom(x=20, y=15, width=10, height=15)
#     room_2 = RectangularRoom(x=35, y=15, width=10, height=15)
#
#     dungeon.tiles[room_1.inner] = tile_types.floor
#     dungeon.tiles[room_2.inner] = tile_types.floor
#
#     for x, y in tunnel_between(room_2.center, room_1.center):
#         dungeon.tiles[x,y] = tile_types.floor
#
#     return dungeon

## Rewritten version for Procedural Dungeon Generation:
def generate_dungeon(max_rooms: int, room_min_size: int, room_max_size: int, map_width: int, map_height: int, player: Entity) -> GameMap:

    dungeon = GameMap(map_width, map_height)
    rooms: List[RectangularRoom] = []

    for r in range(max_rooms):
        room_width = random.randint(room_min_size, room_max_size)
        room_height = random.randint(room_min_size, room_max_size)

        x = random.randint(0, dungeon.width - room_width - 1)
        y = random.randint(0, dungeon.height - room_width - 1)

        new_room = RectangularRoom(x, y, room_width, room_height)

        # Check for overlap between rooms:
        if any(new_room.intersects(other_room) for other_room in rooms):
            continue # If there's an overlap, skip and keep trying
        # If no intersections, then room is valid

        # Dig out the inner area
        dungeon.tiles[new_room.inner] = tile_types.floor

        if len(rooms) == 0:
            # first room, where player starts
            player.x, player.y = new_room.center
        else:
            # All rooms after this, dig out tunnels to the previous one.
            for x, y in tunnel_between(rooms[-1].center, new_room.center):
                dungeon.tiles[x, y] = tile_types.floor

        rooms.append(new_room)

    return dungeon

def tunnel_between(start: Tuple[int,int], end: Tuple[int,int]) -> Iterator[Tuple[int,int]]:
    """ Takes 2 arguments, both Tuples with an X and Y coordinates, and Returns another Tuple representing an L-shaped tunnel between these 2 points """
    x1, y1 = start
    x2, y2 = end

    if random.random() < 0.5: # 50% chance
        corner_x, corner_y = x2, y1 # Move horizontally, then vertically.
    else:
        corner_x, corner_y = x1, y2 # Move vertically, then horizontally.

    # Generate the coordinates for this tunnel.
    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y # Returns a generator
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y # Returns a generator