import pygame as pg 
import os
from game.casting.actor import Actor
from constants import *
from bullet import Bullet


class Player(Actor):
    
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_bullets(self, velocity, objs):
        # moves its list of bullets
        self.cooldown()
        for bullet in self._bullets:
            bullet.moveBullet(velocity)
            if bullet.off_screen(SCREEN_HEIGHT):
                # bullets not allowed off screen
                self._bullets.remove(bullet)
            else:
                for obj in objs:
                    if bullet.collision(obj):
                        objs.remove(obj)
                        if bullet in self._bullets:
                            self._bullets.remove(bullet)

    def draw(self, window):
        # draws the player
        super().draw(window)
        self.healthBar(window)

    #Shows the health of the player
    def healthBar(self, window):
        pygame.draw.rect(window, (255,0,0), (self._x, self._y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self._x, self._y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self._health/self.max_health), 10))

