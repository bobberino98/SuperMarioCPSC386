import pygame
from pygame.sprite import Sprite
from gravity import Gravity


class Mario(Sprite):
    SPEED_CAP = 5
    ACCEL_FACTOR = 0.025
    DECEL_FACTOR = 0.25
    FALL_FACTOR = 0.15
    TURN_FACTOR = 0.3

    def __init__(self, screen, settings, gamemap):
        super(Mario, self).__init__()
        self.screen = screen
        self.settings = settings
        self.gravity = Gravity()
        self.gamemap = gamemap
        self.image = pygame.image.load("media/images/mario/regular.png")
        self.rect = self.image.get_rect()
        self.speed = 0
        self.dir = 1
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.jump_finished = False
        self.jump_speed = 0

    def __str__(self):
        return 'Mario: x:' + str(self.rect.x) + ' y:' + str(self.rect.y)

    def update(self, gamemap):  # Update and then blit
        if not self.jumping and not gamemap.object_hit_ground(self):
            self.gravity.perform(self)
        if self.jumping:
            self.jump()
        else:
            self.jump_speed = 0
        if self.moving_left:
            if self.dir == 1 and self.speed != 0:
                self.turn()

            self.accelerate()
            self.rect.x += self.dir * self.speed

            # self.direction = None
        elif self.moving_right:
            if self.dir == -1 and self.speed != 0:
                self.turn()

            self.accelerate()
            self.rect.x += self.dir * self.speed

            # self.direction = None
        else:
            self.decelerate()
            self.rect.x += self.dir * self.speed
        self.rect.y -= self.jump_speed
        self.blitme()

    def accelerate(self):
        if self.speed == 0:
            self.speed = 2 + Mario.ACCEL_FACTOR
        if self.speed < Mario.SPEED_CAP:
            self.speed *= 1 + Mario.ACCEL_FACTOR

    def decelerate(self):
        if self.speed >= Mario.ACCEL_FACTOR:
            self.speed -= Mario.DECEL_FACTOR
        else:
            self.speed = 0

    def turn(self):
        if self.speed >= Mario.ACCEL_FACTOR:
            self.speed -= Mario.TURN_FACTOR
        else:
            self.speed = 0
            self.dir *= -1

    def jump(self):
        if not self.jump_finished:
            if self.jump_speed <= 0:
                self.jump_speed = 7

            else:
                self.jump_speed -= Mario.FALL_FACTOR
                if self.jump_speed <= 0:
                    self.jump_finished= True
        else:
            self.jump_speed -= Mario.FALL_FACTOR
            if self.gamemap.object_hit_ground(self):
                self.jump_finished = False

    def blitme(self):   # Blit Mario
        self.screen.blit(self.image, self.rect)
