from game.casting.actor import Actor
from game.casting.bullet import Bullet
from constants import *
class Opponent(Actor):
    # randomized coloration
    COLOR_MAP = {
                "red": (RED_SPACE_SHIP, RED_LASER),
                "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                }
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)


    def move(self, velocity):
        self._y += velocity

    # Allow bullet from opponent to be shot from the center instead of the side
    def shoot(self):
        if self.cool_down_counter == 0:
            bullet = Bullet(self._x-20, self._y, self.laser_img)
            self._bullets.append(bullet)
            self.cool_down_counter = 1