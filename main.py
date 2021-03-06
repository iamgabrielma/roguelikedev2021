#!/usr/bin/env python3
import tcod

from input_handlers import EventHandler
from entity import Entity
from engine import Engine
#from game_map import GameMap --> Out, moving to proc gen dungeons
from procGen import generate_dungeon

def testing_func():
    return "Testing"

def main() -> None:

    # Screen size
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 50

    # ProcGen details
    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    # Which font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # Instantiate our event handler
    event_handler = EventHandler()

    # Instantiate the player Entity and add it to our entities dictionary
    player = Entity(int(screen_width/2), int(screen_height/2), "@", (255, 255, 255))
    enemy = Entity(int(screen_width/(2-5)), int(screen_height/2), "@", (255, 255, 0))
    entities = {player, enemy}

    # Map
    #game_map = GameMap(map_width,map_height)
    #game_map = generate_dungeon(map_width, map_height) --> moving to ProcGen:
    game_map = generate_dungeon(max_rooms=max_rooms, room_min_size=room_min_size, room_max_size=room_max_size, map_width=map_width, map_height=map_height, player=player)

    # Pass everything into the Engine
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    # Creates the screen ( the Terminal )
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset, # Tileset we've previously defined
            title="PlagueRogue",
            vsync=True, # TODO: Check what does vsync do
    ) as context:
        # Creates the Console inside the Terminal, we're also fitting the Console to the Terminal screen
        # By default, numpy accesses 2D arrays in [y, x] order, by setting order="F", we can change this to be [x, y] instead.
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # Game loop starts:
        while True:
            #root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            engine.render(console=root_console, context=context)
            
            events = tcod.event.wait() # this waits for user input to process.
            
            engine.handle_events(events)
            # present() is what will print on screen, is like the loop Update() method
            context.present(root_console)

if __name__ == "__main__":
    main()

