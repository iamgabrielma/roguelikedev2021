class Action:
    pass

class EscapeAction(Action):
    pass

class MovementAction(Action):
    # TODO: research
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
