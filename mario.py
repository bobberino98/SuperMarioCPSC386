from pygame.sprite import Sprite
from gravity import Gravity
from imagerect import ImageRect


class Mario(Sprite):
    SPEED_CAP = 5
    ACCEL_FACTOR = 0.025
    DECEL_FACTOR = 0.25
    FALL_FACTOR = 0.20
    TURN_FACTOR = 0.3

    def __init__(self, screen, settings, gamemap):
        super(Mario, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.gravity = Gravity()
        self.gamemap = gamemap
        self.img_rect = ImageRect(screen, "media/images/mario/regular", 32, 32)

        self.rect = self.img_rect.rect
        self.rect.y = self.screen_rect.top
        self.rect.x = self.screen_rect.left
        self.dist = 0
        self.speed = 0
        self.dir = 1
        self.moving_right = False
        self.moving_left = False
        self.jumping = False
        self.jump_finished = False
        self.jump_speed = 0
        self.jump_start = False

    def __str__(self):
        return 'Mario: x:' + str(self.rect.x) + ' y:' + str(self.rect.y)

    def update(self, gamemap):  # Update and then blit
        if not self.jumping and not gamemap.object_hit_ground(self):
            self.gravity.perform(self)

        if not self.jump_start and self.gamemap.object_hit_ground:
            self.jump_start = True
        if self.jumping:
            self.jump()
        elif self.jumping and gamemap.object_hit_ground(self):
            self.jump()
        else:
            self.jump_speed = 0
        if self.moving_left:
            if self.dir == 1 and self.speed != 0:
                self.turn()
            elif self.dir == 0:
                self.dir = -1
            self.accelerate()
            if self.rect.x > 0:
                self.rect.x += self.dir * self.speed

        elif self.moving_right:
            if self.dir == -1 and self.speed != 0:
                self.turn()
            elif self.dir == 0:
                self.dir = 1
            self.accelerate()
            if self.rect.centerx >= self.screen_rect.width/2:
                self.gamemap.scroll(self.speed)
            else:
                self.rect.x += self.dir * self.speed
        else:
            self.decelerate()
            if self.rect.x > 0 and self.rect.right < self.screen_rect.width:
                self.rect.x += self.dir * self.speed

        self.rect.y -= self.jump_speed
        self.img_rect.rect = self.rect
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
            self.dir = 0

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
                    self.jump_finished = True
                elif self.gamemap.object_hit_ground(self):
                    self.jump_finished = True

                    self.jump_speed *= -1
        else:
            self.jump_speed -= Mario.FALL_FACTOR
            if self.gamemap.object_hit_ground(self):
                self.jump_finished = False

    def blitme(self):  # Blit Mario
        self.img_rect.blitme()
