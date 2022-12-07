import pygame
import os
import time
import random
pygame.font.init()

from constants import *
from game.casting.actor import Actor
from game.casting.player import Player
from game.services.keyboard_service import KeyboardService
from game.casting.opponent import Opponent



def main():
    gameRunning = True
    FPS = 60
    level = 0
    lives = 3
    main_font = pygame.font.SysFont("comicsans", 40)
    lost_game_font = pygame.font.SysFont("cosmicsans", 60)

    opponents = []
    waveLength = 5
    opponentVelocity = 1

    player_vel = 5
    player = Player(300, 650)

    # keys = KeyboardService()

    clock = pygame.time.Clock()

    
    lost = False
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text
        lives_tag = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_tag = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_tag, (10, 10))
        WIN.blit(level_tag, (SCREEN_WIDTH - level_tag.get_width() - 10, 10))

        for opponent in opponents:
            opponent.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_game_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (SCREEN_WIDTH/2 - lost_label.get_width()/2, 350))
        player.draw(WIN)
        # keys.get_direction()
        pygame.display.update()

    while gameRunning:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player._health <= 0:
            lost = False
            lost_count = 0

        if lost:
            if lost_count > FPS * 3:
                gameRunning = False
            else:
                continue


        if len(opponents) == 0:
            level = level + 1
            waveLength = waveLength + 1

            for i in range (waveLength):
                opponent = Opponent(random.randrange(50, SCREEN_WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                opponents.append(opponent)


                # opponent = opponent(random.randrange(50, SCREEN_WIDTH-100), random.randrange(-1500*level/3, -100)), random.choice(["red", "blue", "green"])
                # opponents.append(opponent)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

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


        for opponent in opponents:
            opponent.move(opponentVelocity)
            if opponent._y + opponent.get_height() > SCREEN_HEIGHT:
                lives -= 1
                opponents.remove(opponent)

       

main()

