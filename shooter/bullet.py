import pygame
from constants import *

class Bullet:
    def __init__(self, x, y, img):
        self._x = x
        self._y = y
        self._img = img
        self.mask = pygame.mask.from_surface(self._img)

    def draw(self, window):
        window.blit(self._img, (self._x, self._y))
    
    def move(self, velocity):
        self._y += velocity

    def off_screen(self, height):
        return not(self._y <= height and self._y >= 0)

    def collision(self, obj):
        return collide(obj, self)

# def collide(obj1, obj2):
#     offset_x = obj2._x - obj1._x
#     offset_y = obj2._y - obj1._y
#     return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None