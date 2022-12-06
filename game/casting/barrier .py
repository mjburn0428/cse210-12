from game.casting.actor import Actor 

class Barrier(Actor):
    """The solid object that servers as a barrier"""
    def __init__(self, body, animation, points, debug=False):
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points

    def get_animation(self):
        return self._animation

    def  get_body(self):
        return self._body

    def get_points(self):
        return self._points