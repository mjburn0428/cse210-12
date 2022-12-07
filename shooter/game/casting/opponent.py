from game.casting.actor import Actor
class Opponent(Actor):
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
