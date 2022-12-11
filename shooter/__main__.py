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
    # Setting the variables for game set up adn play
    gameRunning = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 40)
    lost_game_font = pygame.font.SysFont("cosmicsans", 60)

    opponents = []
    waveLength = 5
    bulletVelocity = 7
    opponentVelocity = 1

    player_vel = 7
    player = Player(650, 650)
    player2 = Player(325, 650)

    # keys = KeyboardService()

    clock = pygame.time.Clock()

    
    lost = False
    
    def redraw_window():
        WIN.blit(BG, (0,0))
        # draw text on screen
        lives_tag = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_tag = main_font.render(f"Level: {level}", 1, (255,255,255))

        WIN.blit(lives_tag, (10, 10))
        WIN.blit(level_tag, (SCREEN_WIDTH - level_tag.get_width() - 10, 10))

        for opponent in opponents:
            opponent.draw(WIN)

        player.draw(WIN)
        player2.draw(WIN)

        if lost:
            lost_label = lost_game_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (SCREEN_WIDTH/2 - lost_label.get_width()/2, 350))
        player.draw(WIN)
        player2.draw(WIN)
        
        pygame.display.update()

    while gameRunning:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0:
            lost = True
            gameRunning = False

        # if lost:
        #     if lost_count > FPS * 3:
        #         gameRunning = False
        #     else:
        #         continue

        # iterating through different levels
        if len(opponents) == 0:
            level = level + 1
            waveLength = waveLength + 1

            for i in range (waveLength):
                opponent = Opponent(random.randrange(50, SCREEN_WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                opponents.append(opponent)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                # gameRunning = False

        # keys to control the players
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

        if keys[pygame.K_a] and player2._x - player_vel > 0: # left
            player2._x -= player_vel
        if keys[pygame.K_d] and player2._x + player_vel + player2.get_width() < SCREEN_WIDTH: # right
            player2._x += player_vel
        if keys[pygame.K_w] and player2._y - player_vel > 0: # up
            player2._y -= player_vel
        if keys[pygame.K_s] and player2._y + player_vel + player2.get_height() + 15 < SCREEN_HEIGHT: # down
            player2._y += player_vel
        if keys[pygame.K_x]:
            player2.shoot()

        # moving the opponenets and collision
        for opponent in opponents:
            opponent.move(opponentVelocity)
            opponent.move_bullets(bulletVelocity, player)

            if random.randrange(0, 2*60) == 1:
                opponent.shoot()

            if collide(opponent, player):
                player._health -= 10
                opponents.remove(opponent)
                if player._health <= 0:
                    lives -= 1
                    player._health = player.max_health

            elif opponent._y + opponent.get_height() > SCREEN_HEIGHT:
                lives -= 1
                opponents.remove(opponent)

            if collide(opponent, player2):
                player2._health -= 10
                opponents.remove(opponent)
                if player2._health <= 0:
                    lives -= 1
                    player2._health = player2.max_health

        player.move_bullets(-bulletVelocity, opponents)
        player2.move_bullets(-bulletVelocity, opponents)

def main_menu():
    # make a title screen
    title_font = pygame.font.SysFont("comicsans", 70)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("To begin, Press the mouse...", 1, (255,255,255))
        WIN.blit(title_label, (SCREEN_WIDTH/2 - title_label.get_width()/2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()