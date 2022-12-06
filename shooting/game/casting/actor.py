from game.casting.text import Text

class Actor:
    """A thing participating in the game"""

    def __init__(self, debug = False):
        self._debug = debug

    def is_debug(self):
        return self._debug