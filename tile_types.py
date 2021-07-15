from typing import Tuple
import numpy as np

# Tile graphics structured type
# dtype creates a data type that Numpy can use, behaves similarly to a C Struct, so we can have out custom datatype for Tile.
graphic_dt = np.dtype([

	("ch", np.int32),  # The character, represented in integer format. We’ll translate it from the integer into Unicode.
	("fg", "3B"),  # ForeGround color . 3B = 3 unsigned bytes which can be used for RGB color codes.
	("bg", "3B"), # Background color, similar to foreground.

])

tile_dt = np.dtype([

	("walkable", np.bool),  # True if this tile can be walked over.
	("transparent", np.bool),  # True if this tile doesn't block FOV.
	("dark", graphic_dt),  # Graphics for when this tile is not in FOV. later on, we’ll want to differentiate between tiles that are and aren’t in the field of view. dark will represent tiles that are not in the current field of view.

])

def new_tile(*, walkable: int, transparent: int, dark: int) -> np.ndarray:

	return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)
wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)