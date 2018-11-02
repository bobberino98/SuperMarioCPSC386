import pygame
from pygame.sprite import Sprite
from gravity import Gravity


class Mario(Sprite):
    SPEED_CAP = 5
    ACCEL_FACTOR = 0.025

    def __init__(self, screen, settings):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.gravity = Gravity()
        self.image = pygame.image.load("media/images/mario/regular.png")
        self.rect = self.image.get_rect()
        self.speed = 0
        self.dir = 1
        self.moving_right = False
        self.moving_left = False

    def __str__(self):
        return 'Mario: x:' + str(self.rect.x) + ' y:' + str(self.rect.y)

    def update(self, gamemap):  # Update and then blit
        if not gamemap.object_hit_ground(self):
            self.gravity.perform(self)
        if self.moving_left:
            self.dir = -1
            self.accelerate()
            self.rect.x += self.dir * self.speed

            # self.direction = None
        elif self.moving_right:
            self.dir = 1
            self.accelerate()
            self.rect.x += self.dir * self.speed

            # self.direction = None
        else:
            self.decelerate()
            self.rect.x += self.dir * self.speed


        self.blitme()

    def accelerate(self):
        if self.speed == 0:
            self.speed = 2 + Mario.ACCEL_FACTOR
        if self.speed < Mario.SPEED_CAP:
            self.speed *= 1 + Mario.ACCEL_FACTOR

    def decelerate(self):
        if self.speed > 0:
            self.speed -= Mario.ACCEL_FACTOR

    def blitme(self):   # Blit Mario
        self.screen.blit(self.image, self.rect)
