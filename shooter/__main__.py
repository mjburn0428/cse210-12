import pygame
import os
import time
import random
pygame.font.init()
from game.casting.actor import Actor
# from game.services.keyboard_service import KeyboardService

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

# Lasers
RED_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("shooter/assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("shooter/assets", "background-black.png")), (SCREEN_WIDTH, SCREEN_HEIGHT))





def main():
    gameRunning = True
    FPS = 60
    level = 1
    lives = 3
    main_font = pygame.font.SysFont("comicsans", 40)

    player_vel = 5
    ship = Actor(300, 650)

    # keys = KeyboardService()

    clock = pygame.time.Clock()
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text
        lives_tag = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_tag = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_tag, (10, 10))
        WIN.blit(level_tag, (SCREEN_WIDTH - level_tag.get_width() - 10, 10))

        # for enemy in enemies:
        #     enemy.draw(WIN)

        # player.draw(WIN)

        # if lost:
        #     lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
        #     WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
        ship.draw(WIN)
        # keys.get_direction()
        pygame.display.update()

    while gameRunning:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

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


main()

