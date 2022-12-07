import pygame

class Actor:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self._x = x
        self._y = y
        self._health = health
        self._ship_img = None
        self._bullet_img = None
        self._bullets = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (225,0,0), (self._x, self._y, 50, 50))
        # window.blit(self._ship_img, (self._x, self._y))
    #     for bullet in self.bullets:
    #         laser.draw(window)

    # def move_lasers(self, vel, obj):
    #     self.cooldown()
    #     for laser in self.lasers:
    #         laser.move(vel)
    #         if laser.off_screen(SCREEN_HEIGHT):
    #             self.lasers.remove(laser)
    #         elif laser.collision(obj):
    #             obj.health -= 10
    #             self.lasers.remove(laser)

    # def cooldown(self):
    #     if self.cool_down_counter >= self.COOLDOWN:
    #         self.cool_down_counter = 0
    #     elif self.cool_down_counter > 0:
    #         self.cool_down_counter += 1

    # def shoot(self):
    #     if self.cool_down_counter == 0:
    #         laser = Laser(self.x, self.y, self.laser_img)
    #         self.lasers.append(laser)
    #         self.cool_down_counter = 1

    # def get_width(self):
    #     return self._ship_img.get_width()

    # def get_height(self):
    #     return self._ship_img.get_height()