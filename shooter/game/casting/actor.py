import pygame
from constants import *
from game.casting.bullet import Bullet


class Actor:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self._x = x
        self._y = y
        self._health = health
        self.ship_img = None
        self._bullet_img = None
        self._bullets = []
        self.cool_down_counter = 0

    def draw(self, window):
        # pygame.draw.rect(window, (225,0,0), (self._x, self._y, 50, 50))
        window.blit(self.ship_img, (self._x, self._y))
        for bullet in self._bullets:
            bullet.draw(window)

    def move_bullets(self, velocity, obj):
        self.cooldown()
        for bullet in self._bullets:
            bullet.move(velocity)
            if bullet.off_screen(SCREEN_HEIGHT):
                self._bullets.remove(bullet)
            elif bullet.collision(obj):
                obj._health -= 10
                self._bullets.remove(bullet)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            bullet = Bullet(self._x, self._y, self.laser_img)
            self._bullets.append(bullet)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()