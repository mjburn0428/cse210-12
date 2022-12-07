import pygame
import os
from game.casting.actor import Actor


RED_SPACE_SHIP = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_yellow.png"))

class Player(Actor):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
