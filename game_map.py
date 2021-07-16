import numpy as np
from tcod.console import Console
import tile_types

class GameMap:

    def __init__(self, width: int, height: int):

        self.width = width
        self.height = height
        # Numpy 2D array filled with tile_type.floor --> Out, as we'll start filling everything will walls, and then carving the floors.
        #self.tiles = np.full( (width,height), fill_value = tile_types.floor, order="F")
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        # FOV implementation:
        self.visible = np.full((width, height), fill_value=False, order="F") # Tiles the Player can currently see
        self.explored = np.full((width, height), fill_value=False, order="F")  # Tiles the Player has seen before

        # TEST: Creates a 3-tile-wide-wall at the specified location
        # self.tiles[30:33, 22] = tile_types.wall

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        # We can use this to ensure the player doesn’t move beyond the map, into the void.
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        # Using the Console class’s tiles_rgb method, we can quickly render the entire map. This method proves much faster than using the console.print method that we use for the individual entities.
        #console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"] --> Implementing FOV:
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist = [self.visible, self.explored],
            choicelist = [self.tiles["light"], self.tiles["dark"]],
            default = tile_types.SHROUD
        )
