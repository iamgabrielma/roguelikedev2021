from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from actions import EscapeAction, MovementAction
from entity import Entity
from input_handlers import EventHandler
from game_map import GameMap

class Engine:

	def __init__(self, entities: Set[Entity], event_handler: EventHandler, game_map: GameMap, player: Entity):
		"""
		- entities: We'll use a SET, as elements must be unique and can't be added twice.
		- event_handler: 
		- player: Outside of Set[Entity] just for easier access
		"""
		self.entities = entities
		self.event_handler = event_handler
		self.game_map = game_map
		self.player = player

	def handle_events(self, events: Iterable[Any]) -> None:
		"""

		"""
		for event in events:
			action = self.event_handler.dispatch(event) # we send the event to our event_handler dispatch method, which will return an action as response

			if action is None:
				continue

			if isinstance(action, MovementAction):
				#self.player.move(dx=action.dx, dy=action.dy)
				if self.game_map.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
					self.player.move(dx=action.dx, dy=action.dy)

			elif isinstance(action, EscapeAction):
				raise SystemExit()

	def render(self, console: Console, context: Context) -> None:
		"""
		Handles screen drawing
		"""
		self.game_map.render(console)

		for entity in self.entities:
			console.print(entity.x, entity.y, entity.char, fg=entity.color)

		context.present(console) # present() is what will print on screen, is like the loop Update() method
		console.clear() # We clear the console before running the next loop
		
