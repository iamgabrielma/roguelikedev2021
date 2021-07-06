#!/usr/bin/env python3
import tcod
#from actions import EscapeAction, MovementAction

from input_handlers import EventHandler
from entity import Entity
from engine import Engine

def testing_func():
    return "Testing"

def main() -> None:

    # Screen size
    screen_width = 80
    screen_height = 50

    # Player Movement --> We've moved this to use the Entity class instead.
    # player_x = int(screen_width/2)
    # player_y = int(screen_height / 2)

    # Which font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # Instanciate our event handler
    event_handler = EventHandler()

    # Instantiate the player Entity and add it to our entities dictionary
    player = Entity(int(screen_width/2), int(screen_height/2), "@", (255, 255, 255))
    entities = {player}

    engine = Engine(entities= entities , event_handler= event_handler, player= player)

    # Creates the screen ( the Terminal )
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset, # Tileset we've previously defined
            title="Oxygen",
            vsync=True, # TODO: Check what does vsync do
    ) as context:
        # Creates the Console inside the Terminal, we're also fitting the Console to the Terminal screen
        # By default, numpy accesses 2D arrays in [y, x] order, by setting order="F", we can change this to be [x, y] instead.
        root_console = tcod.Console(screen_width, screen_height, order="F")
        # Game loop starts:
        while True:
            #root_console.print(x=player.x, y=player.y, string=player.char, fg=player.color)
            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)
            # present() is what will print on screen, is like the loop Update() method
            context.present(root_console)
            #root_console.clear() # We clear the console before running the next loop
            # Graceful program exit without crashing it, by pressing X in the console window.
            # for event in tcod.event.wait(): # this waits for user input to process.
            #     action = event_handler.dispatch(event) # we send the event to our event_handler dispatch method, which will return an action as response

            #     if action is None:
            #         continue
            #     if isinstance(action, MovementAction): # TODO: Research isinstance()
            #         player.move(dx=action.dx, dy=action.dy)
            #     if isinstance(action, EscapeAction):
            #         raise SystemExit()


if __name__ == "__main__":
    main()

