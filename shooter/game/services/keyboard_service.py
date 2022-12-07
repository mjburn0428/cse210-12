import pygame
from constants import *
from game.casting.actor import Actor
from game.casting.player import Player

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
        
        player = Player(300, 650)


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player._x - player_vel > 0: # left
            player._x -= player_vel
        if keys[pygame.K_RIGHT] and player._x + player_vel + player.get_width() < SCREEN_WIDTH: # right
            player._x += player_vel
        if keys[pygame.K_UP] and player._y - player_vel > 0: # up
            player._y -= player_vel
        if keys[pygame.K_DOWN] and player._y + player_vel + player.get_height() + 15 < SCREEN_HEIGHT: # down
            player._y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        # direction = (x, y)
        # direction = direction.scale(self._cell_size)
        # return direction