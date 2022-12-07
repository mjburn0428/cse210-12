import pygame

from game.casting.actor import Actor

class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        # self._cell_size = cell_size
        pass

    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        
        player_vel = 5
    
        ship = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship._x - player_vel > 0: # left
            ship._x -= player_vel
        if keys[pygame.K_RIGHT] and ship._x + player_vel + ship.get_width() < SCREEN_WIDTH: # right
            ship._x += player_vel
        if keys[pygame.K_UP] and ship._y - player_vel > 0: # up
            ship._y -= player_vel
        if keys[pygame.K_DOWN] and ship._y + player_vel + ship.get_height() + 15 < SCREEN_HEIGHT: # down
            ship._y += player_vel
        if keys[pygame.K_SPACE]:
            ship.shoot()

        # direction = (x, y)
        # direction = direction.scale(self._cell_size)
        # return direction