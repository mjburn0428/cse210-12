import pygame
import os

# SCREEN
# WIDTH, HEIGHT = 750, 750
SCREEN_WIDTH = 950
SCREEN_HEIGHT = 750
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2


WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooter game")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_yellow.png"))
YELLOW_PLAYER_TWO = pygame.image.load(os.path.join("shooter/assets", "pixel_ship_yellow.png"))

# BULLETS
RED_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("shooter/assets", "background-black.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))

def collide(obj1, obj2):
    offset_x = obj2._x - obj1._x
    offset_y = obj2._y - obj1._y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None