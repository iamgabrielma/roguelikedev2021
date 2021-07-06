class Engine:
"""
Take the responsibily of drawing the map and entities, as well as handling the player’s input. 
"""
	def __init__(self, entities: Set[Entity], event_handler: EventHandler, player: Entity):
		"""
		- entities: We'll use a SET, as elements must be unique and can't be added twice.
		- event_handler: 
		- player: Outside of Set[Entity] just for easier access
		"""
		self.entities = entities
		self.event_handler = event_handler
		self.player = player

	def handle_events():
		"""
		"""
		pass

	def render():
		"""
		"""
		pass
